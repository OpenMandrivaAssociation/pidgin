%define version 2.0.0
%define subv	beta7
%define release %mkrel 2.%subv.1

%define major 0
%define name pidgin
%define libname %mklibname %{name} %major

%define purple purple
%define lib_purple %mklibname %{purple} %major

%define console_app finch
%define lib_console_app %mklibname %{console_app} %major

%define build_evolution 1
%if %{mdkversion} < 1010
	%define build_evolution 0
	%define __libtoolize /bin/true
%endif

%define build_silc 0
%if %{mdkversion} >= 1020
	%define build_silc 1
%endif

%define build_dbus 1
%if %{mdkversion} < 200610
	%define build_dbus 0
%endif

%define build_meanwhile 1
%if %{mdkversion} < 200610
	%define build_meanwhile 0
%endif

%define build_mono 1
%define build_vv 0

%{?_without_evolution: %{expand: %%global build_evolution 0}}
%{?_with_evolution: %{expand: %%global build_evolution 1}}

%{?_without_silc: %{expand: %%global build_silc 0}}
%{?_with_silc: %{expand: %%global build_silc 1}}

%{?_without_dbus: %{expand: %%global build_dbus 0}}
%{?_with_dbus: %{expand: %%global build_dbus 1}}

%{?_without_meanwhile: %{expand: %%global build_meanwhile 0}}
%{?_with_meanwhile: %{expand: %%global build_meanwhile 1}}

%{?_without_mono: %{expand: %%global build_mono 0}}
%{?_with_mono: %{expand: %%global build_mono 1}}

%{?_without_vv: %{expand: %%global build_vv 0}}
%{?_with_vv: %{expand: %%global build_vv 1}}

%define perl_version %(rpm -q --qf '%%{epoch}:%%{VERSION}' perl)
%define epoch 1

Summary: 	A GTK+ based multiprotocol instant messaging client
Name: 		pidgin
Version: 	%{version}
Release: 	%{release}
Epoch:		%{epoch}
Group: 		Networking/Instant messaging
License: 	GPL
URL: 		http://www.pidgin.im/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0:	%{name}-%{version}%subv.tar.bz2
#Source1: 	%{name}-%{version}%subv.tar.bz2.asc
#Source2:	gaim-qq.theme.bz2
Patch0:		gaim-2.0.0beta2-smiley.patch
#gw: from svn, make mono plugins build again
#Patch1: gaim-18172-mono-api-change.patch
#gw these patches were copied from the Fedora package
#gw include the gnthistory plugin in the gtk UI
Patch102: gaim-2.0.0beta5-debian-02_gnthistory-in-gtk.patch
#gw get the right GStreamer audio sink from GConf
Patch103: gaim-2.0.0beta5-debian-03_gconf-gstreamer.patch
#gw fix reading resolv.conf in NetworkManager integration
Patch111: gaim-2.0.0beta5-debian-11_reread-resolvconf.patch
BuildRequires:	automake1.9 intltool
BuildRequires:	autoconf2.5
BuildRequires:	gtk+2-devel
Buildrequires:	gtkspell-devel >= 2.0.2
Buildrequires:	sqlite3-devel
Buildrequires:	libncursesw-devel
#gw not really needed as gaim has its own libgadu included
#Buildrequires:	libgadu-devel
#gw we have networkmanager only in contribs:
#Buildrequires:	libnetworkmanager-glib-devel
BuildRequires:	libxscrnsaver-devel
BuildRequires:  libgstreamer0.10-devel
BuildRequires:	perl-devel
BuildRequires:	tk tk-devel tcl tcl-devel
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	ImageMagick
BuildRequires:	libnss-devel
BuildRequires:	libnspr-devel
BuildRequires:	krb5-devel
BuildRequires:	libjack-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	gettext-devel
BuildRequires:	libexpat-devel
BuildRequires:	howl-devel
BuildRequires:	avahi-glib-devel avahi-client-devel
BuildRequires:	doxygen
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils
%if %build_meanwhile
BuildRequires:	meanwhile-devel >= 1.0.0
%else
BuildConflicts:	meanwhile-devel
%endif
%if %build_evolution
BuildRequires:	evolution-data-server-devel
%endif
%if %build_silc
BuildRequires:	silc-toolkit-devel >= 0.9.12
%else
BuildConflicts:	silc-toolkit-devel
%endif
%if %build_dbus
BuildRequires:	dbus-devel >= 0.50
%endif
%if %build_mono
BuildRequires:	mono-devel
%endif
%if %build_vv
BuildRequires:  libortp-devel >= 0.8.1
BuildRequires:	speex-devel
%endif
Obsoletes:	hackgaim <= 0.60
Provides:	hackgaim <= 0.60
Obsoletes:	gaim
Provides:	gaim
Requires:	%{purple} = %{epoch}:%{version}-%release

%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols including AIM, MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu,
ICQ, IRC, Novell Groupwise, QQ, Lotus Sametime, SILC, Simple and
Zephyr.  These protocols are implemented using a modular, easy to
use design.  To use a protocol, just add an account using the
account editor.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting, TCL scripting and C plugins.

Pidgin is not affiliated with or endorsed by America Online, Inc.,
Microsoft Corporation, Yahoo! Inc., or ICQ Inc.

%package -n	%{purple}-perl
Summary:	Purple extension, to use perl scripting
Group: 		Networking/Instant messaging
Obsoletes:	gaim-perl
Provides:	gaim-perl = %{epoch}:%{version}-%release
Requires:	%{purple} = %{epoch}:%{version}-%release

%description -n	%{purple}-perl
Purple can use perl script as plugin, this plugin enable them.

%package -n	%{purple}-tcl
Summary:	Purple extension, to use tcl scripting
Group: 		Networking/Instant messaging
Obsoletes:	gaim-tcl
Provides:	gaim-tcl = %{epoch}:%{version}-%release
Requires:	%{purple} = %{epoch}:%{version}-%release

%description -n	%{purple}-tcl
Purple can use tcl script as plugin, this plugin enable them.

%package 	gevolution
Summary:	Pidgin extension, for Evolution integration
Group:          Networking/Instant messaging
Obsoletes:	gaim-gevolution
Provides:	gaim-gevolution = %{epoch}:%{version}-%release
Requires:       %{name} = %{epoch}:%{version}-%release

%description 	gevolution
This pidgin plugin allows you to have pidgin working together with evolution.

%package -n	%{purple}-silc
Summary:	Purple extension, to use SILC (Secure Internet Live Conferencing)
Group: 		Networking/Instant messaging
Obsoletes:	gaim-silc
Provides:	gaim-silc = %{epoch}:%{version}-%release
Requires:	%{purple} = %{epoch}:%{version}-%release

%description -n %{purple}-silc
This purple plugin allows you to use SILC (Secure Internet Live Conferencing)
plugin for live video conference.

%package -n	%{libname}-devel
Summary:	Development files for pidgin
Group: 		Development/GNOME and GTK+
Requires:	%{libname} = %{epoch}:%{version}-%release
Requires:	libpurple-devel = %{epoch}:%{version}-%release
Provides:	libpidgin-devel = %{epoch}:%{version}-%release
Provides:	pidgin-devel = %{epoch}:%{version}-%release
Obsoletes:	gaim-devel

%description -n %{libname}-devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%package -n	%{lib_purple}
Summary:	libpurple library for IM clients like Pidgin and Finch
Group:		System/Libraries
Provides:	libpurple = %{epoch}:%{version}-%release 	
Provides:	purple = %{epoch}:%{version}-%release
Obsoletes:	%mklibname gaim 0
Provides:	%mklibname gaim 0 = %{epoch}:%{version}-%release

%description -n %{lib_purple}
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%package -n	%{lib_purple}-devel
Summary:	Development headers, documentation, and libraries for libpurple
Group:		Development/GNOME and GTK+
Requires:	%{lib_purple} = %{epoch}:%{version}-%release
Provides:	libpurple-devel = %{epoch}:%{version}-%release 	
Provides:	purple-devel = %{epoch}:%{version}-%release 	

%description -n %{lib_purple}-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

%package -n	%{console_app}
Summary:	A text-based user interface for Pidgin
Group:	Networking/Instant messaging
Provides:	gaim-text = %{epoch}:%{version}-%release
Requires:	libpurple = %{epoch}:%{version}-%release
Conflicts:	%mklibname gaim 0

%description -n	%{console_app}
A text-based user interface for using libpurple. This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.

%package -n	%{lib_console_app}-devel
Summary:	Headers etc. for finch stuffs
Group:	Development/C
Requires:	libpurple-devel = %{epoch}:%{version}-%release 	
Provides:	%{console_app}-devel = %{epoch}:%{version}-%release 	

%description -n	%{lib_console_app}-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.

%package -n	%{purple}-bonjour
Summary:	Bonjour plugin for Purple
Group:		Networking/Instant messaging
Obsoletes:	gaim-bonjour
Provides:	gaim-bonjour  = %{epoch}:%{version}-%release
Requires:	%{purple} = %{epoch}:%{version}-%release

%description -n %{purple}-bonjour
Bonjour plugin for Purple

%package -n	%{purple}-meanwhile
Summary:	Lotus Sametime Community Client plugin for Purple
Group:		Networking/Instant messaging
Obsoletes:	gaim-meanwhile
Provides:	gaim-meanwhile = %{epoch}:%{version}-%release
Requires:	%{purple} = %{epoch}:%{version}-%release

%description -n %{purple}-meanwhile
Lotus Sametime Community Client plugin for purple

%package -n	%{purple}-client
Summary:	Plugin and sample client to control purple clients
Group: 		Networking/Instant messaging
Requires:	%{purple} >= %{epoch}:%{version}-%{release}
Requires:	dbus-python
Obsoletes:	libgaim-remote0, gaim-client
Provides:	libgaim-remote0, gaim-client

%description -n	%{purple}-client
Applications and library to control purple clients remotely.

%package -n	%{purple}-client-devel
Summary:	Development files for gaim-client
Group:		Development/GNOME and GTK+
Obsoletes:	gaim-client-devel
Provides:	gaim-client-devel = %{epoch}:%{version}-%release
Requires:	%{purple}-client = %{epoch}:%{version}-%release

%description -n	%{purple}-client-devel
This package contains development files needed for developing or
compiling applications that need purple remote control functions.

%package -n	%{purple}-mono
Summary:        Purple extension, to use Mono plugins
Group:		Networking/Instant messaging
Obsoletes:	gaim-mono
Provides:	gaim-mono = %{epoch}:%{version}-%release
Requires:	%{purple} = %{epoch}:%{version}-%release

%description -n	%{purple}-mono
Purple can use plugins developed with Mono.

%prep
%setup -q -n %{name}-%{version}%{subv}
#cd gtk
#%patch0 -p1 -b .smiley
#cd ..
#%patch1 -p0 -b .mono
#%patch102 -p0
#%patch103 -p1
#%patch111 -p1

#aclocal-1.9
#automake-1.9
#autoconf

%build
# (Abel) 0.72-3mdk Somehow it won't connect to servers if gaim is
#                  linked against gnutls
%configure2_5x \
	--enable-gnutls=no \
	--with-perl-lib=vendor \
%if %build_dbus
	--enable-dbus \
%else
	--disable-dbus \
%endif
%if %build_mono
	--enable-mono \
%else
	--disable-mono \
%endif
%if ! %build_evolution
	--disable-gevolution \
%endif
%if %build_vv
	--enable-vv \
%else
	--disable-vv \
%endif
	--without-krb4
#gw parallel build doesn't work with the mono plugin
make

%install
rm -rf %{buildroot}
%makeinstall_std mkinstalldirs='mkdir -p'

#icons
#install -d -m 755 %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
#install -m 644 -D %{name}/pixmaps/icons/48/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png
#install -m 644 -D %{name}/pixmaps/icons/32/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
#install -m 644 -D %{name}/pixmaps/icons/16/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network" \
  --add-category="InstantMessaging" \
  --add-category="X-MandrivaLinux-Internet-InstantMessaging" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# append QQ theme entry into default theme
#bzip2 -dc %{SOURCE2} >> %{buildroot}%{_datadir}/pixmaps/pidgin/emotes/default

# remove files not bundled
rm -f %{buildroot}%{_libdir}/%{name}/*.la \
      %{buildroot}%{_libdir}/%{name}/*.a \
      %{buildroot}%{_libdir}/%{purple}-2/*.la \
      %{buildroot}%{_libdir}/%{purple}-2/*.a \
      %{buildroot}%{_libdir}/*.la
 
%find_lang %{name}

find $RPM_BUILD_ROOT%{_libdir}/purple-2 -xtype f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" | \
        grep -v /libbonjour.so | \
        grep -v /libsametime.so | \
        grep -v /mono.so | \
	grep -v /tcl.so | \
	grep -v /dbus-example.so | \
	grep -v /libsilcpurple.so | \
	grep -v /perl.so | \
        grep -v ".dll$" > %{name}-%{version}-purpleplugins

find $RPM_BUILD_ROOT%{_libdir}/pidgin -xtype f -print | \
	grep -v /gevolution.so | \
        sed "s@^$RPM_BUILD_ROOT@@g" > %{name}-%{version}-pidginplugins

find $RPM_BUILD_ROOT%{_libdir}/finch -xtype f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" > %{name}-%{version}-finchplugins

# files -f file can only take one filename :(
cat %{name}.lang >> %{name}-%{version}-purpleplugins

%post
%post_install_gconf_schemas purple

%preun
%preun_uninstall_gconf_schemas purple

%postun

%post -n %{lib_purple} -p /sbin/ldconfig
%postun -n %{lib_purple} -p /sbin/ldconfig

%if %build_dbus
%post -n %{purple}-client -p /sbin/ldconfig
%postun -n %{purple}-client -p /sbin/ldconfig
%endif

%files -f %{name}-%{version}-pidginplugins
%defattr(-,root,root)
%doc AUTHORS COPYING COPYRIGHT ChangeLog
%doc NEWS README README.MTN doc/the_penguin.txt
%{_mandir}/man1/pidgin.*
%{_mandir}/man3*/*
%_sysconfdir/gconf/schemas/%{purple}.schemas
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/icons/*
%{_datadir}/sounds/%{name}

%files -n %{libname}-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%files -f %{name}-%{version}-purpleplugins -n %{lib_purple}
%defattr(-,root,root)
%_libdir/libpurple.so.%{major}*

%files -n %{lib_purple}-devel
%defattr(-, root, root)
%doc ChangeLog.API HACKING PLUGIN_HOWTO
%dir %{_includedir}/libpurple
%{_includedir}/lib%{purple}/*.h
%{_libdir}/lib%{purple}.so
%{_libdir}/pkgconfig/%{purple}.pc
%{_datadir}/aclocal/%{purple}.m4

%files -f %{name}-%{version}-finchplugins -n %{console_app}
%defattr(-, root, root)
%doc %{_mandir}/man1/%{console_app}.*
%{_bindir}/%{console_app}
%{_libdir}/libgnt.so.*

%files -n %{lib_console_app}-devel
%defattr(-, root, root)
%dir %{_includedir}/%{console_app}
%{_includedir}/%{console_app}/*.h
%dir %{_includedir}/gnt
%{_includedir}/gnt/*.h
%{_libdir}/pkgconfig/gnt.pc
%{_libdir}/libgnt.so

%files -n %{purple}-bonjour
%defattr(-,root,root)
%{_libdir}/%{purple}-2/libbonjour.so

%files -n %{purple}-perl
%defattr(-,root,root)
%doc doc/PERL-HOWTO.dox
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/auto/Pidgin/*
%{perl_vendorarch}/auto/Purple/*
%{_libdir}/%{purple}-2/perl.so

%files -n %{purple}-tcl
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{purple}-2/tcl.so

%if %build_silc
%files -n %{purple}-silc
%defattr(-,root,root)
%doc libpurple/protocols/silc/README
%{_libdir}/%{purple}-2/libsilcpurple.so
%endif

%if %build_evolution
%files gevolution
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}/gevolution.so
%endif

%if %build_meanwhile
%files -n %{purple}-meanwhile
%defattr(-,root,root)
%{_libdir}/%{purple}-2/libsametime.so
%endif

%if %build_dbus
%files -n %{purple}-client
%defattr(-,root,root)
%doc COPYRIGHT
%{_bindir}/%{purple}-remote
%{_bindir}/%{purple}-send
%{_bindir}/%{purple}-send-async
%{_bindir}/%{purple}-client-example
%{_bindir}/%{purple}-url-handler
%{_libdir}/lib%{purple}-client.so.0*
%{_libdir}/%{purple}-2/dbus-example.so

%files -n %{purple}-client-devel
%defattr(-,root,root)
%{_libdir}/lib%{purple}-client.so
%endif

%if %build_mono
%files -n %{purple}-mono
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{purple}-2/mono.so
%{_libdir}/%{purple}-2/*.dll
%endif

%clean
rm -rf %{buildroot}
