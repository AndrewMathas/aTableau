#!/usr/bin/env -S uv run --script

# ---------------------------------------------------------------------------
# test_atableau.py - Andrew Mathas (C) 2022-2026
#
# Requires:
#  - uv -- this runs the script and installs the python dependencies
#  - ImageMagick is used to create image diffs of changed files
# ---------------------------------------------------------------------------

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "pdf2image",
#     "pillow",
# ]
# ///


r"""
usage: test_atableau.py [-hh] [-d] [-k] [-q] [-v] [-t THRESHOLD] [-w WORKERS]
                        [-e | -i | -u] [files ...]

positional arguments:
  files                     Example files to test, with wild cards applied (default: all files)

options:
  -e, --extract             Extract the examples from the aTableau manual
  -i, --initialise          Initialise all of the good webp files for future comparisons
  -u, --update              Update the good files as they are checked
  -d, --diff                Open image-diffs for the examples that have changed (requires magick)
  -k, --keep                Keep the generated example image files
  -q, --quiet               Quiet mode: only print files with discrepancies
  -v, --verbose             Enable verbose printing
  -t, --threshold THRESHOLD Percentage of pixels that must differ (default: 0.05)
  -w, --workers WORKERS     Number of workers to use when checking examples (default: 16)
  -h, -hh                   Help (use -hh for extended help)
"""

HELP = r"""
This python script is part of the aTableau LaTeX package. It can be used to
check that the output from the aTableau example files have not changed during
development. The example files are extracted from the aTableau manual,
atableau.tex, which is assumed to either be in the same directory as this
script, or in the parent directory. If it does not already exist, the script
creates a symbolic link that is the python equivalent of

    ln -s ../atableau.tex atableau-examples.tex

Running pdflatex on the file atableau-examples.tex extracts all of the examples
from the manual, creating a separate file in the current directory for each
example.  Running this script on the example files compares their output with
the expected output.

BEFORE starting development, the examples files should be initialised using

    test_examples.py -i

This will extract the examples from the manual, and then create a "good" webp
file for each example, such as ribbon-good.webp, for the example ribbon.tex.
The "good" webp files are then used as proxies for the expected output for the
examples.

Once the good files have been initialised, the command

    test_examples.py [files]

compiles and tests all of the matching files to check for changes. The optional
argument  <files> is interpreted liberally with wild-card expansions on both sides.
For example,

    test_examples.py tableau

tests all of the example files with names that contain 'tableau'. Use

    test_examples.py -d tableau

to display image diffs of each discrepancy with a good file.

When new examples are added to the manual, they can be extracted using:

    test_examples.py -e

When they do not already exist, this will also create good webp images files
for the examples, but it will not overwrite any existing good webp files. In
fact, the `-e` option rewrites all of the example LaTeX files, without
changing the good image files. The examples should be regularly extracted
from manual as they can change, or new examples are added.

If any of the examples in the manual change in a good way, in the sense that
the example is corrected, or improved, then the good images can be updated
using:

    test_examples -u [files]

There are over 200 examples in the manual, but this script is reasonably quick
in checking all of the example files because they are processed in parallel.

Andrew Mathas 2025-26
"""

# ------------------------------------------------------------------------
import argparse
import os
import platform
import signal
import subprocess
import sys
import tempfile

# for running in parallel
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy

# image conversion and comparison
from pdf2image import convert_from_path
from PIL import Image, ImageChops

# ------------------------------------------------------------------------
# execution

# An image magick command to open up an example image and its good
# version, with an image-diff in the middle.
COMPARE_IMAGES = r"""magick {image}.webp {image}-good.webp \
  \( -clone 0 -fuzz 10% -trim +repage -bordercolor white -border 20 \) \
  \( -clone 1 -fuzz 10% -trim +repage -bordercolor white -border 20 \) \
  \( -clone 2 -clone 3 -compose difference -composite -threshold 5% \
     -fill red -opaque white -transparent black \) \
  \( -clone 3 -clone 4 -compose over -composite \) \
  -delete 0,1,4 \
  -swap 1,2 \
  -background white -bordercolor white -border 10 \
  -bordercolor blue -border 5 \
  +smush +10 {image_diff}
"""

# Per-pixel colour difference (0-255) at or below which a change is treated as
# rendering/encoding noise rather than a genuine change to the example.
PIXEL_TOLERANCE = 8


def run_command(cmd):
    r"""
    Short-cut for shell commands. On failure the raised CalledProcessError
    carries the captured output (as text) so the caller can surface the error.
    """
    subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)


def _ignore_sigint():
    """
    Worker initialiser: ignore Ctrl-C in the workers so that a SIGINT interrupts
    only the main process, which then shuts the pool down (see below). Without
    this the workers each raise their own KeyboardInterrupt and spew tracebacks.
    """
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def run_parallel_command(options, files):
    """
    Run parallel commands corresponding to options.action on the list of
    example files.
    """
    command = ACTIONS[options.action]
    bad_examples = []
    # Not using a `with` block: on Ctrl-C its __exit__ would call shutdown(wait=True)
    # and block until every queued task finished -- making Ctrl-C look ignored.
    executor = ProcessPoolExecutor(
        max_workers=options.workers, initializer=_ignore_sigint
    )
    try:
        futures = {executor.submit(command, file, options): file for file in files}
        passed = 0
        for future in as_completed(futures):
            file = futures[future]
            try:
                result = future.result()  # Raises exception if command() fails
                if result:
                    bad_examples.append(result)
                else:
                    passed += 1

            except Exception as error:
                message = f"Error running {options.action} on {file}: {error}"
                # surface the tail of any captured output (e.g. the LaTeX error)
                output = getattr(error, "stdout", "") or getattr(error, "output", "")
                if output:
                    message += "\n" + "\n".join(str(output).splitlines()[-15:])
                print(red_text(message))
                bad_examples.append(message)

    except KeyboardInterrupt:
        print(red_text("\nInterrupted -- stopping."), flush=True)
        # terminate the workers (they ignore SIGINT) so shutdown returns at once
        # instead of waiting for the queued examples to finish compiling
        for process in getattr(executor, "_processes", {}).values():
            process.terminate()
        executor.shutdown(wait=True)
        sys.exit(130)

    executor.shutdown(wait=True)

    if bad_examples:
        if options.action == "updating":
            for file in bad_examples:
                # ask for confirmation before updating good image files
                # we can't do this from inside a parallel worker
                if "Error" in file:
                    print(file)
                else:
                    response = input(f"Update good image for {file}? [N/y] ")
                    if response.strip().lower() in ["y", "yes"]:
                        os.replace(f"{file}.webp", f"{file}-good.webp")
                        print(f" - {example_number(file):<14} updated ({file})")

        elif not options.quiet:
            print("\nChanged examples:\n" + "\n".join(sorted(bad_examples)))

    if not options.quiet:
        print(f"\n{passed} examples {options.action.replace('ing', 'ed')}")


def open_file(file):
    r"""
    Open an (image) file. Exactly how this is done is platform dependent.
    """
    match platform.system():
        case "Darwin":
            subprocess.run(["open", str(file)])
        case "Linux":
            subprocess.run(["xdg-open", str(file)])
        case "Windows":
            os.startfile(str(file))


# ------------------------------------------------------------------------
# utility functions


def red_text(text):
    """
    Return a string that makes `text` red  when printed to the terminal
    """
    return f"\033[31m{text}\033[39m"


def example_number(file):
    """
    Look in the example file `file`.tex to find the example number, which is on
    a line of the form "% Example N, page M".
    """
    with open(f"{file}.tex", "r") as example:
        for line in example:
            if line.startswith("% Example"):
                return line[1:].strip()

    raise ValueError(red_text(f" - no '% Example ...' line found in {file}.tex"))


def make_image(file, ext):
    """
    Make a webp image for the example `file` with the specified
    "extension", which is either '-good.webp' or '.webp'
    """
    if not os.path.isfile(f"{file}.tex"):
        raise FileNotFoundError(red_text(f" - {file} not found!"))

    # make the LaTeX file halt on error, otherwise run_parallel_command will hang
    run_command(f"pdflatex -halt-on-error -interaction=nonstopmode {file}")
    os.remove(f"{file}.log")

    # make the webp image file
    webp = convert_from_path(f"{file}.pdf", last_page=1)
    webp[0].save(f"{file}{ext}", "WEBP")
    os.remove(f"{file}.pdf")


def different_images(file, options):
    """
    Return `True` or `False` depending on whether the image has changed.

    Two images differ if their dimensions differ, or if more than
    `options.threshold` percent of their pixels differ by more than
    PIXEL_TOLERANCE.  Counting the fraction of meaningfully-changed pixels is
    both scale-independent and sensitive to small, localised changes, whereas
    the mean difference over the whole image is neither.
    """
    image = Image.open(f"{file}.webp")
    good = Image.open(f"{file}-good.webp")

    # A change in size is always a change. (Otherwise ImageChops.difference
    # silently compares only the overlapping region and can miss the change.)
    if image.size != good.size:
        if options.verbose:
            print(f"{file=}: size changed {good.size} -> {image.size}")
        return True

    # per-pixel change magnitude (max across colour channels), then the
    # percentage of pixels that changed by more than the tolerance
    diff = numpy.asarray(ImageChops.difference(image, good))
    per_pixel = diff.max(axis=-1) if diff.ndim == 3 else diff
    changed = 100.0 * numpy.count_nonzero(per_pixel > PIXEL_TOLERANCE) / per_pixel.size

    if options.verbose:
        print(f"{file=}: {changed=:.3f}%")
    return changed > options.threshold


def find_example_files(files):
    """
    Determine the files to look at -- we glob for maximum effect
    """
    example_files = []
    for file in files:
        pattern = file if "." in file else f"*{file}*.tex"
        example_files.extend(Path(f).stem for f in Path().glob(pattern))

    # remove the files that we don't want to test
    for bad in ["", "atableau-examples"]:
        try:
            example_files.remove(bad)
        except ValueError:
            pass

    return example_files


# ------------------------------------------------------------------------
# action -> ACTION[action] = {action}_image()


def initialising_image(file, options):
    """
    Recompile the LaTeX example and convert the PDF file to a webp file
    to a "good" webp image, with name `file`-good.webp
    """
    make_image(file, "-good.webp")
    if not options.quiet:
        print(f" - {example_number(file):<14} image created ({file}-good.webp)")


def extracting_image(file, options):
    """
    After updating the example LaTeX files, make good image files for
    any new examples.
    """
    if not os.path.isfile(f"{file}-good.webp"):
        initialising_image(file, options)


def updating_image(file, options):
    """
    Update the good webp image for file
    """
    make_image(file, ".webp")
    if different_images(file, options):
        return file

    else:
        if not options.quiet:
            print(
                f" - {example_number(file):<14} has not changed ({file}): NOT updated"
            )
        if not options.keep:
            os.remove(f"{file}.webp")


def checking_image(file, options):
    """
    Check to see whether the webp file is good
    """
    make_image(file, ".webp")
    example, page = example_number(file).split(", ")
    if different_images(file, options):
        bad_example = f" - {example:<13}: BAD {page:<7} ({file})"
        print(red_text(bad_example))
        if options.diff:
            # create a side-by-side image and then open it
            image_diff = Path(tempfile.gettempdir()) / f"{file}.png"
            run_command(COMPARE_IMAGES.format(image=file, image_diff=image_diff))
            open_file(image_diff)

        return bad_example

    elif not options.quiet:
        print(f" - {example:<13}: OK  {page:<7} ({file})")

    if not options.keep:
        os.remove(f"{file}.webp")


# possible action commands
ACTIONS = {
    "checking": checking_image,
    "initialising": initialising_image,
    "extracting": extracting_image,
    "updating": updating_image,
}

# ------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="test aTableau example files for changes",
        add_help=False,  # will override default help
    )

    parser.add_argument(
        "files",
        nargs="*",
        default=[""],
        help="Example files to test, with wild cards applied (default: all files)",
    )

    action = parser.add_mutually_exclusive_group()
    action.set_defaults(action="checking")
    action.add_argument(
        "-e",
        "--extract",
        action="store_const",
        const="extracting",
        dest="action",
        help="Extract the examples from the aTableau manual",
    )
    action.add_argument(
        "-i",
        "--initialise",
        action="store_const",
        const="initialising",
        dest="action",
        help="Initialise all of the good webp files for future comparisons",
    )
    action.add_argument(
        "-u",
        "--update",
        action="store_const",
        const="updating",
        dest="action",
        help="Update the good files as they are checked",
    )

    parser.add_argument(
        "-d",
        "--diff",
        action="store_true",
        default=False,
        help="open image-diffs for the examples that have changed",
    )

    parser.add_argument(
        "-k",
        "--keep",
        action="store_true",
        default=False,
        help="Keep example image files (default: False)",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="Quiet mode: only print files with discrepancies (default: False)",
    )

    parser.add_argument(
        "-t",
        "--threshold",
        action="store",
        type=float,
        default=0.05,
        help="Percentage of pixels that must differ for a change (default: 0.05)",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Enables verbose printing",
    )

    parser.add_argument(
        "-w",
        "--workers",
        action="store",
        type=int,
        default=16,
        help="Number of workers/threads to use when checking examples (default: 16)",
    )

    parser.add_argument("-h", "--help", action="count", default=0)

    options = parser.parse_args()

    # if run from the atableau directory, cd into the tests directory
    if os.path.basename(os.getcwd()) == "aTableau":
        os.chdir("tests")

    # help those who ask for help
    if options.help > 0:
        parser.print_help()
        if options.help == 1:
            sys.stdout.write("\nFor extended help use -hh\n")
        else:
            sys.stdout.write(HELP)
        sys.exit()

    if not os.path.isfile("atableau-examples.tex"):
        print("Adding a symlink to atableau-examples.tex")
        if os.path.isfile("atableau.tex"):
            os.symlink("atableau.tex", "atableau-examples.tex")
        elif os.path.isfile("../atableau.tex"):
            os.symlink("../atableau.tex", "atableau-examples.tex")
        else:
            raise FileNotFoundError(
                red_text(" - unable to find atableau.tex and atableau-examples.tex")
            )

        # next extract the example files
        options.action = "extracting"

    if options.action == "extracting":
        print("Extracting example files from the aTableau manual")
        example_files = find_example_files([""])

        # remove all of the old example files in case some names have changed
        for f in Path().glob("*.tex"):
            if f.stem != "atableau-examples":
                f.unlink(missing_ok=True)

        # extract the examples from the manual (and clean up latex files)
        run_command(
            "pdflatex -halt-on-error -interaction=nonstopmode atableau-examples"
            " && latexmk -C atableau-examples"
        )

    # populate the list of examples that we need to look at
    example_files = find_example_files(options.files)

    # act on the example files
    run_parallel_command(options, example_files)
