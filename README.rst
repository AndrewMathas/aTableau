|version|
|LPPL|
|LaTeX|

========
aTableau
========

*This version of the package is already quite powerful, but it is still
in the proof-of-concept phase. There are still bugs and some commands
are not yet documented.  Several planned features have not been
implemented. Everything is subject to change. Comments and suggestions
are welcome.*

A LaTeX package for symmetric group combinatorics, including:
    - Young diagrams
    - tabloids
    - tableaux
    - abacuses
    - KLRW diagrams


.. code-block:: latex

    \Tabloid{1379{11},249{10},6,8}
    \SkewTableau{3,2,1}{345,56,9{10}}
    \SkewTableau[french]{3,2}{345,56,9{10}}
    \RibbonTablea[ukrainian, skew={4,1^2}]{16rcrrrccrcc, 26, 34rc}
    \Abacus[rows=3, infinite]{3}{0,2,3,4,5}
    \Abacus{3}{0,2,3,4,5}


.. |version| image:: https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=version
.. |LaTeX|   image:: https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat
.. |LPPL|    image:: https://img.shields.io/github/license/note286/xduts?style=flat-square
