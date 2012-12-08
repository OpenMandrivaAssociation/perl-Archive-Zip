%define upstream_name    Archive-Zip
%define upstream_version 1.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Provide an interface to ZIP archive files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{realname}
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.300.0-4mdv2012.0
+ Revision: 765055
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.300.0-3
+ Revision: 763479
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.300.0-2
+ Revision: 667028
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.300.0-1mdv2010.1
+ Revision: 402978
- rebuild using %%perl_convert_version

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdv2010.0
+ Revision: 391180
- update to new version 1.30

* Tue Jun 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2010.0
+ Revision: 390832
- update to new version 1.29

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.28-1mdv2010.0
+ Revision: 386994
- update to new version 1.28

* Tue Oct 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2009.1
+ Revision: 293549
- update to new version 1.26

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2009.1
+ Revision: 292026
- update to new version 1.25

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.0
+ Revision: 277941
- update to new version 1.24

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.23-2mdv2009.0
+ Revision: 223502
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2008.1
+ Revision: 107200
- update to new version 1.23
- update to new version 1.23

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2008.1
+ Revision: 105300
- update to new version 1.22

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2008.0
+ Revision: 46770
- new version

  + Olivier Thauvin <nanardon@mandriva.org>
    - 1.18


* Tue Jul 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.16-1mdk
- 1.16

* Thu Jun 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.15-1mdk
- 1.15

* Thu Jun 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.14-2mdk
- Rebuild

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.14-1mdk
- 1.14

* Mon Oct 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.13-1mdk
- 1.13
- Add examples

* Fri Jul 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.12-1mdk
- New release 1.12
- Remove MANIFEST

* Mon May 10 2004 Michael Scherer <misc@mandrake.org> 1.10-1mdk
- New release 1.10
- remove perl hardcoded requires

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 1.06-1mdk
- 1.06.

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 1.05-5mdk
- mv rm buildroot from %%prep to %%install
- macroize
- %%makeinstall_std

* Wed Jul 16 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.05-4mdk
- fix buildrequires (Michael Scherer)

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.05-3mdk
- rebuild for new auto{prov,req}

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.05-2mdk
- buildrequires

* Fri Jan 17 2003 François Pons <fpons@mandrakesoft.com> 1.05-1mdk
- 1.05.

* Fri Jul 19 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.01-1mdk
- 1.01

* Wed Jul 10 2002 Pixel <pixel@mandrakesoft.com> 0.11-2mdk
- rebuild for perl 5.8.0

* Thu Aug 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.11-1mdk
- updated to 0.11

* Wed Mar 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.10-1mdk
- added in contribs by Stefan van der Eijk <s.vandereijk@chello.nl> :
	- new in contrib

