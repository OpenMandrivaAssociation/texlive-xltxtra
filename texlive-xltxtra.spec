Name:		texlive-xltxtra
Version:	56594
Release:	1
Summary:	"Extras" for LaTeX users of XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xltxtra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-metalogo

%description
The package loads the fixltx2e package from the LaTeX
distribution, and etex.sty from the e-TeX distribution. The
package then patches the \- (discretionary hyphen command) to
use the current hyphen character (which may be different from
than the default, which is the character at the ASCII hyphen
slot), and loads the realscripts to patch the \textsuperscript
command (from the LaTeX kernel) and the \textsubscript command
(from the fixltx2e package). The package is loaded by the
fontspec package, so that it should not ordinarily be necessary
to load it explicitly. The package relies on the metalogo
package for typesetting the XeTeX and XeLaTeX logos.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xltxtra
%doc %{_texmfdistdir}/doc/xelatex/xltxtra
#- source
%doc %{_texmfdistdir}/source/xelatex/xltxtra

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
