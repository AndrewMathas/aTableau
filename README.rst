|version|
|LaTeX|
|LPPL|

========
ATableau
========


LaTeX macros for symmetric group combinatorics: Young diagrams, tabloids, tableaux, abacuses, ...

This version of the code is already quite powerful, but it is still in the proof-of-concept phase and everything is subject to change.

.. code-block:: latex

    \Tableau{ .\bullet...., \bullet B\bullet., .\bullet.., .}
    \Tabloid{1379{11},249{10},6,8}
    \SkewTableau{3,2,1}{345,56,9{10}}
    \SkewTableau[french]{3,2}{345,56,9{10}}
    \Abacus[rows=3, infinite]{3}{0,2,3,4,5}
    \Abacus{3}{0,2,3,4,5}


.. |version| image:: https://img.shields.io/ctan/v/gitinfo-lua
.. |LPPL| image:: https://img.shields.io/github/license/note286/xduts?style=flat-square
.. |LaTeX| image:: https://img.shields.io/badge/LaTeX-008080?logo=latex&logoColor=fff&style=flat
