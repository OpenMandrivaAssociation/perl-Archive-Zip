%define realname	Archive-Zip
%define name		perl-%realname
%define version		1.18
%define release		%mkrel 1

Summary:	Provide an interface to ZIP archive files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NE/NEDKONZ/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot/
Buildrequires:	perl-devel zlib-devel perl-Compress-Zlib
BuildRequires:  perl(File::Which)
BuildArch:	noarch

%description
A Perl module that provides an interface to ZIP archive files.

%prep
%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%{__make} test

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO Changes
%doc examples
%{_bindir}/crc32
%{perl_vendorlib}/Archive/*
%{_mandir}/*/*

