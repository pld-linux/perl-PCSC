%include	/usr/lib/rpm/macros.perl
Summary:	Perl interface to the PC/SC smart card library
Summary(pl):	Perlowy interfejs do biblioteki PC/SC
Name:		perl-PCSC
Version:	1.1.3
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-perl/pcsc-perl-%{version}.tar.gz
URL:		http://ludovic.rousseau.free.fr/softwares/pcsc-perl/pcsc-perl.html
# it's dlopened, so not autodetected
Requires:	pcsc-lite-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the PC/SC smart card library.

%description -l pl
Perlowy interfejs do biblioteki PC/SC obs³uguj±cej czytniki Smart
Card.

%prep
%setup -q -n pcsc-perl-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 

%{__make} \
	DEFINE="-Wall" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%{perl_vendorarch}/PCSC.pm
%dir %{perl_vendorarch}/PCSC
%{perl_vendorarch}/PCSC/Card.pm
%dir %{perl_vendorarch}/auto/PCSC
%{perl_vendorarch}/auto/PCSC/PCSC.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PCSC/PCSC.so
%{_mandir}/man3/*.3*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/gsm.script
