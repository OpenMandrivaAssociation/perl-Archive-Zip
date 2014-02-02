%define upstream_name    Archive-Zip
%define upstream_version 1.34

Summary:	Provide an interface to ZIP archive files
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Archive/Archive-Zip-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(File::Which)
BuildRequires:	pkgconfig(zlib)

%description
A Perl module that provides an interface to ZIP archive files.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE
%doc examples
%{_bindir}/crc32
%{perl_vendorlib}/Archive
%{_mandir}/man3/*


