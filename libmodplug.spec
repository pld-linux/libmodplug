Summary:	The ModPlug mod file playing library
Summary(pl):	ModPlug - biblioteka do odtwarzania plików mod
Name:		libmodplug
Version:	0.8
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://dl.sourceforge.net/modplug-xmms/%{name}-%{version}.tar.gz
# Source0-md5:	cea399626e2a074e2a77c8cd98387a48
URL:		http://modplug-xmms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ModPlug is the mod file playing library. It can play 22 different mod
formats, including: MOD, S3M, XM, IT, 669, AMF (both of them), AMS,
DBM, DMF, DSM, FAR, MDL, MED, MTM, OKT, PTM, STM, ULT, UMX, MT2, PSM.
Sound quality is slightly better than Mikmod and vastly superior over
Winamp.

%description -l pl
Modplug to biblioteka do odtwarzania plików mod. Potrafi odtwarzaæ 22
ró¿ne formaty mod, w tym: MOD, S3M, XM, IT, 669, AMF (obie wersje),
AMS, DBM, DMF, DSM, FAR, MDL, MED, MTM, OKT, PTM, STM, ULT, UMX, MT2,
PSM. Jako¶æ d¼wiêku jest nieco lepsza ni¿ w przypadku Mikmoda i
zdecydowanie przewy¿sza Winampa.

%package devel
Summary:	Header files for libmodplug library
Summary(pl):	Pliki nag³ówkowe biblioteki libmodplug
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libmodplug library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libmodplug.

%package static
Summary:	Static libmodplug library
Summary(pl):	Statyczna biblioteka libmodplug
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmodplug library.

%description static -l pl
Statyczna biblioteka libmodplug.

%prep
%setup -q

%build
# supplied libtool doesn't support C++ libraries
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libmodplug
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
