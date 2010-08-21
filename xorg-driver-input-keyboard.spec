Summary:	X.org keyboard input drivers
Summary(pl.UTF-8):	Sterowniki wejściowe klawiatury dla X.org
Name:		xorg-driver-input-keyboard
Version:	1.4.0
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
# Source0-md5:	fd17158ffeacecc8cc670604460cb98b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libpciaccess-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.2.99.0
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_xinput
Requires:	xorg-xserver-server >= 1.2.99.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org keyboard input drivers. They support the standard OS-provided
keyboard interface.

%description -l pl.UTF-8
Sterowniki wejściowe klawiatury dla X.org. Obsługują standardowy
interfejs klawiatury udostępniany przez system operacyjny.

%prep
%setup -q -n xf86-input-keyboard-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.4*
