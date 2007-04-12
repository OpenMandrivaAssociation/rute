Summary:	Rute Users Tutorial and Exposition
Name:		rute
Version:	0.9.1
Release:	%mkrel 4

Source0:	rute.pdf
Source1:	rute.menu

License:	Paul Sheer, <psheer@icon.co.za>. Published under Open Content license.
Group:		Books/Computer books
BuildRoot:	%_tmppath/%name-%version-root
BuildArch:	noarch
URL:		http://home.shisas.co.za/rute/
Requires:	gv, locales-en, mandrake_desk
Obsoletes:	rute_pdf

%description
Rute is a beginners guide to Linux and Unix-like systems. It is designed as a
dependency consistent tutorial document. This means you can (and should) read
it from beginning to end in consecutive order. Rute also satisfies the
requirements for course notes for a Linux training course.

%prep

%build
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%install
cd $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
cp %{SOURCE0} .

mkdir -p $RPM_BUILD_ROOT/%{_menudir}
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_menudir}/%{name}
perl -pi -e 's,DOCDIR,%{_docdir}/%{name}-%{version}/,' $RPM_BUILD_ROOT/%{_menudir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
 
%postun
%{clean_menus}

%files
%defattr(-,root,root,0755)
%{_docdir}/%{name}-%{version}
%{_menudir}/*


