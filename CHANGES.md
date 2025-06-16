![version](https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=aTableau)
![LPPL](https://img.shields.io/github/license/note286/xduts?style=flat-square)
![CTAN](https://img.shields.io/ctan/v/atableau?color=blue&link=https://ctan.org/pkg/atableau)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat)

# aTableau - Change log

### Version 2.2.0 - 2025-04-?
  - abacuses can now be specified by quotients
  - multidirectional ribbons are now supported  (still incomplete)
  - adds the `colour theme` key, which changes the colour scheme
  - adds the `colours` key, which allows a cyclic list of fill colours in tableaux
  - adds the `shape` key for `\RibbonTableau`
  - adds the `traditional` key for abacuses  (still incomplete)
  - adds the `framed` key for abacuses
  - fixes bug in `beta numbers` key for abacuses
  - many improvements and corrections to the manual

### Version 2.1.1 - 2025-02-14
  - fixes expansion issue with `ribbon box` and friends
  - fixes licensing issues identified by CTAN

### Version 2.1.0 - 2025-01-24
  - adds support for using aTableau commands as subscripts and superscripts
  - adds warnings about using older versions of LaTeX3

### Version 2.0.0 - 2025-01-22
  - completely rewritten using LaTeX3
  - key interface for the **aTableau** options
  - allow commands to be used both in and outside `tikzpicture` environments
  - a quark-based interface allows styles to be applied to tableau and abacus entries
  - support for different tableau (english, french, ukrainian, australian) and abacus (south, west, north, east) conventions
  - support diagrams, tableaux, including tabloids, skew and shifted tableaux and ribbon tableaux
  - adds stars and styles to tableaux, diagrams and abacuses

### Version 1.0.0 - 2023-10-06
  - initial version
  - basic implementation of Young diagrams, tabloids, tableaux, shifted tableaux, Ukrainian tableaux, abacuses, braids
