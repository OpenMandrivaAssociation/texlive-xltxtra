# revision 19809
# category Package
# catalog-ctan /macros/latex/contrib/xltxtra
# catalog-date 2010-09-19 16:45:28 +0200
# catalog-license lppl
# catalog-version 0.5e
Name:		texlive-xltxtra
Version:	0.5e
Release:	1
Summary:	"Extras" for LaTeX users of XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xltxtra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xltxtra.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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
%{_texmfdistdir}/tex/latex/xltxtra/xltxtra.sty
%doc %{_texmfdistdir}/doc/latex/xltxtra/README
%doc %{_texmfdistdir}/doc/latex/xltxtra/xltxtra.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xltxtra/xltxtra.dtx
%doc %{_texmfdistdir}/source/latex/xltxtra/xltxtra.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
