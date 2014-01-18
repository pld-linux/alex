#
# Conditional build:
%bcond_with	bootstrap	# use foreign (non-rpm) ghc
#
Summary:	A lexical analyser generator for Haskell
Summary(pl.UTF-8):	Generator analizatorów składniowych dla Haskella
Name:		alex
Version:	3.1.3
Release:	2
License:	BSD-like w/o adv. clause
Group:		Development/Tools
#Source0Download: http://hackage.haskell.org/package/alex
Source0:	http://hackage.haskell.org/package/alex-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	525e570cb0e84fd856f9c53605ec9e98
URL:		http://www.haskell.org/alex/
BuildRequires:	autoconf >= 2.50
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
%{!?with_bootstrap:BuildRequires:	ghc >= 6.6}
BuildRequires:	ghc-QuickCheck >= 2
BuildRequires:	gmp-devel
%{!?with_bootstrap:BuildRequires:	happy}
BuildRequires:	libxslt-progs
#For generating documentation in PDF: fop or xmltex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alex is a tool for generating lexical analysers in Haskell, given a
description of the tokens to be recognised in the form of regular
expressions. It is similar to the tool lex or flex for C/C++.

%description -l pl.UTF-8
Alex to narzędzie do generowania analizatorów składniowych w Haskellu
na podstawie opisu tokenów do rozpoznawania w postaci wyrażeń
regularnych. Jest podobne do narzędzi lex lub flex dla C/C++.

%prep
%setup -q

%build
%{?with_bootstrap:PATH=$PATH:/usr/local/bin}
runhaskell Setup.lhs configure --prefix=%{_prefix}
runhaskell Setup.lhs build

cd doc
%{__autoconf}
%configure
%{__make} html
cd ..

%install
rm -rf $RPM_BUILD_ROOT
%{?with_bootstrap:PATH=$PATH:/usr/local/bin}
runhaskell Setup.lhs copy --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# work around automatic haddock docs installation
%{__rm} -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README TODO doc/alex
%attr(755,root,root) %{_bindir}/alex
%{_datadir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}
