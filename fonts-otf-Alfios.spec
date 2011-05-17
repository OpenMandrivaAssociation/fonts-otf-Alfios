%define fontname	Alfios
%define name		fonts-otf-%{fontname}
%define version		1.01
%define release		%mkrel 1

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Alfios fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		http://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
Lowercase upright Greek were designed in 1805 by Firmin Didot (1764 -
1836) and cut by Walfard and Vibert. The typeface, together with a
complete printing house, was donated in 1821 to the new Greek state by
Didot's son, Ambroise Firmin Didot (1790 - 1876). Lowercase italic
Greek were designed in 1802 by Richard Porson (1757 - 1808) and cut by
Richard Austin. They were first used by Cambridge University Press in
1810. Capitals, Latin and Cyrillic, as well as the complete bold
weights, have been designed in an attempt to create a well-balanced
font. The font covers the Windows Glyph List, Greek Extended, various
typographic extras and some Open Type features (Numerators,
Denominators, Fractions, Old Style Figures, Historical Forms,
Stylistic Alternates, Ligatures); it is available in regular, italic,
bold and bold italic.

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*
