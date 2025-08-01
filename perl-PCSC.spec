# TODO: rename to perl-Chipcard-PCSC?
#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires running pcscd)
#
%define	pdir	Chipcard
%define	pnam	PCSC
Summary:	Perl interface to the PC/SC smart card library
Summary(pl.UTF-8):	Interfejs perlowy do biblioteki PC/SC
Name:		perl-PCSC
Version:	1.4.16
Release:	3
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	https://pcsc-perl.apdu.fr/Chipcard-PCSC-v%{version}.tar.gz
# Source0-md5:	51f77496146132ed159d319ea14e5565
URL:		https://pcsc-perl.apdu.fr/
BuildRequires:	pcsc-lite-devel >= 1.6.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
# it's dlopened, so not autodetected
Requires:	pcsc-lite-libs >= 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PCSC module implements the PCSC class, Perl interface to the PC/SC
smart card library. Objects of this class are used to communicate with
the PCSC-lite daemon (pcscd(1)). PC/SC represents an abstraction layer
to smartcard readers. It provides a communication layer with a wide
variety of smart card readers through a standardized API.

%description -l pl.UTF-8
Moduł PCSC zawiera implementację klasy PCSC, perlowego interfejsu do
biblioteki PC/SC obsługującej czytniki kart Smart. Obiekty tej klasy
służą do komunikacji z demonem PCSC (pcscd(1)). Biblioteka PC/SC
stanowi abstrakcyjną warstwę dla czytników kart Smart. Udostępnia ona,
za pośrednictwem zestandaryzowanego API, warstwę komunikacyjną dla
wielu różnych czytników kart Smart.

%prep
%setup -q -n Chipcard-PCSC-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	DEFINE="-Wall" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Chipcard/{PCSC.pod,PCSC/Card.pod}

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
%attr(755,root,root) %{perl_vendorarch}/auto/Chipcard/PCSC/PCSC.so
%{_mandir}/man3/Chipcard::PCSC*.3pm*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/gsm.script
