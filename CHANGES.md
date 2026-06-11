![version](https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=aTableau&v=2)
![LPPL](https://img.shields.io/badge/license-LPPL%201.3c-orange)
[![CTAN](https://img.shields.io/ctan/v/atableau?color=blue)](https://ctan.org/pkg/atableau)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff)

# **aTableau** - Change log

### Version 2.2.2 - 2026-??-??

- allows the package to be used even if the `atableau.ini` file is not found
- adds `entries=ladders` for ladder numbers in diagrams
- fixes a bug with the `beads` key, so that empty runners now work as advertised when abacuses are specified by their quotients

### Version 2.2.1 - 2026-06-02

- allows arbitrary TikZ coordinates to be used to position **aTableau** pictures inside `tikzpicture` environments
- allows `colour theme` to define a custom colour theme
- allows `cover` key to now be used with multishapes
- allows `entries=last` to be used with skew shapes
- adds `entries=columns` and `entries=rows`
- adds image diffs to the testing framework
- reads metadata directly from the `atableau.ini` file
- updates tableaux naming conventions

### Version 2.2.0 - 2025-10-10

- allows _generalised ribbon tableaux_ with `c`, `C`, `r` and `R` specifications
- allows _complex styles_ in abacuses and tableaux to be entered as `[...]`, instead of `[{...}]`
- allows abacuses to be specified by _quotients_
- adds optional _overlay specifications_ for use with **beamer**
- adds the `\NewATableauCommand` command for creating custom **aTableau** commands
- adds the `beads` key for setting the number of beads on an abacus
- adds the `colour theme` key, which gives a choice of three colour schemes
- adds the `colours` key, which sets a cyclic list of fill colours for tableaux
- adds the `cover` key for covering tableaux and diagrams
- adds the `framed` key for framing abacuses
- adds the `rotate` key for rotating **aTableau** pictures
- adds the `row labels` key to add row labels to an abacus
- adds the `shape` key for setting the shape of a `\RibbonTableau`
- adds the `traditional` key for traditional abacuses, with rods and beads
- adds error messages when an **aTableau** command is not properly contained inside a `tikzpicture` environment
- adds a testing framework using the examples from the manual
- fixes a bug in the `beta numbers` key for abacuses
- makes many improvements and corrections to the manual


### Version 2.1.1 - 2025-02-14

- fixes expansion issue with `ribbon box` and friends
- fixes licensing issues identified by CTAN

### Version 2.1.0 - 2025-01-24

- adds support for using **aTableau** commands as subscripts and superscripts
- adds warnings about using older versions of LaTeX3

### Version 2.0.0 - 2025-01-22

- rewrites package from scratch using  LaTeX3
- adds a key-value interface for the picture options
- adds support for the different tableau and abacus conventions
- adds stars and styles to tableaux, diagrams, and abacuses
- allows commands to be used both in and outside `tikzpicture` environments
- allows TikZ styles to be applied to tableau and abacus entries

### Version 1.0.0 - 2023-10-06

- initial version
- implements Young diagrams, tabloids, tableaux, shifted tableaux, russian tableaux, abacuses
