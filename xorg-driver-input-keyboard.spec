Summary:	X.org keyboard input drivers
Summary(pl.UTF-8):	Sterowniki wejściowe klawiatury dla X.org
Name:		xorg-driver-input-keyboard
Version:	1.8.1
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
# Source0-md5:	96ccc43d389b970afbd3893875dfd678
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.4
BuildRequires:	rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.4
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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.4*
