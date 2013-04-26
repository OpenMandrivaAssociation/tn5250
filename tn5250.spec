%define Werror_cflags %nil

%define major   1
%define libname %mklibname %name %major

%define summary 5250 Telnet protocol and Terminal
%define title tn5250

Summary: 	5250 Telnet protocol and Terminal
Name: 		tn5250
Version: 	0.17.4
Release: 	5
License: 	GPL & LGPL
Group: 		Networking/Other
Source: 	http://prdownloads.sourceforge.net/tn5250/%{name}-%{version}.tar.bz2
Url: 		http://tn5250.sourceforge.net
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
%configure2_5x --with-x --with-ssl
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

install -d -m 0755 %{buildroot}/%{_menudir}
install -d -m 0755 %{buildroot}/%{_miconsdir}
install -d %{buildroot}%{_datadir}/icons
install -d %{buildroot}/etc/X11/applnk/Internet/
install linux/5250.tcap %{buildroot}%{_datadir}/%{name}
install linux/5250.terminfo %{buildroot}%{_datadir}/%{name}
install *.png %{buildroot}%{_datadir}/icons
install *.xpm %{buildroot}%{_datadir}/icons
mv -f linux/README README.linux
cp -f %{name}-48x48.png %{buildroot}%{_datadir}/icons/%{name}.png


%post
if which tic>/dev/null 2>&1; then tic %{_datadir}/%{name}/5250.terminfo >/dev/null 2>&1; fi

%preun
if [ $1 = 0 ]; then
rm -f %{_datadir}/terminfo/5/5250
rm -f %{_datadir}/terminfo/X/xterm-5250
fi

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.ssl TODO README.linux
%{_bindir}/*5250
%{_bindir}/*5250d
%{_bindir}/scs2*
%{_bindir}/5250keys
%{_mandir}/man[15]/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/icons/*
%{_datadir}/applications/mandriva-%{name}.desktop

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*a
%{_libdir}/*so
%{_includedir}/tn5250.h
%dir %{_includedir}/tn5250
%{_includedir}/tn5250/*.h


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17.4-4mdv2011.0
+ Revision: 615232
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 0.17.4-3mdv2010.1
+ Revision: 536661
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Jan 12 2009 Jérôme Soyer <saispo@mandriva.org> 0.17.4-1mdv2009.1
+ Revision: 328670
- New upstream release

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.17.3-6mdv2009.0
+ Revision: 261571
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.17.3-5mdv2009.0
+ Revision: 254665
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.17.3-3mdv2008.1
+ Revision: 136546
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import tn5250


* Sun Aug 06 2006 Jerome Soyer <saispo@mandriva.org> 0.17.3-3mdv2007.0
- Fix Icons Menu

* Fri Jul 28 2006 Jerome Soyer <saispo@mandriva.org> 0.17.3-2mdv2007.0
- Fix Menu Entry

* Thu Jun 29 2006 Jerome Soyer <saispo@mandriva.org> 0.17.3-1mdv2007.0
- New release 0.17.3
- XDG Menu
- Remove SOURCE1
- Fix rpmlint error

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.16.5-4mdk
- rebuilt against openssl-0.9.8a

* Fri May  6 2005 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.16.5-3mdk
- Fix menu for x86_64
- Add mutliarch headers (lmontel)

* Thu Jul 22 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.16.5-2mdk
- Add a menu entry for xt5250

* Thu Jun 24 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.16.5-1mdk
- 0.16.5
- First Mandrakelinux package

* Mon May 13 2002 Steve Fox <drfickle@us.ibm.com>
- 0.16.4
- Convert to spec.in

* Mon Dec 12 2001 Steve Fox <drfickle@us.ibm.com>
- 0.16.3

* Mon Jan 29 2001 Henri Gomez <hgomez@slib.fr>
- 0.16.1 RPM release 2
- Dave McKenzie's cursor positioning fixes
- Scott Klement fixes to lp5250d, auto-enter field handling,
  field plus & field minus key handling , FER state key handling

* Fri Dec 22 2000 Henri Gomez <hgomez@slib.fr>
- 0.16.1

* Tue Dec 12 2000 Henri Gomez <hgomez@slib.fr>
- 0.16.0
- many fixes, take a look at ChangeLog
- compiled on Redhat 6.1 box plus updates with rpm-3.0.5

* Fri May 02 2000 Henri Gomez <hgomez@slib.fr>
- 0.16.0pre2

* Tue Apr 04 2000 Henri Gomez <gomez@slib.fr>
- 0.15.8-1
- Removed backspace patch (included in 0.15.8)

* Tue Feb 15 2000 Henri Gomez <gomez@slib.fr>
- 0.15.7-2
- Backspace problem corrected (Carey Evans Patch)

* Thu Feb 10 2000 Henri Gomez <gomez@slib.fr>
- 0.15.7
- Removed config.guess and config.sub from CVS since they should be
  provided by autogen.sh.
- Added --enable-old-keys switch to configure to compile in the old
  keyboard handler (preparation for 0.15.7).
- Fixed bugs with handling response code for printer sessions.
- Added a response code/error message lookup table so that we can get
  the error message in Plain English (tm).
- Apply patch from Mike Madore regarding IBMTRANSFORM set incorrectly
  (for printer sessions).
- Documented `-P cmd' option in usage message, removed `-p' option to
  indicate print session as `-P cmd' is required for a working session
  anyway.
- Fixed typo in new key-parsing code preventing PgDn from working.
- Added code to handle Esc+Del = Ins vt100 key mapping.
- Added stuff to XTerm resources to turn on real underlining and turn
  off silly color-instead-of-underline mode.
- Throw away weird keys we get from ncurses4 after before first
  keypress.
- Implemented FER (Field-Exit Required) state (not tested).
- Use 'TERM' to determine if terminal is an xterm or xterm-5250, as it
  *works* :) (Thanks to Frank Richter for pointing out bug).
- Apply Frank Richter's cursor-position-on-status-line patch.
- Implement rest of keys for #defined USE_OWN_KEY_PARSING.
- Finally object-orientized translation map stuff, but will have to be
  modified later to handle wide characters/DBCS characters/Unicode -
  however we intend to support different character sets better.
- In Field Exit handling for signed numeric fields, don't NUL-out the last
  (sign) position of the field - this is what Field- and Field+ are for.
- Home key when already in home position should send the Home aid code,
  even when we have a pending insert.  Also, home key should move to the
  beginning of the *first non-bypass field* not the *current field* when
  there is no pending insert (IC address).
- Clear pending insert flag on Clear Unit or Clear Unit Alternate command.

* Wed Jan 12 2000 Henri Gomez <gomez@slib.fr>
- 0.15.6
- Reported by Phil Gregory - display is not inhibited and cursor is not in
  proper place after Write Error Code.
- Implemented Read Immediate Alternate and Read MDT Fields Alternate commands,
  modified tn5250_session_query_reply to indicate that we now support them to
  the host.
- Implemented TD (Transparent Data) order.  There is apparently nowhere to
  indicate this to the host. (This may have been the cause of earlier binary
  data issues).
- Implemented MC (Move Cursor) order.  This is now indicated to the host.
- Move remaining keyboard handling from session.c to display.c, make
  tn5250_display_waitevent NOT return keyboard events. (Might we want to
  pass along ones we don't understand?  Nah...)
- Save/restore message line when Write Error Code is used by the host to
  inhibit display.  Also, use the correct message line (according to the
  format table header).
- Added refresh() call to cursesterm.c.  Hopefully, this will resolve the
  80 -> 132 column switch refresh issues reported by some users.
- Wrote a quick hack of a Perl script to insert Robodoc comment headers
  for all the functions (and manually did all the structures).  Yeah, it's
  ugly, but no-one produces a tool as good as Javadoc which works on C.
- tn5250_dbuffer_send_data_for_fields(): A *SET* bit inhibits the transmission
  of field data, not a clear one.  Also, fine point of spec, all three aid key
  bytes must be present before the 5294 controller will obey any of them.
- Carey Evans' suggestions for new xt5250 script portability, security
  incorporated.
- xt5250: Now changes window title to name of host.
- cursesterm.c: Now obeys the information returned from ENQ about what
  type of terminal, and only uses xterm resize escape when on an xterm
  again.


* Thu Jan  6 2000 Henri Gomez <gomez@slib.fr>
- 0.15.5
- Extensively modified xt5250 script to prompt for hostname if not given,
  automagically use xrdb to load the keyboard mappings.  Inspired by Henri
  (Thanks!)
- Renamed Xdefaults to xt5250.keys, installs in $pkgdatadir, also
  installs Linux keyboard maps there.
- Removed smacs, rmacs, and acsc from 5250.terminfo - we don't use them and
  they don't seem to work under an xterm.  Makes 'dialog' draw all sorts of
  funny looking characters.
- If installing on Linux system, automatically 'tic 5250.terminfo' if
  tic command is found (and user is root).
- Fixed bit-ordering issue causing beeps/screen flashes all the time
  (hopefully).
- Happy Y2K!
- Changed handling of Field+ and Field- in regards to number-only-type
  fields.
- No longer ignores the function key bits in the format table header.  This
  means that we won't transmit the field data for a function key unless the
  AS/400 has requested it.
- Rolled Tn5250Table functionality into Tn5250DBuffer, removed
  formattable.[ch] and resulting duplicate functionality in display.c
- Apparently, the AS/400 and S/36 differ in how they send the client the
  Restore Screen data.  The AS/400 just sends the data raw, while the
  System/36 prefixes it with a X'04' X'12' (Restore Screen) opcode.  This
  is now ignored.
- Removed portsnoop. It doesn't belong here and there's better stuff out
  there (check freshmeat.net).  nc seems to work well, and is installed on
  most distributions by default.
  formattable.[ch] and resulting duplicate functionality in display.c
- Apparently, the AS/400 and S/36 differ in how they send the client the
  Restore Screen data.  The AS/400 just sends the data raw, while the
  System/36 prefixes it with a X'04' X'12' (Restore Screen) opcode.  This
  is now ignored.
- Removed portsnoop. It doesn't belong here and there's better stuff out
  there (check freshmeat.net).  nc seems to work well, and is installed on
  most distributions by default.

* Tue Dec 21 1999 Henri Gomez <gomez@slib.fr>
- 0.15.4
- Rewrite of screen/format table save/restore code to generate Write to Display
  commands and orders.  This should even allow you to resume a session with
  a different emulator and have the restore screen feature still work.  This
  results in a noticable slowdown in situations where the save screen command
  is used.
- Fixes for End key behavior.
- Fixes for Del key behavior, other keys which weren't setting the field's
  modified flag.
- Buffered keystrokes will now cause the display to update.
- Some 'binary' characters now accepted as data characters.
- CC1/CC2 bytes in Read MDT Fields/Read INput Fields commands were not being
  handled.
- Partial work on restructuring... Auto Enter fields now work again.
- Updates to documentation and NEWS, including information about the FAQ and
  mailing list archives.


* Wed Nov 24 1999 Henri Gomez <gomez@slib.fr>
- 0.15.3
  When using --with-slang configure option, no longer cores after signon
  screen.
  When using debug:tracefile syntax, no longer cores after signon screen.
  Fixed assertion found by Sean Porterfield regarding 132-column display.
  Slight work to reduce number of screen updates, although this isn't
  finished.
  Some work on solidifying the lib API.


* Fri Nov 18 1999 Henri Gomez <gomez@slib.fr>
- 0.15.2
 Field Exit and Field + are now seperate functions. '+' in numeric field
  maps to Field +.  Field + changes the sign of the number like it should.
- Re-implemented transmitting signed fields to host.
- Re-implemented Field -.
- Numeric Only and Signed Number field types are handled according to spec
  now, even though the spec is really weird about how they are handled
  (The last digit's zone is changed on Numeric Only on Field -/+, but the
  sign position is changed from ' ' to '-' with Field -/+, and the zone
  shift for that one takes place at transmit.)
- Now ignore garbage keys again.  Why are we getting two decimal 410s when
  we type the first character?  This doesn't make sense unless it's related
  to how we detect the xterm.

* Wed Nov 17 1999 Henri Gomez <gomez@slib.fr>
- 0.15.1
- 3/4ths of the restructuring to make it feasible to use lib5250 for display
  services for applications has been done.
- Lots of cleanup - no longer has duplicate field value data, nor does it have
  many different componenets having a different perception of what the current
  field is.
- Implemented terminal bells.  Whistles yet to come.
- Some minor stuff.  Field Exit Required fields now require field exit, for
  example.

* Tue Nov  2 1999 Henri Gomez <gomez@slib.fr>
- 0.14
- Full FreeBSD support, see the README and other files in the freebsd/
  directory.  Special thanks to Scott Klement for this (I've put his name all
  over the ChangeLog for this -- this way, it's not _my_ fault <g>).
- Linux-specific files moved to linux/ subdir.
- README files updated - now more clear on how to set up X Windows support.
- Field Minus sequence (Esc+M) added.
- Dup key support added.
- Small field exit bug fixed.
- Help key/aid code implemented.
- Fix per Carey Evans for handling right-blank fields.
- Reset key now works even when keyboard is locked.  Possible but unlikely bug
  where reset key could cause the next keystroke to be ignored is fixed.
- C programs which use stdin/stdout will now clear the input line properly.
- A small fix to format table handling code with the Repeat to Address order.
  This problem may never have been observed, but hey...

* Mon Oct 6 1999 Henri Gomez <gomez@slib.fr>
- updated Readme

* Fri Oct 1 1999 Henri Gomez <gomez@slib.fr>
- 0.13.13
- added xrdb load key in xt5250
- added gnome icons entry for xt5250

* Mon Sep 6 1999 Henri Gomez <gomez@slib.fr>
- 0.13.12

* Wed Sep 1 1999 Henri Gomez <gomez@slib.fr>
- 0.13.11
  Initial RPM release
