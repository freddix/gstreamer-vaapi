Summary:	VA-API acceleration for GStreamer
Name:		gstreamer-vaapi
Version:	0.5.10
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.freedesktop.org/software/vaapi/releases/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.bz2
# Source0-md5:	3bd90b696b644be943450ba0c1497193
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gstreamer-plugins-bad-devel >= 1.2.0
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-base
Requires:	libva-driver-intel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of GStreamer plugins and helper libraries that allow
hardware accelerated video decoding through VA-API.

%package libs
Summary:	GStreamer VA-API libraries
Group:		Libraries

%description libs
GStreamer VA-API libraries.

%package devel
Summary:	Header files for GStreamer VA-API libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for GStreamer VA-API
libraries.

%prep
%setup -qn gstreamer-vaapi-%{version}

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-gstreamer-api=1.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstvaapi.so
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstvaapi_parse.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgstcodecparsers_vpx.so.0
%attr(755,root,root) %ghost %{_libdir}/libgstvaapi*-1.4.so.?
%attr(755,root,root) %{_libdir}/libgstcodecparsers_vpx.so.*.*.*
%attr(755,root,root) %{_libdir}/libgstvaapi*-1.4.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstcodecparsers_vpx.so
%attr(755,root,root) %{_libdir}/libgstvaapi*-1.4.so
%{_includedir}/gstreamer-1.0/gst/vaapi
%{_pkgconfigdir}/*-1.0.pc

