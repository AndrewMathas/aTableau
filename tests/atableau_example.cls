% ----------------------------------------------------------------------
% atableau_example.cls - Andrew Mathas (C) 2022-2025
% Modified: 21:07 Sunday, 12 October 2025
% ----------------------------------------------------------------------

% This class file is part of the testing framework for the aTableau package. It
% provides all of the bells and whistles needed to compile the examples from
% the manual as standalone files. A typical example file is something like
%
%    \documentclass {atableau_example}
%    \begin {document}
%    %Example 1.1
%    \Tableau {1234,567,89{10},{11}{12}}
%    \end {document}
%
% The example number is stored in the file as a comment, but is not
% part of the corresponing pdf/webp file because the example numbers
% will change whenever a new example is added earlier in the same
% section of the manual. The file name is given by the unique label
% attached to the example.

% The python script test_atableau.py can be used to convert these LaTeX
% files into webp images, making it possible to check for changes in the
% examples during development.

\ProvidesClass{atableau_example}
\LoadClass{standalone}

\RequirePackage{atableau}

\RequirePackage{amssymb}
\RequirePackage{MnSymbol}
\RequirePackage[svgnames]{xcolor}

\nofiles  % we do not need an aux file

% some of the example files need some of the following

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

