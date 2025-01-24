![version](https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=version)
![LPPL](https://img.shields.io/github/license/note286/xduts?style=flat-square)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat)

# aTableau

A LaTeX package for symmetric group combinatorics, with commands for:

  - Young diagrams
  - tableaux
  - tabloids
  - skew tableaux
  - shifted tableaux
  - ribbon tableaux
  - multitableaux
  - abacuses

``` latex
\Tableau{12345,678,9{10},{11}}
\Diagram[french]{4^4,2,1^3}
\Tabloid{1379{11},249{10},6,8}
\SkewTableau[ukrainian]{3,2,1}{345,56,9{10}}
\SkewDiagram[skew border style={dashed,fill=red!10},skew border]{1^2}{2^3}
\ShiftedTableau[skew boxes]{1*23,4*5}
\ShiftedDiagram[skew border]{3,2}
\RibbonTableau[ukrainian, skew={4,1^2}]{16rcrrrccrcc, 26, 34rc}
\Multidiagram[australian]{3,2^2|2,1,1|1}
\Multitableau[box font=\tiny]{123,45,67|89,{10},{11}|{12}{13}{14}}
\Abacus[rows=3, abacus ends=..]{3}{0,2,3,4,5}
\Abacus{3}{0,2,3,4,5}
```

### Dependencies
[LaTeX3](https://www.latex-project.org/latex3/) and [TikZ](https://tikz.net/)

## Author
Andrew Mathas 

## Licence
LPPL Version 1.3c  2008-05-04

## Repository
[github.com/AndrewMathas/aTableau/](github.com/AndrewMathas/aTableau/)

