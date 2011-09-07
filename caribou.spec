Summary:	On-screen keyboard
Summary(pl.UTF-8):	Klawiatura ekranowa
Name:		caribou
Version:	0.3.91
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/caribou/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	c91c7b722cccf66745dd6befeeb8aace
Patch0:		soname.patch
URL:		http://live.gnome.org/Caribou
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1.11
BuildRequires:	clutter-devel >= 1.6.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgee-devel
BuildRequires:	libxklavier-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-pygobject3-devel >= 2.90.3
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter >= 1.6.0
Requires:	gtk+2
Requires:	gtk+3
Requires:	python-modules
Requires:	python-pyatspi >= 2.0.0
Requires:	python-pygobject3 >= 2.90.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Caribou is an on-screen keyboard suitable for people who can use a
mouse but not a hardware keyboard. This on-screen keyboard may also be
useful for touch screen or tablet users.

%description -l pl.UTF-8
Caribou jest klawiaturą ekranową odpowiednią dla ludzi, którzy nie
mogą użyć zwykłej klawiatury a tylko mysz. Może być również pomocna
dla użytkowników ekranów dotykowych oraz tabletów.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas

%postun
/sbin/ldconfig
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/caribou
%attr(755,root,root) %{_bindir}/caribou-preferences
%attr(755,root,root) %{_libexecdir}/antler-keyboard
%attr(755,root,root) %{_libdir}/libcaribou.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaribou.so.0
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libcaribou-gtk-module.so
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libcaribou-gtk-module.so
%{_datadir}/antler
%{_datadir}/caribou
%{_datadir}/dbus-1/services/org.gnome.Caribou.Antler.service
%{_datadir}/glib-2.0/schemas/org.gnome.antler.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%{_desktopdir}/caribou.desktop
%{py_sitescriptdir}/caribou
%{_sysconfdir}/xdg/autostart/caribou-autostart.desktop
%{_libdir}/girepository-1.0/Caribou-1.0.typelib
