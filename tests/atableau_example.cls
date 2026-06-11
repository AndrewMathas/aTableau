% ----------------------------------------------------------------------
% atableau_example.cls - Andrew Mathas (C) 2022-2025
% Modified: 21:03 Thursday, 11 June 2026
% ----------------------------------------------------------------------

% This class file is part of the testing framework for the aTableau package. It
% provides all of the bells and whistles needed to compile the examples from
% the manual as standalone files. The examples are automatically extracted from
% the manual when it is compiled using a symbolic link from atableau-examples.tex.
% A typical example file looks like:
%
%    \documentclass {atableau_example}
%    \begin {document}
%    % Example 1.1, page 3
%    \Tableau {1234,567,89{10},{11}{12}}
%    \end {document}
%
% The example number and page number are stored in the file as a comment. They
% are not printed by the corresponding tex/webp file because the example numbers
% can change change as the manual is updated. The file name is given by the
% unique label attached to the example environment. The example and page numbers
% in the example files are used by test_atableau.py when reporting on the examples.

% The python script test_atableau.py converts the LaTeX example files into webp
% images and then compares them with "good" example images to check for changes
% in the examples during development, optionally providing an image diff. In
% this way, the examples in the manual become the test suite for the aTableau
% package.

\ProvidesClass{atableau_example}
\LoadClass{standalone}

\RequirePackage{atableau}

\RequirePackage{amssymb}
\RequirePackage{MnSymbol}
\RequirePackage[svgnames]{xcolor}

\nofiles  % we do not need an aux file

% one or more of the example files need the following

\usetikzlibrary{
  decorations.pathmorphing,
  matrix,
  patterns,
}

\tikzset{
  add grid/.code = {
    % draw coordinate axes
    \draw[help lines, step=0.5,thin, LightGrey](-0.5,-1.5) grid (4,2.5);
    \draw[help lines, step=1,thin, Grey](-0.5,-1.5) grid (4,2.5);
    \foreach \pt in {0,...,3} {
      \node[below,font=\tiny] at (\pt,-1.5){$\pt$};
    }
    \foreach \pt in {-1,...,2} {
      \node[left, font=\tiny] at (-0.5,\pt){$\pt$};
    }
  }
}

