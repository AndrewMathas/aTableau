|version|
|LPPL|
|LaTeX|

========
aTableau
========

A LaTeX package for symmetric group combinatorics, including:
    - Young diagrams
    - tableaux
    - tabloids
    - skew tableaux
    - shifted tableaux
    - ribbon tableaux
    - multitableaux
    - abacuses


.. code-block:: latex

    \Tableau{12345,678,9{10},{11}}
    \Diagram[australian]{4^4,2,1^3}
    \Tabloid{1379{11},249{10},6,8}
    \SkewTableau[ukrainian]{3,2,1}{345,56,9{10}}
    \SkewTableau[french]{3,2}{345,56,9{10}}
    \RibbonTablea[ukrainian, skew={4,1^2}]{16rcrrrccrcc, 26, 34rc}
    \Abacus[rows=3, abacus ends=..]{3}{0,2,3,4,5}
    \Abacus{3}{0,2,3,4,5}


.. |version| image:: https://img.shields.io/github/v/tag/AndrewMathas/aTableau?color=success&label=version
.. |LaTeX|   image:: https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat
.. |LPPL|    image:: https://img.shields.io/github/license/note286/xduts?style=flat-square
