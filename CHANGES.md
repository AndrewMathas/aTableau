![version](https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=aTableau&v=2)
![LPPL](https://img.shields.io/badge/license-LPPL%201.3c-orange)
[![CTAN](https://img.shields.io/ctan/v/atableau?color=blue)](https://ctan.org/pkg/atableau)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff)

# **aTableau** - Change log

## Version 2.2.2 - 2026-06-30

- Adds `entries=ladders` for ladder numbers in diagrams
- Fixes a bug with the `beads` key, so that empty runners now work as advertised when abacuses are specified by their quotients
- Removes dependence on the `atableau.ini` file

## Version 2.2.1 - 2026-06-02

- Allows arbitrary TikZ coordinates to be used to position **aTableau** pictures inside `tikzpicture` environments
- Allows `colour theme` to define a custom colour theme
- Allows `cover` key to now be used with multishapes
- Allows `entries=last` to be used with skew shapes
- Adds `entries=columns` and `entries=rows`
- Adds image diffs to the testing framework
- Reads metadata directly from the `atableau.ini` file
- Updates tableaux naming conventions

## Version 2.2.0 - 2025-10-10

- Allows _generalised ribbon tableaux_ with `c`, `C`, `r` and `R` specifications
- Allows _complex styles_ in abacuses and tableaux to be entered as `[...]`, instead of `[{...}]`
- Allows abacuses to be specified by _quotients_
- Adds optional _overlay specifications_ for use with **beamer**
- Adds the `\NewATableauCommand` command for creating custom **aTableau** commands
- Adds the `beads` key for setting the number of beads on an abacus
- Adds the `colour theme` key, which gives a choice of three colour schemes
- Adds the `colours` key, which sets a cyclic list of fill colours for tableaux
- Adds the `cover` key for covering tableaux and diagrams
- Adds the `framed` key for framing abacuses
- Adds the `rotate` key for rotating **aTableau** pictures
- Adds the `row labels` key to add row labels to an abacus
- Adds the `shape` key for setting the shape of a `\RibbonTableau`
- Adds the `traditional` key for traditional abacuses, with rods and beads
- Adds error messages when an **aTableau** command is not properly contained inside a `tikzpicture` environment
- Adds a testing framework using the examples from the manual
- Fixes a bug in the `beta numbers` key for abacuses
- Makes many improvements and corrections to the manual

## Version 2.1.1 - 2025-02-14

- Fixes expansion issue with `ribbon box` and friends
- Fixes licensing issues identified by CTAN

## Version 2.1.0 - 2025-01-24

- Adds support for using **aTableau** commands as subscripts and superscripts
- Adds warnings about using older versions of LaTeX3

## Version 2.0.0 - 2025-01-22

- Rewrites package from scratch using LaTeX3
- Adds a key-value interface for the picture options
- Adds support for the different tableau and abacus conventions
- Adds stars and styles to tableaux, diagrams, and abacuses
- Allows commands to be used both in and outside `tikzpicture` environments
- Allows TikZ styles to be applied to tableau and abacus entries

## Version 1.0.0 - 2023-10-06

- Initial version
- Implements Young diagrams, tabloids, tableaux, shifted tableaux, russian tableaux, abacuses
