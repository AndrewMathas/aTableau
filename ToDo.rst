
A ToDo list for a aTableau
--------------------------

* abacus documentation
* allow polar coordinates to be used (perhaps this is automatic?)
* allow a label on diagrams. For example, this could be used for the
  * initial residue 
      0
       \
         0 1 2 3 0 1 2 3
         3 0 1 2 3
         2 3 0 1

* can we get rid of the need for double bracing by writing a custom csv interpreter?
* add options:
   * beta? = allow abacus/partition to be specified by beta numbers
   * rows       = number of rows in abacus
   * dots       = dotted abacus runners
   * checkboard={colours}? = cyclic list of cell background colours...
   * an alignment option for the tableau entries
   * cartan=... for residues A1-e, A2-e, C1-2, D2-2, ...
   * residue=e : allow residues of type C, ...

* fix separators and proper spacing for multidiagrams and tableaux.
* multidiagram version of show=residue|content|hooks|initial|final|...
* add features for customising abacuses
* decide whether to add KLRW diagrams
* ?allow dots on the diagram boundary: row dots={...}, column dots={...}
* ?use shortminus for negative entries:
  \usepackage{amsfonts} %% <- also included by amssymb
  \DeclareMathSymbol{\shortminus}{\mathbin}{AMSa}{"39}

AM October 2024
