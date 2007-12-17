Summary:	Rute Users Tutorial and Exposition
Name:		rute
Version:	1.0.0
Release:	%mkrel 1

Source0:	%{name}.html.tar.bz2
Source1:	rute.menu

License:	Paul Sheer, <psheer@icon.co.za>. Published under Open Content license.
Group:		Books/Computer books
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

%post
%{update_menus}
 
%postun
%{clean_menus}

%files
%defattr(-,root,root,0755)
%doc *
%{_datadir}/applications/*.desktop
