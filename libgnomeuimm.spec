Name:           libgnomeuimm26
Version:        2.28.0
Release:        1%{?dist}

Summary:        C++ interface for Gnome libs (a GUI library for X)

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgnomeuimm/2.28/libgnomeuimm-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  libgnomeui-devel >= 2.7.1
BuildRequires:  libgnomemm26-devel >= 2.16.0
BuildRequires:  libgnomecanvasmm26-devel >= 2.6.0
BuildRequires:  gconfmm26-devel >= 2.6.0
BuildRequires:  libglademm24-devel >= 2.4.0
BuildRequires:  gnome-vfsmm26-devel >= 2.16.0

%description
This package provides a C++ interface for GnomeUI.  It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary:        Headers for developing programs that will use Gnome--
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libgnomeui-devel
Requires:       libgnomemm26-devel
Requires:       libgnomecanvasmm26-devel
Requires:       gconfmm26-devel
Requires:       libglademm24-devel
Requires:       gnome-vfsmm26-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use Gnome--, part of Gtk-- the C++ interface to
the GTK+ (the Gimp ToolKit) GUI library.


%prep
%setup -q -n libgnomeuimm-%{version}


%build
%configure --disable-static --enable-docs
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/libgnomeuimm-2.6
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.28.0-1
- Update to upstream 2.28.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr  7 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-1
- Update to upstream 2.26.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0

* Wed Mar 12 2008 Denis Leroy <denis@poolshark.org> - 2.22.0-1
- Update to 2.22.0

* Mon Feb 11 2008 Denis Leroy <denis@poolshark.org> - 2.20.2-1
- Update to 2.20.2, more gcc 4.3 fixes

* Tue Jan 29 2008 Denis Leroy <denis@poolshark.org> - 2.20.1-1
- Update to upstream 2.20.1, gcc 4.3 fixes
- BR versions update

* Fri Sep 21 2007 Denis Leroy <denis@poolshark.org> - 2.20.0-1
- Update to new upstream stable 2.20

* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 2.18.0-1
- Update to Gnome 2.18, to follow libgnomeui version

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-2
- FE6 Rebuild

* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-1
- Update to 2.16.0

* Thu Mar 23 2006 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to 2.14.0

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.12.0-3
- Rebuild

* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-2
- Disabled static libraries

* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Update to 2.12.0

* Wed Apr 20 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Upgrade to 2.10.0. Removed x86_64 patch.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Jan 27 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.6.0-2
- Add autoreconf patch; fixes build on x86_64

* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.6.0-0.fdr.1
- Upgrade to 2.6.0

* Sat Nov 1  2003 Michael Koziarski <michael@koziarski.org> - 2.0.0-0.fdr.3
- Fix overly simplified dependencies

* Sat Nov 1  2003 Michael Koziarski <michael@koziarski.org> - 2.0.0-0.fdr.2
- setup -q
- simplify Dependencies

* Sat Oct 18 2003 Michael Koziarski <michael@koziarski.org> - 2.0.0-0.fdr.1
- Initial RPM creation
