![version](https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=aTableau)
![LPPL](https://img.shields.io/github/license/note286/xduts?style=flat-square)
![CTAN](https://img.shields.io/ctan/v/atableau?color=blue&link=https://ctan.org/pkg/atableau)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat)

# **aTableau** - Change log

### Version 2.2.0 - 2025-?
  - allows *generalised ribbon tableaux* with `c`, `C`, `r` and `R` specifications
  - allows *complex styles* in abacuses and tableaux to be entered as `[...]`, instead of `[{...}]`
  - adds optional *overlay specifications* for use with **beamer**
  - allows abacuses to be specified by *quotients*
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
  - adds error messages whenever an **aTableau** command is not properly contained inside a `tikzpicture` environment
  - fixes bug in the `beta numbers` key for abacuses
  - many improvements and corrections to the manual

### Version 2.1.1 - 2025-02-14
  - fixes expansion issue with `ribbon box` and friends
  - fixes licensing issues identified by CTAN

### Version 2.1.0 - 2025-01-24
  - adds support for using **aTableau** commands as subscripts and superscripts
  - adds warnings about using older versions of LaTeX3

### Version 2.0.0 - 2025-01-22
  - package completely rewritten using LaTeX3
  - key-value interface added for the **aTableau** options
  - allowed commands to be used both in and outside `tikzpicture` environments
  - a quark-based interface allows styles to be applied to tableau and abacus entries
  - support for different tableau (english, french, ukrainian, australian) and abacus (south, west, north, east) conventions
  - support for diagrams, tableaux, including tabloids, skew and shifted tableaux and ribbon tableaux
  - adds stars and styles to tableaux, diagrams, and abacuses

### Version 1.0.0 - 2023-10-06
  - initial version
  - basic implementation of Young diagrams, tabloids, tableaux, shifted tableaux, Ukrainian tableaux, abacuses
