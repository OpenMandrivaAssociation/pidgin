%define version 2.3.1
%define release %mkrel 2

%define major 0
%define name pidgin
%define libname %mklibname purple %major
%define develname %mklibname purple -d

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

%{?_without_meanwhile: %{expand: %%global build_meanwhile 0}}
%{?_with_meanwhile: %{expand: %%global build_meanwhile 1}}

%{?_without_mono: %{expand: %%global build_mono 0}}
%{?_with_mono: %{expand: %%global build_mono 1}}

%{?_without_vv: %{expand: %%global build_vv 0}}
%{?_with_vv: %{expand: %%global build_vv 1}}

Summary:	A GTK+ based multiprotocol instant messaging client
Name:		pidgin
Version:	%{version}
Release:	%{release}
Group:		Networking/Instant messaging
License:	GPLv2+
URL:		http://www.pidgin.im/
Source0:	http://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.bz2
Source1:	facebook.c

Patch0:		pidgin-2.1.1-smiley.patch
Patch1:		http://www.nosnilmot.com/patches/pidgin-2.0.2-vertical-panel-icon.patch
#gw these patches were copied from the Fedora package
#gw fix reading resolv.conf in NetworkManager integration
Patch111:	pidgin-2.2.0-reread-resolvconf.patch
# (tpg) pidgin-privacy-please is useless without those two patches
Patch112:	http://tools.desire.ch/data/pidgin-pp/files/patches/pidgin-2.2.2-auth-signals-1.2.patch
Patch113:	http://tools.desire.ch/data/pidgin-pp/files/patches/pidgin-2.3.0-blocked-signals-1.0.patch
Patch114:	pidgin-2.2.1-jabber-crash-non-utf8-locale.patch
Patch115:	pidgin-2.3.1-gg-search-by-uin.patch
BuildRequires:	automake intltool
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
Buildrequires:	gtkspell-devel >= 2.0.2
Buildrequires:	sqlite3-devel
Buildrequires:	libncursesw-devel
# (tpg) libgadu is now in main, pidgin's one is really old
Buildrequires:	libgadu-devel >= 1.7.1-7
#gw we have networkmanager only in contribs:
#Buildrequires:	libnetworkmanager-glib-devel
BuildRequires:	libxscrnsaver-devel
BuildRequires:	libgstreamer0.10-devel
BuildRequires:	perl-devel
BuildRequires:	tk tk-devel tcl tcl-devel
BuildRequires:	startup-notification-devel >= 0.5
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
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	gnutls-devel
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
BuildRequires:	dbus-devel >= 0.50
%if %build_mono
BuildRequires:	mono-devel
%endif
%if %build_vv
BuildRequires:	libortp-devel >= 0.8.1
BuildRequires:	speex-devel
%endif
Obsoletes:	hackgaim <= 0.60 gaim
Provides:	hackgaim <= 0.60 gaim
Requires:	%{libname} >= %{version}-%{release}
Requires:	%{name}-i18n = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package plugins
Summary: Pidgin plugins shared by the Purple and Finch
Group: Networking/Instant messaging

%description plugins
This contains the parts of Pidgin that are shared between the Purple and
Finch Instant Messengers.


%package perl
Summary:	Purple extension, to use perl scripting
Group:		Networking/Instant messaging
Obsoletes:	gaim-perl
Provides:	gaim-perl
Requires:	%{name} = %{version}-%{release}

%description perl
Purple can use perl script as plugin, this plugin enable them.

%package tcl
Summary:	Purple extension, to use tcl scripting
Group:		Networking/Instant messaging
Obsoletes:	gaim-tcl
Provides:	gaim-tcl
Requires:	%{name} = %{version}-%{release}

%description tcl
Purple can use tcl script as plugin, this plugin enable them.

%package gevolution
Summary:	Pidgin extension, for Evolution integration
Group:		Networking/Instant messaging
Obsoletes:	gaim-gevolution
Provides:	gaim-gevolution
Requires:	%{name} = %{version}-%{release}

%description gevolution
This pidgin plugin allows you to have pidgin working together with evolution.

%package silc
Summary:	Purple extension, to use SILC (Secure Internet Live Conferencing)
Group:		Networking/Instant messaging
Obsoletes:	gaim-silc
Provides:	gaim-silc
Requires:	%{name} = %{version}-%{release}

%description silc
This purple plugin allows you to use SILC (Secure Internet Live Conferencing)
plugin for live video conference.

%package -n %{develname}
Summary:	Development files for pidgin
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Requires:	%{lib_console_app} = %{version}-%{release}
Provides:	libpidgin-devel = %{version}-%{release}
Provides:	pidgin-devel = %{version}-%{release}
Obsoletes:	gaim-devel

%description -n %{develname}
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%package -n %{libname}
Summary:	The libpurple library for IM clients like Pidgin and Finch
Group:		System/Libraries

%description -n %{libname}
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%package -n %{lib_console_app}
Summary:	The libgnt library for the Finch IM client
Group:		System/Libraries
Conflicts:	%mklibname gaim 0

%description -n %{lib_console_app}
libgnt contains the core IM support for the Finch IM client.

libgnt supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%package -n %{console_app}
Summary:	A text-based user interface for Pidgin
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	%{lib_console_app} >= %{version}-%{release}
Requires:	%{name}-i18n = %{version}-%{release}

%description -n	%{console_app}
A text-based user interface for using libpurple. This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.

%package bonjour
Summary:	Bonjour plugin for Purple
Group:		Networking/Instant messaging
Obsoletes:	gaim-bonjour
Provides:	gaim-bonjour
Requires:	%{name} = %{version}-%{release}

%description bonjour
Bonjour plugin for Purple

%package meanwhile
Summary:	Lotus Sametime Community Client plugin for Purple
Group:		Networking/Instant messaging
Obsoletes:	gaim-meanwhile
Provides:	gaim-meanwhile
Requires:	%{name} = %{version}-%{release}

%description meanwhile
Lotus Sametime Community Client plugin for purple

%package client
Summary:	Plugin and sample client to control purple clients
Group:		Networking/Instant messaging
Requires:	dbus-python
Obsoletes:	libgaim-remote0, gaim-client
Provides:	libgaim-remote0, gaim-client
Requires:	%{name} = %{version}-%{release}

%description client
Applications and library to control purple clients remotely.

%package mono
Summary:	Purple extension, to use Mono plugins
Group:		Networking/Instant messaging
Obsoletes:	gaim-mono
Provides:	gaim-mono
Requires:	%{name} = %{version}-%{release}

%description mono
Purple can use plugins developed with Mono.

%package facebook
Summary:	Facebook plugin for Pidgin
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description facebook
The Pidgin Facebook Plugin is a plugin for the pidgin 
instant messaging client that integrates facebook data
with the buddy data. It is currently in early development.

I have added a default API Key/Secret for the Mandriva
package, but please feel free to change this.

See: http://www.neaveru.com/wordpress/index.php/pidgin-facebook-plugin/ 

%package i18n
Summary:	Translation files for Pidgin/Finch
Group:		Networking/Instant messaging
Obsoletes:	%{name} < 2.1.0

%description i18n
This package contains translation files for Pidgin/Finch.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .smiley
#patch1 -p0 -b .vertical-panel-icon
%patch111 -p1

%patch112 -p1
%patch113 -p1

#%patch114 -p0
%patch115 -p1

%build
# (Abel) 0.72-3mdk Somehow it won't connect to servers if gaim is
#                  linked against gnutls
# (tpg) should work now!
%configure2_5x \
	--enable-gnutls=yes \
	--with-perl-lib=vendor \
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
	--without-krb4 \
	--with-gadu-includes=%{_includedir} \
	--with-gadu-libs=%{_libdir} \
	--disable-static
#gw parallel build doesn't work with the mono plugin
# (tpg) this dirty hack solves this :)
%(echo %make|perl -pe 's/-j\d+/-j1/g')

%install
rm -rf %{buildroot}

%makeinstall_std mkinstalldirs='mkdir -p'

### HACK Facebook plugin (colin)
pushd pidgin/plugins
cp -f %SOURCE1 .
make facebook.so
cp -a facebook.so %{buildroot}%{_libdir}/purple-2
popd
### END HACK

desktop-file-install \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network" \
  --add-category="InstantMessaging" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# remove files not bundled
rm -f %{buildroot}%{_libdir}/*/*.la
 
%find_lang %{name}

%post
%{update_menus}
%post_install_gconf_schemas purple
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas purple

%postun
%{clean_menus}
%clean_icon_cache hicolor

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n %{lib_console_app} -p /sbin/ldconfig
%postun -n %{lib_console_app} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYRIGHT ChangeLog
%doc NEWS README README.MTN doc/the_penguin.txt
%{_mandir}/man1/pidgin.*
%_sysconfdir/gconf/schemas/purple.schemas
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/icons/*
%{_datadir}/sounds/purple
%_libdir/pidgin/cap.so
%_libdir/pidgin/convcolors.so
%_libdir/pidgin/extplacement.so
%_libdir/pidgin/gestures.so
%_libdir/pidgin/gtkbuddynote.so
%_libdir/pidgin/history.so
%_libdir/pidgin/iconaway.so
%_libdir/pidgin/markerline.so
%_libdir/pidgin/musicmessaging.so
%_libdir/pidgin/notify.so
%_libdir/pidgin/pidginrc.so
%_libdir/pidgin/relnot.so
%_libdir/pidgin/spellchk.so
%_libdir/pidgin/ticker.so
%_libdir/pidgin/timestamp.so
%_libdir/pidgin/timestamp_format.so
%_libdir/pidgin/xmppconsole.so
%_libdir/purple-2/autoaccept.so
%_libdir/purple-2/buddynote.so
%_libdir/purple-2/idle.so
%_libdir/purple-2/joinpart.so
%_libdir/purple-2/libaim.so
%_libdir/purple-2/libgg.so
%_libdir/purple-2/libicq.so
%_libdir/purple-2/libirc.so
%_libdir/purple-2/libjabber.so
%_libdir/purple-2/libjabber.so.0
%_libdir/purple-2/libjabber.so.0.0.0
%_libdir/purple-2/libmsn.so
%_libdir/purple-2/libmyspace.so
%_libdir/purple-2/libnovell.so
%_libdir/purple-2/liboscar.so
%_libdir/purple-2/liboscar.so.0
%_libdir/purple-2/liboscar.so.0.0.0
%_libdir/purple-2/libqq.so
%_libdir/purple-2/libsimple.so
%_libdir/purple-2/libxmpp.so
%_libdir/purple-2/libyahoo.so
%_libdir/purple-2/libzephyr.so
%_libdir/purple-2/log_reader.so
%_libdir/purple-2/newline.so
%_libdir/purple-2/offlinemsg.so
%_libdir/purple-2/psychic.so
%_libdir/purple-2/ssl-gnutls.so
%_libdir/purple-2/ssl-nss.so
%_libdir/purple-2/ssl.so
%_libdir/purple-2/statenotify.so
%_datadir/purple/ca-certs/*.pem

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog.API HACKING PLUGIN_HOWTO
%{_includedir}/*
%{_datadir}/aclocal/purple.m4
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpurple.so
%{_libdir}/libgnt.so
%{_libdir}/libpurple-client.so
%{_libdir}/lib*.la

%files -n %{libname}
%defattr(-,root,root)
%_libdir/libpurple.so.%{major}*

%files -n %{console_app}
%defattr(-, root, root)
%doc %{_mandir}/man1/%{console_app}.*
%{_bindir}/%{console_app}
%_libdir/finch/
%_libdir/gnt/

%files -n %{lib_console_app}
%defattr(-, root, root)
%{_libdir}/libgnt.so.%{major}*

%files bonjour
%defattr(-,root,root)
%{_libdir}/purple-2/libbonjour.so

%files perl
%defattr(-,root,root)
%doc doc/PERL-HOWTO.dox
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/auto/Pidgin/*
%{perl_vendorarch}/auto/Purple/*
%{_libdir}/purple-2/perl.so
%{_mandir}/man3*/*

%files tcl
%defattr(-,root,root)
%doc COPYING
%{_libdir}/purple-2/tcl.so

%if %build_silc
%files silc
%defattr(-,root,root)
%doc libpurple/protocols/silc/README
%{_libdir}/purple-2/libsilcpurple.so
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
%{_libdir}/purple-2/libsametime.so
%endif

%files client
%defattr(-,root,root)
%doc COPYRIGHT
%{_bindir}/purple-remote
%{_bindir}/purple-send
%{_bindir}/purple-send-async
%{_bindir}/purple-client-example
%{_bindir}/purple-url-handler
%{_libdir}/libpurple-client.so.0*
%{_libdir}/purple-2/dbus-example.so

%if %build_mono
%files mono
%defattr(-,root,root)
%doc COPYING
%{_libdir}/purple-2/mono.so
%{_libdir}/purple-2/*.dll
%endif

%files facebook
%defattr(-,root,root)
%doc COPYING
%{_libdir}/purple-2/facebook.so

%files i18n -f %{name}.lang
%defattr(-,root,root)

%clean
rm -rf %{buildroot}
