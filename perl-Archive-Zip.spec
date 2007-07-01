%define module      Archive-Zip
%define name		perl-%{module}
%define version		1.20
%define release		%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Provide an interface to ZIP archive files
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{realname}
Source:		http://www.cpan.org/modules/by-module/Archive/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
Buildrequires:	zlib-devel
Buildrequires:	perl(Compress::Zlib)
BuildRequires:  perl(File::Which)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A Perl module that provides an interface to ZIP archive files.

%prep
%setup -q -n %{module}-%{version}

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

