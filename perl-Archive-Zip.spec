%define upstream_name    Archive-Zip
%bcond_with tests

Summary:	Provide an interface to ZIP archive files
Name:		perl-%{upstream_name}
Version:	1.68
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Archive::Zip
Source0:	http://www.cpan.org/modules/by-module/Archive/%{upstream_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(File::Which)
BuildRequires:	pkgconfig(zlib)
# For tests only
BuildRequires:	perl(SUPER)
BuildRequires:	perl(Test::MockModule)

%description
A Perl module that provides an interface to ZIP archive files.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make_build CFLAGS="%{optflags}"

%if %{with tests}
%check
# Disabled because of Test-MockModule dependency
make test
%endif

%install
%make_install

%files
%doc  Changes 
%doc examples
%{_bindir}/crc32
%{perl_vendorlib}/Archive
%{_mandir}/man3/*
