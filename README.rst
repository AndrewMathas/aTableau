.. raw:: html

    <style> .red {color:red} </style>

|version|
|LaTeX|
|ctan|
|LPPL|

========
ATableau
========

      *This version of the code is already quite powerful, but it is
      still in the proof-of-concept phase. There are still many bugs,
      planned features that are not yet implemented, and everything
      is subject to change.*

LaTeX macros for symmetric group combinatorics: Young diagrams, tabloids, tableaux, abacuses, ...


.. code-block:: latex

    \Tableau{ .\bullet...., \bullet B\bullet., .\bullet.., .}
    \Tabloid{1379{11},249{10},6,8}
    \SkewTableau{3,2,1}{345,56,9{10}}
    \SkewTableau[french]{3,2}{345,56,9{10}}
    \RibbonTablea[ukraine, skew=4,1^2]{16rcrrrccrcc, 26, 34rc}
    \Abacus[rows=3, infinite]{3}{0,2,3,4,5}
    \Abacus{3}{0,2,3,4,5}


.. |version| image:: https://img.shields.io/github/v/tag/webquiz/release?color=success&label=version
.. |LaTeX| image:: https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat
.. |ctan| image:: https://img.shields.io/ctan/l/webquiz
.. |LPPL| image:: https://img.shields.io/github/license/note286/xduts?style=flat-square
