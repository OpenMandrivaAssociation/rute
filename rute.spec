Summary:	Rute Users Tutorial and Exposition
Name:		rute
Version:	1.0.0
Release:	5

Source0:	%{name}.html.tar.bz2
Source1:	rute.menu

License:	Paul Sheer, <psheer@icon.co.za>. Published under Open Content license.
Group:		Books/Computer books
BuildRoot:	%_tmppath/%name-%version-root
BuildArch:	noarch
Requires:	xdg-utils
URL:		http://rute.2038bug.com
Obsoletes:	rute_pdf

%description
Rute is a beginners guide to Linux and Unix-like systems. It is designed as a
dependency consistent tutorial document. This means you can (and should) read
it from beginning to end in consecutive order. Rute also satisfies the
requirements for course notes for a Linux training course.

%prep
%setup -q -n %{name}

%build
rm -fr $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Beginners Guide to Linux
Comment=Rute Users Tutorial and Exposition
Exec=xdg-open %{_docdir}/%{name}/index.html
Icon=documentation_section
Type=Application
Categories=Documentation;System;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root,0755)
%doc *
%{_datadir}/applications/*.desktop


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-4mdv2010.0
+ Revision: 433599
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-3mdv2009.0
+ Revision: 242634
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jun 23 2007 Funda Wang <fundawang@mandriva.org> 1.0.0-1mdv2008.0
+ Revision: 43373
- Use xdg menu
  use xdg-open
- New version


* Thu Feb 08 2007 Lenny Cartier <lenny@mandriva.com> 0.9.1-4mdv2007.0
+ Revision: 117694
- Rebuild
- Import rute

