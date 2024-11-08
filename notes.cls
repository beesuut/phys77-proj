\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{notes}

\LoadClass{article}

\RequirePackage[utf8]{inputenc}

% Theorems
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}{Corollary}[section]
\newtheorem{definition}{Definition}[section]
\newtheorem{question}{Question}

% Sets
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\uvectheta}{\boldsymbol{\hat{{\theta}}}}
\DeclareRobustCommand{\uvec}[1]{{%
  \ifcsname uvec#1\endcsname
     \csname uvec#1\endcsname
   \else
    \hat{\mathbf{#1}}%
   \fi
}}

% Formatting
\newcommand{\tab}{\hspace*{10px}}
\newcommand{\indicates}{\(\rightarrow\) }

% Calculus
\newcommand{\deriv}[2]{\displaystyle\frac{d #1}{d #2}}
\newcommand{\pd}[2]{\displaystyle\frac{\partial #1}{\partial #2}}
\newcommand{\cv}[2]{\begin{bmatrix}#1\\#2\\\end{bmatrix}}
\newcommand{\grad}{\vec{\nabla}}

% Images
\newcommand{\image}[4]{
    \begin{figure}[H]
    \centering
    \includegraphics[width=#4]{#1}
    \caption{#3}
    \label{#2}
\end{figure}}

% Math
\RequirePackage{amsmath}
\RequirePackage{amsthm}
\RequirePackage{amsfonts}
\RequirePackage{witharrows} % Reference Arrows
\RequirePackage{siunitx} % SI Units
\RequirePackage{pgfplots} % Graphing
    \pgfplotsset{compat=1.18, width=10cm}
\RequirePackage{textcomp, gensymb}

% Packages
\RequirePackage{graphicx}
\RequirePackage{hyperref} % Hyperlinks
\RequirePackage{fancyvrb}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage} % Last Page Reference
\RequirePackage{geometry}
\RequirePackage{multicol}
\RequirePackage{setspace}
\RequirePackage{parskip} % No Indent
\RequirePackage{listings} % Code Blocks
\RequirePackage{courier}
\RequirePackage{color}
\RequirePackage{float} % Force Image Placement

% Fancy Header
\pagestyle{fancy}

% Hyperlinks
\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=red}

% Section Numbering
\numberwithin{equation}{subsection}