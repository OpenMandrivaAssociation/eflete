Summary:	EFL theme editor
Name:		eflete
Version:	1.19.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	https://download.enlightenment.org/rel/apps/eflete/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(efl)
BuildRequires:	efl

%description
Theme editor for enclightenment window manager.

%files
%doc README
%{_bindir}/eflete
%{_bindir}/eflete_exporter
%{_datadir}/%{name}/themes/default/template/images/*
%{_datadir}/%{name}/themes/default/template/sounds/*
%{_datadir}/%{name}/themes/default/template/edc/*
%{_datadir}/%{name}/themes/default/template/edj/default.edj
%{_datadir}/%{name}/themes/default/color/*
%{_datadir}/%{name}/themes/default//*.edj
%{_datadir}/%{name}/images/*
%{_datadir}/%{name}/layouts/*.edj
%{_datadir}/%{name}/sounds/*
%{_datadir}/%{name}/AUTHORS
%{_datadir}/applications/eflete.desktop
%{_datadir}/locale/*/*
%{_iconsdir}/eflete.svg

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build

%configure  	\
		--with-eolian-gen=/usr/bin/eolian_gen

%make_build


%install
%make_install


%find_lang %{name}
