#
# Conditional build:
%bcond_without	encoder		# build with encoder (using may require license)
#
Summary:	SZIP - Science Data Lossless Compression library
Summary(pl.UTF-8):	SZIP - biblioteka bezstratnej kompresji danych naukowych
Name:		szip
Version:	2.1.1
Release:	1
%if %{with encoder}
License:	free for use in HDF software (decoder), free for non-commercial, scientific use only in HDF software (encoder)
%else
License:	free for use in HDF software
%endif
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	5addbf2a5b1bf928b92c47286e921f72
Patch0:		%{name}-opt.patch
URL:		https://support.hdfgroup.org/doc_resource/SZIP/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	libtool >= 1:1.4.2-9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SZIP is an implementation of the extended-Rice lossless compression
algorithm. The Consultative Committee on Space Data Systems (CCSDS)
has adopted the extended-Rice algorithm for international standards
for space applications. SZIP is reported to provide fast and effective
compression, specifically for the EOS data generated by the NASA Earth
Observatory System (EOS). It was originally developed at University of
New Mexico (UNM) and integrated with HDF4 by UNM researchers and
developers.

%description -l pl.UTF-8
SZIP to implementacja rozszerzonego algorytmu kompresji bezstratnej
Rice'a. CCSDS (Consultative Committee on Space Data Systems)
zaadoptowało rozszerzony algorytm Rice'a na potrzeby międzynarodowych
standardów aplikacji przestrzennych. SZIP daje szybką i efektywną
kompresję, szczególnie dla danych EOS generowanych przez NASA Earth
Observatory System (EOS). Pierwotnie biblioteka została stworzona w
University of New Mexico (UNM) i zintegrowana z HDF4 przez naukowców i
programistów UNM.

%package devel
Summary:	Header files for SZIP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SZIP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SZIP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SZIP.

%package static
Summary:	Static SZIP library
Summary(pl.UTF-8):	Statyczna biblioteka SZIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SZIP library.

%description static -l pl.UTF-8
Statyczna biblioteka SZIP.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_encoder:--disable-encoding}
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
%doc COPYING HISTORY.txt RELEASE.txt
%attr(755,root,root) %{_libdir}/libsz.so.2.*.*
%attr(755,root,root) %ghost %{_libdir}/libsz.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsz.so
%{_libdir}/libsz.la
%{_includedir}/ricehdf.h
%{_includedir}/szip_adpt.h
%{_includedir}/szlib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsz.a
