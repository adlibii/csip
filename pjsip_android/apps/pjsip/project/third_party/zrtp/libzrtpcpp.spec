# Copyright (c) 2008, 2009 David Sugar, Tycho Softworks.
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.

Summary: A ccrtp extension for zrtp/Zfone support
Name: libzrtpcpp
Version: 1.4.6
Release: 0%{?dist}
License: GPLv3+
Group: Development/Libraries
URL: http://www.gnu.org/software/commoncpp/commoncpp.html
Source0: ftp://ftp.gnu.org/gnu/ccrtp/libzrtpcpp-%{PACKAGE_VERSION}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libccrtp-devel >= 1.5.0
BuildRequires: pkgconfig
BuildRequires: libstdc++-devel
BuildRequires: libopenssl-devel >= 0.9.8

%description
This library is a GPL licensed extension to the GNU RTP Stack (GNU ccrtp).
This extension offers a C++ implementation of Phil Zimmermann's ZRTP 
specification. The current release is based on 
draft-zimmermann-avt-zrtp-12.txt which is intended to become the
RFC. Phil's Zfone site provides more 
information, see http://zfoneproject.com/index.html

This implementation was tested to work with Phil's Zfone implementation
of the ZRTP spefication. 

Applications that use GNU ccrtp can use this library to use ZRTP and to
encrypt any RTP (not RTCP) communication. See the demo programs how to
use this.

This release supports the basic ZRTP features, it does not support
preshared specified in the draft. Also the specified Asterisk PBX mode
is not supported. 

%package
Group: System/Libraries
Summary: Runtime library for GNU ZRTP Stack
Requires: ccrtp >= 1.5.0
Requires: libopenssl >= 0.9.8

%package devel
Group: Development/Libraries
Summary: Headers and static link library for libzrtpcpp.
Requires: %{name} = %{version}-%{release}
Requires: libccrtp-devel >= 1.5.0
Requires: libopenssl-devel >= 0.9.8

%description 
This package contains the runtime library needed by applications that use 
the GNU ZRTP stack.

%description devel
This package provides the header files, link libraries, and
documentation for building applications that use libzrtpcpp.

%prep
%setup -q
%build

%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} INSTALL="install -p" install
%{__rm} %{buildroot}%{_libdir}/*.la
%{__rm} -rf %{buildroot}/%{_infodir} 

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS INSTALL ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libzrtpcpp/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sun Oct 11 2009 - Werner Dittmann <werner.dittmann@t-online.de>
- Fix multistream problem
- add DH2048 mode
- update cipher selection to match latest draft (15x)
- Test with zfone3 with Ping packet mode enabled
- some code cleanup

* Erd Jun 24 2009 - David Sugar <dyfet@gnutelephony.org>
- Spec updated per current Fedora & CentOS policies.
- Updated release 1.4.5 has all mandatory IETF interop requirements.

* Fri Jan 26 2009 - Werner Dittmann <werner.dittmann@t-online.de>
- Update to version 1.4.2 to support the latest ZRTP
  specification draft-zimmermann-avt-zrtp-12

* Fri Aug 22 2008 - David Sugar <dyfet@gnutelephony.org>
- Adapted for newer library naming conventions.

* Tue Dec 11 2007 - Werner Dittmann <werner.dittmann@t-online.de>
- this is the first spec file for version 1.x.x
- remove the .la file in devel package
- use default file atttribute instead of 755

* Sat Apr 18 2007 - Werner Dittmann <werner.dittmann@t-online.de>
- set version to 1.1.0
- GNU ZRTP is compatible with the latest Zfone Beta
  from April 2 2007