#gw 2.7.0, the yahoo plugin does not build otherwise
%define _disable_ld_no_undefined 1

%define major 0
%define libname %mklibname purple %{major}
%define libclient %mklibname purple-client %{major}
%define libgnt %mklibname gnt %{major}
%define develname %mklibname purple -d

%define build_evolution 1
%define build_silc 1
%define build_meanwhile 1
%define build_networkmanager 1
%define build_perl 1
#gw http://developer.pidgin.im/ticket/11936#comment:1
%define build_mono 0
%define build_vv 1
# (tpg) libgadu is now in main, pidgin's one is really old
# gw pidgin's internal libgadu was updated recently
# build against external version if possible, keep in mind older distros
# might have older libgadu
#gw configure check is used unless --with-* options are used:
%define build_libgadu 0

%ifarch mips mipsel
%define build_mono 0
%endif

%if %mdvver < 201020
%define build_vv 0
%endif

Summary:	A GTK+ based multiprotocol instant messaging client
Name:		pidgin
Version:	2.10.4
Release:	%mkrel 1
Group:		Networking/Instant messaging
License:	GPLv2+
URL:		http://www.pidgin.im/
Source0:	http://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.bz2
#gw from Fedora: generate one time passwords
Source2:	one_time_password.c
Patch0:		pidgin-2.7.0-smiley.patch
Patch3:		pidgin-2.4.2-set-jabber-as-module.patch
#gw fix build with mono 2.6.4 which does not have the nessessary glib dep
#in the pkgconfig file
#also add missing include
Patch6:		pidgin-2.7.0-mono-build.patch
#gw fix reading resolv.conf in NetworkManager integration
Patch111:	%{name}-2.8.0-reread-resolvconf.patch
Patch115:	%{name}-2.10.0-gg-search-by-uin.patch
Patch116:	%{name}-2.8.0-gg-disconnect.patch
Patch117:	pidgin-2.10.1-fix-perl-module-build.patch
# since libtool drops soname for unversioned modules now, we need to explicitly
# add soname to plugins that other plugins links against it
Patch118:	pidgin-2.10.2-explicitly-add-soname-to-liboscar-and-libjabber.patch

BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	GConf2
BuildRequires:	graphviz
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	krb5-devel
BuildRequires:	tk-devel
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(gnutls)

BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gtk+-2.0)
Buildrequires:	pkgconfig(gtkspell-2.0) >= 2.0.2
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(jack)
BuildRequires:  pkgconfig(libidn)
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.5
Buildrequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(nspr)
%if %mdkversion >= 201100
Buildrequires:	pkgconfig(python)
%else
BuildRequires:	python-devel
%endif
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sm)
Buildrequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(x11)
%if %build_libgadu
Buildrequires:	pkgconfig(libgadu) >= 1.11.0
%endif
%if %build_networkmanager
Buildrequires:	pkgconfig(libnm-util)
%endif
%if %build_meanwhile
BuildRequires:	pkgconfig(meanwhile) >= 1.0.0
%endif
%if %build_evolution
BuildRequires:	pkgconfig(evolution-data-server-1.2)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:  pkgconfig(libedata-book-1.2)
%endif
%if %build_silc
BuildRequires:	pkgconfig(silc) >= 0.9.12
BuildRequires:	pkgconfig(silcclient) >= 0.9.12
%endif
%if %build_perl
BuildRequires:	perl-devel
%endif
%if %build_mono
BuildRequires:	pkgconfig(mono)
%endif
%if %build_vv
BuildRequires:  pkgconfig(farsight2-0.10)
Suggests: gstreamer0.10-farsight2
%endif

Requires:	%{name}-i18n = %{version}-%{release}
Requires:	%{name}-plugins = %{version}-%{release}
Requires:	%{name}-client >= %{version}-%{release}
Requires:	rootcerts
Requires:	xdg-utils

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
Summary:	Pidgin plugins shared by the Purple and Finch
Group:		Networking/Instant messaging
Conflicts:	%{name} < 2.4.1-3

%description plugins
This contains the parts of Pidgin that are shared between the Purple and
Finch Instant Messengers.

%package perl
Summary:	Purple extension, to use perl scripting
Group:		Networking/Instant messaging
Requires:	%{name} >= %{version}-%{release}

%description perl
Purple can use perl script as plugin, this plugin enable them.

%package tcl
Summary:	Purple extension, to use tcl scripting
Group:		Networking/Instant messaging
Requires:	%{name} >= %{version}-%{release}

%description tcl
Purple can use tcl script as plugin, this plugin enable them.

%if %build_evolution
%package gevolution
Summary:	Pidgin extension, for Evolution integration
Group:		Networking/Instant messaging
Requires:	%{name} >= %{version}-%{release}

%description gevolution
This pidgin plugin allows you to have pidgin working together with evolution.
%endif

%package silc
Summary:	Purple extension, to use SILC (Secure Internet Live Conferencing)
Group:		Networking/Instant messaging
Requires:	%{name} >= %{version}-%{release}

%description silc
This purple plugin allows you to use SILC (Secure Internet Live Conferencing)
plugin for live video conference.

%package -n %{develname}
Summary:	Development files for pidgin
Group:		Development/GNOME and GTK+
Requires:	%{libname} >= %{version}-%{release}
Requires:	%{libgnt} = %{version}-%{release}
Requires:	%{libclient} = %{version}-%{release}
Provides:	pidgin-devel = %{version}-%{release}

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

%package -n %{libclient}
Summary:	The libpurple-client library for %{name}-client
Group:		System/Libraries
Conflicts:	%{name}-client < 2.10.1-1

%description -n %{libclient}
libpurple-client contains the shared library for %{name}-client.

%package -n %{libgnt}
Summary:	The libgnt library for the Finch IM client
Group:		System/Libraries
%rename %{_lib}finch0

%description -n %{libgnt}
libgnt contains the core IM support for the Finch IM client.

libgnt supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.

%package -n finch
Summary:	A text-based user interface for Pidgin
Group:		Networking/Instant messaging
Requires:	%{name}-i18n >= %{version}-%{release}
Requires:	%{name}-plugins >= %{version}-%{release}
Requires:	%{name}-client >= %{version}-%{release}

%description -n	finch
A text-based user interface for using libpurple. This can be run from a
standard text console or from a terminal within X Windows.  It
uses ncurses and our homegrown gnt library for drawing windows
and text.

%package bonjour
Summary:	Bonjour plugin for Purple
Group:		Networking/Instant messaging
Requires:	%{name} >= %{version}-%{release}

%description bonjour
Bonjour plugin for purple.

%package meanwhile
Summary:	Lotus Sametime Community Client plugin for Purple
Group:		Networking/Instant messaging
Requires:	%{name} >= %{version}-%{release}

%description meanwhile
Lotus Sametime Community Client plugin for purple.

%package client
Summary:	Plugin and sample client to control purple clients
Group:		Networking/Instant messaging
Requires:	dbus-python

%description client
Applications and library to control purple clients remotely.

%if %build_mono
%package mono
Summary:	Purple extension, to use Mono plugins
Group:		Networking/Instant messaging
Requires:	%{name} >= %{version}-%{release}

%description mono
Purple can use plugins developed with Mono.
%endif

%package i18n
Summary:	Translation files for Pidgin/Finch
Group:		Networking/Instant messaging

%description i18n
This package contains translation files for Pidgin/Finch.

%prep
%setup -q
%patch0 -p1 -b .smiley
%patch3 -p0
%patch6 -p1
%patch111 -p1 -b .reread-resolvconf
%patch115 -p1 -b .gg-search
%patch116 -p1
%patch117 -p1 -b .perl_buildfix~
%patch118 -p1 -b .soname~

autoreconf -fi -Im4macros

%build
%configure2_5x \
	--enable-gnutls=yes \
%if %build_perl
	--enable-perl \
%else
	--disable-perl \
%endif
%if %build_mono
	--enable-mono \
%else
	--disable-mono \
%endif
%if %build_networkmanager
	--enable-nm \
%else
	--disable-nm \
%endif
%if %build_evolution
	--enable-gevolution \
%endif
%if ! %build_vv
	--disable-vv \
%endif
	--without-krb4 \
	--enable-cap \
	--with-system-ssl-certs=%{_sysconfdir}/pki/tls/rootcerts/ \
	--disable-static \
	--disable-schemas-install

%make

# one_time_password plugin, to be merged upstream soon
cp %{SOURCE2} libpurple/plugins/
pushd libpurple/plugins/
make one_time_password.so
popd

%install
rm -rf %{buildroot}

%makeinstall_std mkinstalldirs='mkdir -p'

install -m 0755 libpurple/plugins/one_time_password.so %{buildroot}%{_libdir}/purple-2/

desktop-file-install \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network" \
  --add-category="InstantMessaging" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# remove files not bundled
rm -f %{buildroot}%{_libdir}/*/*.la 
rm -f %{buildroot}%{_prefix}/*/perl5/*/perllocal.pod \
      %{buildroot}%{_libdir}/*/perl/auto/*/{.packlist,*.bs,autosplit.ix}
rm -f %{buildroot}%{_libdir}/*.*a

%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas purple

%files i18n -f %{name}.lang

%files
%doc AUTHORS COPYRIGHT ChangeLog
%doc NEWS README README.MTN doc/the_penguin.txt
%{_mandir}/man1/pidgin.*
%{_sysconfdir}/gconf/schemas/purple.schemas
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/icons/*
%{_datadir}/sounds/purple
%{_libdir}/pidgin/cap.so
%{_libdir}/pidgin/convcolors.so
%{_libdir}/pidgin/extplacement.so
%{_libdir}/pidgin/gestures.so
%{_libdir}/pidgin/gtkbuddynote.so
%{_libdir}/pidgin/history.so
%{_libdir}/pidgin/iconaway.so
%{_libdir}/pidgin/markerline.so
%{_libdir}/pidgin/musicmessaging.so
%{_libdir}/pidgin/notify.so
%{_libdir}/pidgin/pidginrc.so
%{_libdir}/pidgin/relnot.so
%{_libdir}/pidgin/sendbutton.so
%{_libdir}/pidgin/spellchk.so
%{_libdir}/pidgin/themeedit.so
%{_libdir}/pidgin/ticker.so
%{_libdir}/pidgin/timestamp.so
%{_libdir}/pidgin/timestamp_format.so
%if %build_vv
%{_libdir}/pidgin/vvconfig.so
%endif
%{_libdir}/pidgin/xmppconsole.so
%{_libdir}/pidgin/xmppdisco.so

%files -n %{develname}
%doc ChangeLog.API HACKING PLUGIN_HOWTO
%{_includedir}/*
%{_datadir}/aclocal/purple.m4
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libpurple.so
%{_libdir}/libgnt.so
%{_libdir}/libpurple-client.so

%files -n %{libname}
%{_libdir}/libpurple.so.%{major}*

%files -n %{libclient}
%{_libdir}/libpurple-client.so.%{major}*

%files -n %{libgnt}
%{_libdir}/libgnt.so.%{major}*

%files client
%{_bindir}/purple-remote
%{_bindir}/purple-send
%{_bindir}/purple-send-async
%{_bindir}/purple-client-example
%{_bindir}/purple-url-handler
%{_libdir}/purple-2/dbus-example.so

%files -n finch
%doc %{_mandir}/man1/finch.*
%{_bindir}/finch
%{_libdir}/finch/
%{_libdir}/gnt/

%if %build_perl
%files perl
%doc doc/PERL-HOWTO.dox
%dir %{_libdir}/%{name}/perl
%{_libdir}/%{name}/perl/Pidgin.pm
%dir %{_libdir}/%{name}/perl/auto
%dir %{_libdir}/%{name}/perl/auto/Pidgin/
%{_libdir}/%{name}/perl/auto/Pidgin/Pidgin.so
%dir %{_libdir}/purple-2/perl
%{_libdir}/purple-2/perl/Purple.pm
%dir %{_libdir}/purple-2/perl/auto
%dir %{_libdir}/purple-2/perl/auto/Purple/
%{_libdir}/purple-2/perl/auto/Purple/Purple.so
%{_libdir}/purple-2/perl.so
%{_mandir}/man3*/*
%endif

%files bonjour
%{_libdir}/purple-2/libbonjour.so

%files tcl
%doc doc/TCL-HOWTO.dox
%{_libdir}/purple-2/tcl.so

%if %build_silc
%files silc
%doc libpurple/protocols/silc/README
%{_libdir}/purple-2/libsilcpurple.so
%endif

%if %build_evolution
%files gevolution
%{_libdir}/%{name}/gevolution.so
%endif

%if %build_meanwhile
%files meanwhile
%{_libdir}/purple-2/libsametime.so
%endif

%if %build_mono
%files mono
%{_libdir}/purple-2/mono.so
%{_libdir}/purple-2/*.dll
%endif

%files plugins
%dir %{_libdir}/purple-2
%{_libdir}/purple-2/autoaccept.so
%{_libdir}/purple-2/buddynote.so
%{_libdir}/purple-2/idle.so
%{_libdir}/purple-2/joinpart.so
%{_libdir}/purple-2/libaim.so
%{_libdir}/purple-2/libgg.so
%{_libdir}/purple-2/libicq.so
%{_libdir}/purple-2/libirc.so
%{_libdir}/purple-2/libjabber.so
%{_libdir}/purple-2/libmsn.so
%{_libdir}/purple-2/libmxit.so
%{_libdir}/purple-2/libmyspace.so
%{_libdir}/purple-2/libnovell.so
%{_libdir}/purple-2/liboscar.so
%{_libdir}/purple-2/libsimple.so
%{_libdir}/purple-2/libxmpp.so
%{_libdir}/purple-2/libymsg.so*
%{_libdir}/purple-2/libyahoo.so
%{_libdir}/purple-2/libyahoojp.so
%{_libdir}/purple-2/libzephyr.so
%{_libdir}/purple-2/log_reader.so
%{_libdir}/purple-2/newline.so
%{_libdir}/purple-2/offlinemsg.so
%{_libdir}/purple-2/one_time_password.so
%{_libdir}/purple-2/psychic.so
%{_libdir}/purple-2/ssl-gnutls.so
%{_libdir}/purple-2/ssl-nss.so
%{_libdir}/purple-2/ssl.so
%{_libdir}/purple-2/statenotify.so
%dir %{_datadir}/purple/
%dir %{_datadir}/purple/ca-certs
%{_datadir}/purple/ca-certs/AOL*
%{_datadir}/purple/ca-certs/Microsoft*
%{_datadir}/purple/ca-certs/VeriSign*
%{_datadir}/purple/ca-certs/DigiCert*

