%define upstream_name    Archive-Zip
%define upstream_version 1.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Provide an interface to ZIP archive files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Archive/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	zlib-devel
BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(File::Which)
BuildArch:	noarch


%description
A Perl module that provides an interface to ZIP archive files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make CFLAGS="%{optflags}"

%check
%__make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE
%doc examples
%{_bindir}/crc32
%{perl_vendorlib}/Archive
%{_mandir}/*/*


