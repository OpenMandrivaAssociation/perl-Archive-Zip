%define upstream_name    Archive-Zip
%define upstream_version 1.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Provide an interface to ZIP archive files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{realname}
Source0:	http://www.cpan.org/modules/by-module/Archive/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:	zlib-devel
Buildrequires:	perl(Compress::Zlib)
BuildRequires:  perl(File::Which)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
A Perl module that provides an interface to ZIP archive files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes LICENSE
%doc examples
%{_bindir}/crc32
%{perl_vendorlib}/Archive
%{_mandir}/*/*
