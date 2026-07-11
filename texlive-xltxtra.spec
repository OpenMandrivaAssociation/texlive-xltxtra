%global tl_name xltxtra
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Extras for LaTeX users of XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/xltxtra
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(metalogo)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package was previously used to provide a number of features that
were useful for typesetting documents with XeLaTeX. Many of those
features have now been incorporated into the fontspec package and other
packages, but the package persists for backwards compatibility.
Nowadays, loading xltxtra will: load the fontspec, metalogo, and
realscripts packages; redefine \showhyphens so it works correctly; and
define two extra commands: \vfrac and \namedglyph.

