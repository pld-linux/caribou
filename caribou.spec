#
# Conditional build:
%bcond_with	apidocs		# Valadoc documentation

Summary:	On-screen keyboard
Summary(pl.UTF-8):	Klawiatura ekranowa
Name:		caribou
Version:	0.4.21
Release:	3
License:	LGPL v2+
Group:		X11/Applications/Accessibility
Source0:	https://download.gnome.org/sources/caribou/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	16b76cd7453b99e2871e8d4da88bf976
Patch0:		%{name}-docs.patch
Patch1:		autostart-set-nodisplay.patch
Patch2:		fix-font-property-in-style.css.patch
Patch3:		Fix-compilation-error.patch
Patch4:		Fix-subkey-popmenu-not-showing-after-being-dismissed.patch
Patch5:		xadapter.vala-Remove-XkbKeyTypesMask-and-f.patch
Patch6:		stop-patching-generated-gir.patch
Patch7:		build.patch
URL:		https://wiki.gnome.org/Projects/Caribou
BuildRequires:	at-spi2-core-devel >= 2
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.6.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 0.10.7
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	libxklavier-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:2.4
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.14.0
BuildRequires:	vala-libgee >= 0.8
# -devel is just for .pc file
%{?with_apidocs:BuildRequires:	valadoc-devel >= 0.3.1}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.30.0
Requires:	clutter >= 1.6.0
Requires:	glib2 >= 1:2.30.0
Requires:	gobject-introspection >= 0.10.7
Requires:	python3-caribou = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Caribou is an on-screen keyboard suitable for people who can use a
mouse but not a hardware keyboard. This on-screen keyboard may also be
useful for touch screen or tablet users.

%description -l pl.UTF-8
Caribou jest klawiaturą ekranową odpowiednią dla ludzi, którzy nie
mogą użyć zwykłej klawiatury, a tylko mysz. Może być również pomocna
dla użytkowników ekranów dotykowych oraz tabletów.

%package libs
Summary:	Caribou virtual on-screen keyboard library
Summary(pl.UTF-8):	Biblioteka wirtualnej klawiatury na ekranie Caribou
Group:		X11/Libraries
Conflicts:	caribou < 0.4.19

%description libs
Caribou virtual on-screen keyboard library.

%description libs -l pl.UTF-8
Biblioteka wirtualnej klawiatury na ekranie Caribou.

%package devel
Summary:	Development files for Caribou
Summary(pl.UTF-8):	Pliki programistyczne dla Caribou
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+3-devel
Requires:	libgee-devel >= 0.8
Requires:	libxklavier-devel
Requires:	libxml2-devel >= 2.0
Requires:	xorg-lib-libXtst-devel

%description devel
This package provides development files for Caribou.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki programistyczne dla Caribou.

%package apidocs
Summary:	API documentation for Caribou library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Caribou
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Caribou library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Caribou.

%package -n python3-caribou
Summary:	Keyboard UI for Caribou
Summary(pl.UTF-8):	Interfejs użytkownika klawiatury dla Caribou
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python3-modules >= 1:2.4
Requires:	python3-pyatspi >= 2.2.0
Requires:	python3-pygobject3 >= 3.0.0

%description -n python3-caribou
This package contains Caribou Python GUI.

%description -n python3-caribou -l pl.UTF-8
Ten pakiet zawiera graficzny interfejs użytkownika Caribou w Pythonie.

%package -n vala-caribou
Summary:	Vala API for Caribou library
Summary(pl.UTF-8):	API języka Vala do biblioteki Caribou
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.14.0
Requires:	vala-libgee >= 0.8
BuildArch:	noarch

%description -n vala-caribou
Vala API for Caribou library.

%description -n vala-caribou -l pl.UTF-8
API języka Vala do biblioteki Caribou.

%package gtk2-module
Summary:	Caribou IM module for GTK+ 2
Summary(pl.UTF-8):	Moduł IM Caribou dla GTK+ 2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2.0.0

%description gtk2-module
This package contains Caribou IM module for GTK+ 2.

%description gtk2-module -l pl.UTF-8
Ten pakiet zawiera moduł IM Caribou dla GTK+ 2.

%package gtk3-module
Summary:	Caribou IM module for GTK+ 3
Summary(pl.UTF-8):	Moduł IM Caribou dla GTK+ 3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3 >= 3.0.0

%description gtk3-module
This package contains Caribou IM module for GTK+ 3.

%description gtk3-module -l pl.UTF-8
Ten pakiet zawiera moduł IM Caribou dla GTK+ 3.

%package antler
Summary:	Keyboard implementation for Caribou
Summary(pl.UTF-8):	Implementacja klawiatury dla Caribou
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python3-caribou = %{version}-%{release}

%description antler
This package contains Caribou keyboard implementation.

%description antler -l pl.UTF-8
Ten pakiet zawiera implementację klawiatury Caribou.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	PYTHON="%{__python3}" \
	%{?with_apidocs:--enable-docs} \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	caribougtkdocdir=%{_gtkdocdir}/caribou

%find_lang %{name}

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libcaribou-gtk-module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%postun
if [ $1 -eq 0 ] ; then
	%glib_compile_schemas
fi

%posttrans
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/caribou-preferences
%attr(755,root,root) %{_libexecdir}/caribou
%{_datadir}/caribou
%{_datadir}/dbus-1/services/org.gnome.Caribou.Daemon.service
%{_datadir}/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%{_sysconfdir}/xdg/autostart/caribou-autostart.desktop
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/caribou-gtk-module.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaribou.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaribou.so.0
%{_libdir}/girepository-1.0/Caribou-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaribou.so
%{_includedir}/libcaribou
%{_datadir}/gir-1.0/Caribou-1.0.gir
%{_pkgconfigdir}/caribou-1.0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/caribou
%{_datadir}/devhelp/references/caribou
%endif

%files -n python3-caribou
%defattr(644,root,root,755)
%{py3_sitescriptdir}/caribou

%files -n vala-caribou
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/caribou-1.0.deps
%{_datadir}/vala/vapi/caribou-1.0.vapi

%files gtk2-module
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libcaribou-gtk-module.so

%files gtk3-module
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libcaribou-gtk-module.so

%files antler
%defattr(644,root,root,755)
%{_datadir}/antler
%{_datadir}/dbus-1/services/org.gnome.Caribou.Antler.service
%attr(755,root,root) %{_libexecdir}/antler-keyboard
%{_datadir}/glib-2.0/schemas/org.gnome.antler.gschema.xml
