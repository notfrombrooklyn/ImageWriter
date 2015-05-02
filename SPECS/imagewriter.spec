#
# spec file for package imagewriter
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define breq qt4-devel
%define backend udisks2
%define qmake /usr/bin/qmake-qt4
%define lrelease /usr/bin/lrelease-qt4
%define definedbackend USEUDISKS2

Name:           imagewriter
Version:        1.10.1420800585.134a9b3
Release:        0
Summary:        Utility for writing disk images to USB keys
License:        GPL-2.0
Group:          Hardware/Other
Url:            https://github.com/openSUSE/imagewriter
Source0:        imagewriter-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  %{breq} %{backend}
BuildRequires:  xz
Requires:       xdg-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A graphical utility for writing raw disk images & hybrid ISOs to USB keys.

%prep
%setup -q

%build
# Create qmake cache file for building and use optflags.
cat > .qmake.cache <<EOF
PREFIX=%{_prefix}
QMAKE_CXXFLAGS_RELEASE += "%{optflags} -DKIOSKHACK"
DEFINES=%{definedbackend}
EOF
%{qmake}
make

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/imagewriter
%{_datadir}/applications/imagewriter.desktop
%{_datadir}/icons/hicolor/*/apps/imagewriter.*
%{_mandir}/man1/imagewriter.1%{?ext_man}
