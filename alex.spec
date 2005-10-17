Summary:	A lexical analyser generator for Haskell
Summary(pl):	Generator analizatorów sk³adniowych dla Haskella
Name:		alex
Version:	2.0.1
Release:	1
License:	BSD-like w/o adv. clause
Group:		Development/Tools
Source0:	http://www.haskell.org/alex/dist/%{name}-%{version}-src.tar.gz
# Source0-md5:	edb62560e29c8de23913c65c52adbf19
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.haskell.org/alex/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	ghc >= 5.04
BuildRequires:	gmp-devel
BuildRequires:	jadetex
BuildRequires:	openjade
BuildRequires:	sed >= 4.0
BuildRequires:	tetex-dvips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alex is a tool for generating lexical analysers in Haskell, given a
description of the tokens to be recognised in the form of regular
expressions. It is similar to the tool lex or flex for C/C++.

%description -l pl
Alex to narzêdzie do generowania analizatorów sk³adniowych w Haskellu
na podstawie opisu tokenów do rozpoznawania w postaci wyra¿eñ
regularnych. Jest podobne do narzêdzi lex lub flex dla C/C++.

%prep
%setup -q

sed -i -e 's/alpha\*-unknown-linux/alpha*-*-linux/' configure.ac

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.sub .
%configure
%{__make} depend
%{__make}
%{__make} html -C alex/doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}

cp -a alex/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc alex/{ANNOUNCE,LICENSE,README} alex/doc/alex
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/A*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/alex.bin
%{_examplesdir}/%{name}-%{version}
