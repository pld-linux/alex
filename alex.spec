Summary:	A lexical analyser generator for Haskell
Summary(pl):	Generator analizatorów sk³adniowych dla Haskella
Name:		alex
Version:	2.0
Release:	1
License:	BSD-like w/o adv. clause
Group:		Development/Tools
Source0:	http://www.haskell.org/alex/dist/%{name}-%{version}-src.tar.bz2
# Source0-md5:	14ff6abf21d81763b15afe151add9091
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-debian.patch
URL:		http://www.haskell.org/alex/
BuildRequires:	ghc >= 5.04
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
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}
%{__make} ps -C alex/doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a alex/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc alex/{ANNOUNCE,LICENSE,README} alex/doc/alex.{ps,dvi}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/A*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/alex.bin
%{_examplesdir}/%{name}-%{version}
