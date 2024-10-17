Name:		texlive-facture-belge-simple-sans-tva
Version:	67573
Release:	1
Summary:	Simple Belgian invoice without VAT
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/facture-belge-simple-sans-tva
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facture-belge-simple-sans-tva.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facture-belge-simple-sans-tva.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can be used to generate invoices for Belgian
individuals who do not have a VAT number and who wish to do
occasional work, or to carry out paid additional activities
during their free time up to 6,000 euros per calendar year
(amount indexed annually) without having to pay tax or social
security contributions (see the website Activites
complementaires). The package can also generate expense
reports. All totals are calculated automatically, in the
invoice and in the expense report. The package depends on
calctab, ifthen, hyperref, fancyhdr, multirow, eurosym, color,
and colortbl.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/facture-belge-simple-sans-tva
%doc %{_texmfdistdir}/doc/xelatex/facture-belge-simple-sans-tva

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
