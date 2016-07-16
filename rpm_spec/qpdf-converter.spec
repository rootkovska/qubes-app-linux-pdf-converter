#
# This is the SPEC file for creating binary and source RPMs for the VMs.
#
#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2013  Joanna Rutkowska <joanna@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#

%{!?version: %define version %(cat version)}

Name:		qubes-pdf-converter
Version:	%{version}
Release:	1%{dist}
Summary:	The Qubes service for converting untrusted PDF files into trusted ones

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

Requires:	poppler-utils ImageMagick
Requires:	nautilus-python

%define _builddir %(pwd)

%description
The Qubes service for converting untrusted PDF files into trusted ones.

%prep
# we operate on the current directory, so no need to unpack anything

%build

%install
rm -rf $RPM_BUILD_ROOT
make install-vm DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib/qubes/qpdf-convert-client
/usr/lib/qubes/qpdf-convert-server
/usr/lib/qubes/qvm-convert-pdf.gnome
/usr/bin/qvm-convert-pdf
%attr(0644,root,root) /etc/qubes-rpc/qubes.PdfConvert
/usr/share/nautilus-python/extensions/qvm_convert_pdf_nautilus.py*
/usr/share/kde4/services/qvm-convert-pdf.desktop
