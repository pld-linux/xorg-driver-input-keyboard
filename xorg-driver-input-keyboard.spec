Summary:	X.org keyboard input drivers
Summary(pl):	Sterowniki wejściowe klawiatury dla X.org
Name:		xorg-driver-input-keyboard
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-input-keyboard-%{version}.tar.bz2
# Source0-md5:	e560fafebb8fc53be2daa1f43a02d0fd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org keyboard input drivers. They support the standard OS-provided
keyboard interface.

%description -l pl
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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/input/kbd_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/input/keyboard_drv.so
%{_mandir}/man4/kbd.4x*
%{_mandir}/man4/keyboard.4x*
