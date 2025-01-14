
A ToDo list for a aTableau
==========================

* abacus documentation and keys for customising abacuses
  * dotted rows and columns
  * ?? full frame
  * residue labels

* check the manual index


Things we could do
------------------

* rewrite ribbons and \Abacus to simultaneously parse the specifications
  and draw the picture
* rewrite the partition parsing using quarks
* we should really be using l3color and not xcolor...

* ?? beta numbers: allow partition to be specified by beta numbers in \Tableau
  and friends
* ?? checkboard={colours}: cyclic list of cell background colours...
* ?? allow polar, and other, coordinates to be used


Bugs
----

* fix keyword styling in manual

* edge not quite long enough for \Tabloid[skew={0,1,2}]{19{11}7,29{10},6}

* there are too many abacus rows when using beta numbers: \Abacus[beta numbers]{3}{6,4,3,[ball color=red]0}

* are the style settings of thick and semithick working properly for
  the abacus runners and ticks?

* entries=rows does not take into account the  "zero beads" at the start
  of the abacus

* The box width and box height keys need some TLC. Similarly, the tableau and
  abacus conventions are not playing well together. The underlying
  issues are that abacuses and tableaux use the row_d?_fp and col_d?_fp for
  potentially different things, and the conventions change these and the
  box/bead height and width willy nilly.

AM January 25
