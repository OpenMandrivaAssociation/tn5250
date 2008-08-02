%define name tn5250
%define ver 0.17.3

%define major   1
%define libname %mklibname %name %major

%define summary 5250 Telnet protocol and Terminal
%define title tn5250

Summary: 	5250 Telnet protocol and Terminal
Name: 		%name
Version: 	%ver
Release: 	%mkrel 6
License: 	GPL & LGPL
Group: 		Networking/Other
Source: 	http://prdownloads.sourceforge.net/tn5250/%{name}-%{version}.tar.bz2
Url: 		http://tn5250.sourceforge.net
BuildRoot: 	%_tmppath/%name-%version-%release-root
Requires:	ncurses, openssl
BuildRequires:	ncurses-devel, openssl-devel
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
tn5250 is an implementation of the 5250 Telnet protocol
It provide 5250 library and 5250 terminal emulation

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for 5250 protocol
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
tn5250 is an implementation of the 5250 Telnet protocol
It provide 5250 library and 5250 terminal emulation

%package devel
Group:		Development/Other
Summary:	Development tools for 5250 protocol
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-devel

%description devel
tn5250 is an implementation of the 5250 Telnet protocol
It provide 5250 library and 5250 terminal emulation

%prep
%setup -q
perl -pi -e 's,Example\:,Example\:\\n\\,' src/tn5250.c

%build
%configure --with-x --with-ssl
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title}
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=ConsoleOnly;TerminalEmulator;X-MandrivaLinux-System-Terminals;
EOF

install -d -m 0755 %buildroot/%_menudir
install -d -m 0755 %buildroot/%_miconsdir
install -d %{buildroot}%{_datadir}/icons
install -d %{buildroot}/etc/X11/applnk/Internet/
install linux/5250.tcap $RPM_BUILD_ROOT%{_datadir}/%{name}
install linux/5250.terminfo $RPM_BUILD_ROOT%{_datadir}/%{name}
install *.png %{buildroot}%{_datadir}/icons
install *.xpm %{buildroot}%{_datadir}/icons
mv -f linux/README README.linux
cp -f %{name}-48x48.png %{buildroot}%{_datadir}/icons/%{name}.png

%multiarch_includes %buildroot%_includedir/tn5250/config.h

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT


%post
if which tic>/dev/null 2>&1; then tic %{_datadir}/%{name}/5250.terminfo >/dev/null 2>&1; fi
%{update_desktop_database}

%postun
%{clean_desktop_database}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%preun
if [ $1 = 0 ]; then
rm -f %{_datadir}/terminfo/5/5250
rm -f %{_datadir}/terminfo/X/xterm-5250
fi

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.ssl TODO README.linux
%{_bindir}/*5250
%{_bindir}/*5250d
%{_bindir}/scs2*
%{_mandir}/man[15]/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/icons/*
%{_datadir}/applications/mandriva-%{name}.desktop

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*a
%{_libdir}/*so
%{_bindir}/*-config
%{_includedir}/tn5250.h
%dir %{_includedir}/tn5250
%{_includedir}/tn5250/*.h
%dir %_datadir/aclocal
%_datadir/aclocal/tn5250.m4
%{_libdir}/pkgconfig/tn5250.pc

%multiarch %dir %_includedir/%multiarch_platform/tn5250
%multiarch %_includedir/%multiarch_platform/tn5250/*.h

