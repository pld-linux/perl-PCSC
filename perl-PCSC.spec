#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires running pcscd)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Perl interface to the PC/SC smart card library
Summary(pl):	Interfejs perlowy do biblioteki PC/SC
Name:		perl-PCSC
Version:	1.3.1
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-perl/pcsc-perl-%{version}.tar.gz
# Source0-md5:	4c1869b5b726f7ab5b1bda88b390c821
URL:		http://ludovic.rousseau.free.fr/softwares/pcsc-perl/
BuildRequires:	pcsc-lite-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
# it's dlopened, so not autodetected
Requires:	pcsc-lite-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PCSC module implements the PCSC class, Perl interface to the PC/SC
smart card library. Objects of this class are used to communicate with
the PCSC-lite daemon (pcscd(1)). PC/SC represents an abstraction layer
to smartcard readers. It provides a communication layer with a wide
variety of smart card readers through a standardized API.

%description -l pl
Modu³ PCSC zawiera implementacjê klasy PCSC, perlowego interfejsu do
biblioteki PC/SC obs³uguj±cej czytniki kart Smart. Obiekty tej klasy
s³u¿± do komunikacji z demonem PCSC (pcscd(1)). Biblioteka PC/SC
stanowi abstrakcyjn± warstwê dla czytników kart Smart. Udostêpnia ona,
za po¶rednictwem zestandaryzowanego API, warstwê komunikacyjn± dla
wielu ró¿nych czytników kart Smart.

%prep
%setup -q -n pcsc-perl-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	DEFINE="-Wall" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
%dir %{perl_vendorarch}/Chipcard
%{perl_vendorarch}/Chipcard/PCSC.pm
%dir %{perl_vendorarch}/Chipcard/PCSC
%{perl_vendorarch}/Chipcard/PCSC/Card.pm
%dir %{perl_vendorarch}/auto/Chipcard
%dir %{perl_vendorarch}/auto/Chipcard/PCSC
%{perl_vendorarch}/auto/Chipcard/PCSC/PCSC.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Chipcard/PCSC/PCSC.so
%{_mandir}/man3/*.3*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/gsm.script
