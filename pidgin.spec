%define version 2.0.0
%define subv	beta7
%define release %mkrel 2.%subv.1

%define major 0
%define libname %mklibname purple %major

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
Source1: 	%{name}-%{version}%subv.tar.bz2.asc
Source2:	gaim-qq.theme.bz2
Patch0:		gaim-2.0.0beta2-smiley.patch
#gw: from svn, make mono plugins build again
Patch1: gaim-18172-mono-api-change.patch
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
Requires:	%{libname} >= %{epoch}:%{version}-%release

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

%package	perl
Summary:	Pidgin extension, to use perl scripting
Group: 		Networking/Instant messaging
Requires:	%{name} = %{epoch}:%{version}-%release

%description	perl
Pidgin can use perl script as plugin, this plugin enable them.

%package	tcl
Summary:	Pidgin extension, to use tcl scripting
Group: 		Networking/Instant messaging
Requires:	%{name} = %{epoch}:%{version}-%release

%description	tcl
Pidgin can use tcl script as plugin, this plugin enable them.

%package	gevolution
Summary:	Pidgin extension, for Evolution integration
Group:          Networking/Instant messaging
Requires:       %{name} = %{epoch}:%{version}-%release

%description	gevolution
This gaim plugin allows you to have gaim working together with evolution.

%package	silc
Summary:	Pidgin extension, to use SILC (Secure Internet Live Conferencing)
Group: 		Networking/Instant messaging
Requires:	%{name} = %{epoch}:%{version}-%release

%description silc
This gaim plugin allows you to use SILC (Secure Internet Live Conferencing)
plugin for live video conference.

%package -n %libname
Summary:	Shared libs for %name
Group: 		System/Libraries

%description -n %libname
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%package -n	%libname-devel
Summary:	Development files for gaim
Group: 		Development/GNOME and GTK+
Requires:	%{libname} = %{epoch}:%{version}-%release
Provides:	libgaim-devel = %{epoch}:%{version}-%release
Provides:	gaim-devel = %{epoch}:%{version}-%release
Obsoletes:	gaim-devel

%description -n %libname-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.

%package	bonjour
Summary:	Bonjour plugin for Pidgin
Group:		Networking/Instant messaging
Requires:	%{name} = %{epoch}:%{version}-%release

%description bonjour
Bonjour plugin for Pidgin

%package	meanwhile
Summary:	Lotus Sametime Community Client plugin for Pidgin
Group:		Networking/Instant messaging
Requires:	%{name} = %{epoch}:%{version}-%release

%description meanwhile
Lotus Sametime Community Client plugin for Pidgin

%package	client
Summary:	Plugin and sample client to control gaim
Group: 		Networking/Instant messaging
Requires:	%{name} >= %{epoch}:%{version}-%{release}
Requires:	dbus-python
Obsoletes:	libgaim-remote0
Provides:	libgaim-remote0

%description	client
Applications and library to control GAIM remotely.

%package	client-devel
Summary:	Development files for gaim-client
Group:		Development/GNOME and GTK+
Requires:	%{name}-client = %{epoch}:%{version}-%release

%description	client-devel
This package contains development files needed for developing or
compiling applications that need gaim remote control functions.

%package mono
Summary:        Pidgin extension, to use Mono plugins
Group:		Networking/Instant messaging
Requires:	%{name} = %{epoch}:%{version}-%release

%description	mono
Pidgin can use plugins developed with Mono.


%prep
%setup -q -n %{name}-%{version}%{subv}
cd gtk
%patch0 -p1 -b .smiley
cd ..
%patch1 -p0 -b .mono
%patch102 -p0
%patch103 -p1
%patch111 -p1

aclocal-1.9
automake-1.9
autoconf

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
install -d -m 755 %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
install -m 644 -D       gtk/pixmaps/gaim.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 gtk/pixmaps/gaim.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 gtk/pixmaps/gaim.png %{buildroot}%{_miconsdir}/%{name}.png

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network" \
  --add-category="InstantMessaging" \
  --add-category="X-MandrivaLinux-Internet-InstantMessaging" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# append QQ theme entry into default theme
bzip2 -dc %{SOURCE2} >> %{buildroot}%{_datadir}/pixmaps/gaim/smileys/default/theme

# remove files not bundled
rm -f %{buildroot}%{_libdir}/%{name}/*.la \
      %{buildroot}%{_libdir}/%{name}/*.a


%find_lang %{name}

%post
%post_install_gconf_schemas gaim

%preun
%preun_uninstall_gconf_schemas gaim

%postun

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%if %build_dbus
%post client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc doc/FAQ doc/*.txt
%doc AUTHORS ChangeLog COPYING NEWS README 
%_sysconfdir/gconf/schemas/gaim.schemas
#gw TODO: split this to a separate package
%{_bindir}/gaim-text
%{_bindir}/gaim
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/sounds/%{name}
%dir %{_libdir}/%{name}/ 
%dir %_libdir/%name/private/
%_libdir/%name/autoaccept.so
%_libdir/%name/autoreply.so
%_libdir/%name/buddynote.so
%_libdir/%name/cap.so
%_libdir/%name/convcolors.so
%_libdir/%name/extplacement.so
%_libdir/%name/gaimrc.so
%_libdir/%name/gestures.so
%_libdir/%name/gntgf.so
%_libdir/%name/gnthistory.so
%_libdir/%name/gntlastlog.so
%_libdir/%name/history.so
%_libdir/%name/iconaway.so
%_libdir/%name/idle.so
%_libdir/%name/libaim.so
%_libdir/%name/libbonjour.so
%_libdir/%name/libgg.so
%_libdir/%name/libicq.so
%_libdir/%name/libirc.so
%_libdir/%name/libjabber.so
%_libdir/%name/libmsn.so
%_libdir/%name/libnovell.so
%_libdir/%name/liboscar.so*
%_libdir/%name/libqq.so
%_libdir/%name/libsimple.so
%_libdir/%name/libyahoo.so
%_libdir/%name/libzephyr.so
%_libdir/%name/log_reader.so
%_libdir/%name/markerline.so
%_libdir/%name/musicmessaging.so
%_libdir/%name/newline.so
%_libdir/%name/notify.so
%_libdir/%name/offlinemsg.so
%_libdir/%name/psychic.so
%_libdir/%name/relnot.so
%_libdir/%name/s.so
%_libdir/%name/spellchk.so
%_libdir/%name/ssl-gnutls.so
%_libdir/%name/ssl-nss.so
%_libdir/%name/ssl.so
%_libdir/%name/statenotify.so
%_libdir/%name/ticker.so
%_libdir/%name/timestamp.so
%_libdir/%name/timestamp_format.so
%_libdir/%name/xmppconsole.so
%{_mandir}/*/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%files -n %libname
%defattr(-,root,root)
%_libdir/libgnt.so.%{major}*
%_libdir/libgaim.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%doc PROGRAMMING_NOTES HACKING doc/[[:lower:]]*.dox
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/gaim.m4
%{_includedir}/gaim
%{_includedir}/gnt/
%_libdir/libgaim.so
%_libdir/libgaim.la
%_libdir/libgnt.so
%_libdir/libgnt.la


%files perl
%defattr(-,root,root)
%doc doc/PERL-HOWTO.dox
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/Gaim/
%{perl_vendorarch}/auto/Gaim/
%{_libdir}/%{name}/perl.so
%_libdir/%name/private/libgaimperl*

%files tcl
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}/tcl.so

%if %build_silc
%files silc
%defattr(-,root,root)
%doc libgaim/protocols/silc/README
%{_libdir}/%{name}/libsilcgaim.so
%endif

%if %build_evolution
%files gevolution
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}/gevolution.so
%endif

%if %build_meanwhile
%files meanwhile
%defattr(-,root,root)
%{_libdir}/%{name}/libsametime.so
%endif

%if %build_dbus
%files client
%defattr(-,root,root)
%doc COPYRIGHT
%{_bindir}/gaim-remote
%{_bindir}/gaim-send
%{_bindir}/gaim-send-async
%{_bindir}/gaim-client-example
%{_bindir}/gaim-url-handler
%attr(644,root,root) %{_libdir}/libgaim-client.la
%{_libdir}/libgaim-client.so.0*
%{_datadir}/dbus-1/services/gaim.service
%{_libdir}/gaim/dbus-example.so

%files client-devel
%defattr(-,root,root)
%{_libdir}/libgaim-client.so
%endif

%if %build_mono
%files mono
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}/mono.so
%{_libdir}/%{name}/*.dll
%endif

%clean
rm -rf %{buildroot}


