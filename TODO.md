![version](https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=aTableau)
![LPPL](https://img.shields.io/github/license/note286/xduts?style=flat-square)
![CTAN](https://img.shields.io/ctan/v/atableau?color=blue&link=https://ctan.org/pkg/atableau)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat)


# aTableau - ToDo list

### Bugs:
 - fix warning messages when compiling manual
 - fix dotted rows and dotted columns for abacuses


### Features being implemented
  - Find a way for the path, ribbon and snob boxes to inherit colour from the ribbon style
  - Make `\__atableau_abacus:nn` peek for commas rather than using
    `\clist_map_inline:nn`. Currently braces are needed for "complex"
    style specifications in abacuses `[{...}]`. (This has already been
    done for (ribbon) tableau.)
  - check Cartan conventions

### Documentation
  - Add an example showing how to use dotted rows and columns for multitableaux

### Things we might do at some point

  - Add a `custom theme` option that sets the six aTableau colours
  - Rewrite ribbons and `\Abacus` to simultaneously parse the specifications and draw the picture
  - Rewrite the partition parsing so that it uses quarks
  - Beta numbers: allow partition to be specified by beta numbers in `\Diagram` and friends
  - Allow polar, and other, coordinates to be used as `(x,y)`-coordinates
  - Redesign the example environment to automate a testing framework
    using image diffs

AM August 2025
