#!/usr/bin/env -S uv run --script

# ---------------------------------------------------------------------------
# test_atableau.py - Andrew Mathas (C) 2022-2026
#
# Requires: uv -- this runs the script and installs the python dependencies
# ---------------------------------------------------------------------------

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "pdf2image",
#     "pillow",
# ]
# ///


r'''
usage: test_atableau.py [-h] [-q] [-t THRESHOLD] [-w WORKERS] [-e | -i | -u] [files ...]

positional arguments:
  files                 Example files to test, with wild cards applied (default: all files)

options:
  -e, --extract             Extract the examples from the aTableau manual
  -i, --initialise          Initialise all of the good webp files for future comparisons
  -o, --open                open the good images files for the examples that have changed
  -q, --quiet               Quite mode: only print files with discrepancies
  -t, --threshold THRESHOLD Threshold for image comparison (default: 5)
  -u, --update              Update the good files as they are checked
  -w, --workers WORKERS     Number of workers/threads to use when checking examples (default: 8)
'''

HELP = r'''
This python script is part of the aTableau LaTeX package. It can be used to
check that the output from the aTableau example files has not changed during
development. The example files are extracted from the aTableau manual,
atableau.tex, which is assumed to either be in the same directory as this
script, or in the parent directory. If it does not already exist, the script
creates a symbolic link that is the python equivalent of

    ln -s ../atableau.tex atableau-examples.tex

Running pdflatex on the file atableau-examples.tex extracts all of the examples
in the manual, creating a separate file in this directory for each example.
Running this script on the example files compares their output with the
expected output.

BEFORE starting development, the examples files should be initialised using

    test_examples.py -i

This will extract the examples from the manual, and then create a "good" webp
file for each example, such as ribbon-good.webp. The "good" webp files are
then used as proxies for the expected output of the examples.

Once the good files have been initialised, the command

    test_examples.py [files]

compiles and tests all of the matching files to check for changes. Here, <file>
is interpreted liberally with wild-card expansions on both sides. For example,

    test_examples.py tableau

tests all of the example files with names that contain 'tableau'. When new
examples are added to the manual, they can be extracted using:

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
because the examples are processed in parallel.

Andrew Mathas
October 2025
'''

# ------------------------------------------------------------------------
import argparse
import glob
import numpy
import os
import subprocess
import sys

# image conversion and comparison
from pdf2image import convert_from_path
from PIL import Image, ImageChops

# for running in parallel
from concurrent.futures import ProcessPoolExecutor, as_completed

# ------------------------------------------------------------------------
# execution

def run_command(cmd):
    r'''
    Short-cut for shell commands
    '''
    return subprocess.check_output(cmd, shell=True).strip()

def run_parallel_command(options, files):
    '''
    Run parallel commands corresponding to options.action on the list of
    example files.
    '''
    with ProcessPoolExecutor(max_workers=options.workers) as executor:
        command = globals()[f'{options.action}_image'] 
        futures = {executor.submit(command, file, options): file for file in files}
        for future in as_completed(futures):
            file = futures[future]
            try:
                future.result()  # Raises exception if command() fails
            except Exception as error:
                print(f'Error running {command.__name__} on {file}: {error}')

# ------------------------------------------------------------------------
# utility functions

def red_text(text):
    '''
    Return a string that makes `text` red  when printed to the terminal
    '''
    return f'\033[31m{text}\033[39m'

def example_number(file):
    '''
    Look in the example file `file`.tex to find the example number
    '''
    with open(f'{file}.tex', 'r') as example:
        for line in example:
            if line.startswith('% Example'):
                break

    return line[1:].strip()

def make_image(file, ext):
    '''
    Make a webp image for the example `file` with the specified
    "extension", which is either '-good.webp' or '.webp'
    '''
    if not os.path.isfile(f'{file}.tex'):
        raise FileNotFoundError( red_text(f' - {file} not found!') )

    # make the LaTeX file halt on error, otherwise run_parallel_command will hang
    run_command(f'pdflatex -halt-on-error {file}')
    os.remove(f'{file}.log')

    # make the webp image file
    webp = convert_from_path(f'{file}.pdf', last_page=1)
    webp[0].save(f'{file}{ext}', 'WEBP')
    os.remove(f'{file}.pdf')

def different_images(file, options):
    '''
    Return `True` or `False` depending on whether the image has changed
    '''
    diff = ImageChops.difference(Image.open(f'{file}.webp'), Image.open(f'{file}-good.webp'))
    diff_array = numpy.array(diff)
    mean_diff = diff_array.mean()

    return mean_diff > options.threshold

def find_example_files(files):
    '''
    Determine the files to look at -- we glob for maximum effect
    '''
    example_files = []
    for file in files:
        if '.' in file:
            example_files.extend([f[:-4] for f in glob.glob(file)])
        else:
            example_files.extend([f[:-4] for f in glob.glob(f'*{file}*.tex')])

    # remove the files that we don't want to test
    for bad in ['', 'atableau-examples']:
        try:
            example_files.remove(bad)
        except ValueError:
            pass

    return example_files


# ------------------------------------------------------------------------
# actions -> {action}_image()

def initialising_image(file, options):
    '''
    Recompile the LaTeX example and convert the PDF file to a webp file
    to a "good" webp image, with name `file`-good.webp
    '''
    make_image(file, '-good.webp')
    if not options.quiet:
        print(f' - {example_number(file):<14} image created ({file}-good.webp)')

def extracting_image(file, options):
    '''
    After updating the example LaTeX files, make good image files for
    any new examples.
    '''
    if not os.path.isfile(f'{file}-good.webp'):
        initialising_image(file, options)

def updating_image(file, options):
    '''
    Update the good webp image for file
    '''
    make_image(file, '.webp')
    if different_images(file, options):
        os.replace(f'{file}.webp', f'{file}-good.webp')
        if not options.quiet:
            print(f' - {example_number(file):<14} updated ({file}.webp)')
    else:
        os.remove(f'{file}.webp')

def checking_image(file, options):
    '''
    Check to see whether the webp file is good
    '''
    make_image(file, '.webp')
    if different_images(file, options):
        print( red_text(f' - Changed: {example_number(file):<14}  ({file})') )
        if options.open:
            run_command(f'open {file}-good.webp')

    elif not options.quiet:
        print(f' - {example_number(file):<14} OK ({file})')
        os.remove(f'{file}.webp')

# ------------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='test aTableau example files for changes',
        add_help=False  # will override default help
    )

    parser.add_argument('files',
        nargs='*',
        default=[''],
        help='Example files to test, with wild cards applied (default: all files)'
    )

    action = parser.add_mutually_exclusive_group()
    action.add_argument('-e', '--extract',
        action='store_const',
        const='extracting',
        default='checking',
        dest='action',
        help='Extract the examples from the aTableau manual'
    )
    action.add_argument('-i', '--initialise',
        action='store_const',
        const='initialising',
        dest='action',
        help='Initialise all of the good webp files for future comparisons'
    )
    action.add_argument('-u', '--update',
        action='store_const',
        const='updating',
        dest='action',
        help='Update the good files as they are checked'
    )

    parser.add_argument('-o', '--open',
        action='store_true',
        default=False,
        help='open the good images files for the examples that have changed'
    )

    parser.add_argument('-q', '--quiet',
        action='store_true',
        default=False,
        help='Quite mode: only print files with discrepancies (default: False)'
    )

    parser.add_argument('-t', '--threshold',
        action='store',
        type=int,
        default=5,
        help= f'Threshold for image comparison (default: 5)'
    )

    parser.add_argument('-w', '--workers',
        action='store',
        type=int,
        default=8,
        help= f'Number of workers/threads to use when checking examples (default: 8)'
    )

    parser.add_argument('-h', '--help', action='count', default=0)

    options = parser.parse_args()

    # if run from tyhe atableau directory, cd into the tests directory
    if os.path.basename( os.getcwd() ) == 'aTableau':
        os.chdir('tests')

    # help those who ask for help
    if options.help > 0:
        parser.print_help()
        if options.help == 1:
            sys.stdout.write('\nFor extended help use -hh\n')
        else:
            sys.stdout.write(HELP)
        sys.exit()

    if not os.path.isfile('atableau-examples.tex'):
        print('Adding a symlink to atableau-examples.tex')
        if os.path.isfile('atableau.tex'):
            os.symlink('atableau.tex', 'atableau-examples.tex')
        elif os.path.isfile('../atableau.tex'):
            os.symlink('../atableau.tex', 'atableau-examples.tex')
        else:
            raise FileNotFoundError( red_text(' - unable to find atableau.tex and atableau-examples.tex') )
            sys.exit(1)

        # next extract the example files
        options.action = 'extracting'

    if options.action == 'extracting':
        print('Extracting example files from the aTableau manual')
        example_files = find_example_files([''])
        # remove all of the old example files in case some names have changed
        run_command(f'rm -f {" ".join(f"{f}.tex" for f in example_files)}')
        # extract the examples from the manual (and clean up latex files)
        run_command('pdflatex -halt-on-error atableau-examples && latexmk -C atableau-examples')

    # populate the list of examples that we need to look at
    example_files = find_example_files(options.files)

    # act on the example files
    run_parallel_command(options, example_files)
