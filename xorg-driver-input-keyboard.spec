Summary:	X.org keyboard driver
Summary(pl):	Sterownik klawiatury dla X.org
Name:		xorg-driver-input-keyboard
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-input-keyboard-%{version}.tar.bz2
# Source0-md5:	e560fafebb8fc53be2daa1f43a02d0fd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org keyboard driver

%description -l pl
Sterownik klawiatury dla X.org

%prep
%setup -q -n xf86-input-keyboard-%{version}

%build
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

rm $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*{.la,.a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/*/*.so
%{_mandir}/man4x/*.4x*
