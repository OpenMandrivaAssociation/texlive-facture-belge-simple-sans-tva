%global tl_name facture-belge-simple-sans-tva
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Simple Belgian invoice without VAT
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/facture-belge-simple-sans-tva
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/facture-belge-simple-sans-tva.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/facture-belge-simple-sans-tva.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package can be used to generate invoices for Belgian individuals
who do not have a VAT number and who wish to do occasional work, or to
carry out paid additional activities during their free time up to 6,000
euros per calendar year (amount indexed annually) without having to pay
tax or social security contributions (see the website Activites
complementaires). The package can also generate expense reports. All
totals are calculated automatically, in the invoice and in the expense
report. The package depends on calctab, ifthen, hyperref, fancyhdr,
multirow, eurosym, color, and colortbl.

