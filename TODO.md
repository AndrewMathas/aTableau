![version](https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=aTableau)
![LPPL](https://img.shields.io/github/license/note286/xduts?style=flat-square)
![CTAN](https://img.shields.io/ctan/v/atableau?color=blue&link=https://ctan.org/pkg/atableau)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat)


# aTableau - ToDo list

### Bugs:

  - Check coordinate placement of abacuses. It is now slightly off because of the change to the height of the abacus bar
  - Fix abacus ends to work properly with traditional and non-traditional abacuses

### Features being implemented
  - Allow R and C in ribbon tableau specifications ...still needs enhancement for ribbon border...
  - Allow abacuses similar to those in suanpan-l3  ...almost done, still need to finalise the scale, borders, and the runner decorations ...

### Documentation
  - add an example showing how to use dotted rows and columns for multitableaux

### Things we might do at some point

  - Add a `custom theme` option that sets the six aTableau colours
  - Rewrite ribbons and `\Abacus` to simultaneously parse the specifications and draw the picture
  - Rewrite the partition parsing so that it uses quarks
  - Beta numbers: allow partition to be specified by beta numbers in \Diagram and friends
  - Allow polar, and other, coordinates to be used as `(x,y)`-coordinates

AM April 2025
