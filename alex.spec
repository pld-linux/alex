Summary:	A lexical analyser generator for Haskell
Name:		alex
Version:	2.0
Release:	0.1
License:	BSD-like w/o adv. clause
Group:		Development/Tools
Source0:	http://www.haskell.org/alex/dist/%{name}-%{version}-src.tar.bz2
# Source0-md5:	14ff6abf21d81763b15afe151add9091
URL:		http://www.haskell.org/alex/
BuildRequires:	ghc >= 5.04
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alex is a tool for generating lexical analysers in Haskell,
given a description of the tokens to be recognised in the form
of regular expressions.
It is similar to the tool lex or flex for C/C++.

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%{__gettextize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
