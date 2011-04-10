Summary:	On-screen keyboard
Summary(pl.UTF-8):	Klawiatura ekranowa
Name:		caribou
Version:	0.2.00
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/caribou/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	fcbbc21c04479f38713cff3ac877a2e0
URL:		http://live.gnome.org/Caribou
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1.11
BuildRequires:	clutter-devel >= 1.6.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-pygobject-devel >= 2.28.0
BuildRequires:	rpmbuild(macros) >= 1.592
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	GConf2-libs
Requires:	clutter >= 1.6.0
Requires:	gtk+3
Requires:	python-modules
Requires:	python-pyatspi >= 2.0.0
Requires:	python-pygobject >= 2.28.0
BuildArch:	noarch
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

%build
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
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/caribou
%{_datadir}/caribou
%{_datadir}/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%{_desktopdir}/caribou.desktop
%{py_sitescriptdir}/caribou
%{_sysconfdir}/xdg/autostart/caribou-autostart.desktop
