%{define} subver beta

Summary:	EFL theme editor
Name:		eflete
Version:	1.19.0
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/bindings/python/%{name}-%{version}-beta.tar.xz
BuildRequires:	pkgconfig(eo) >= 1.19.1
BuildRequires:	pkgconfig(efl) >= 1.19.1

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
%setup -q

%build

%configure  	\
		--with-eolian-gen=/usr/bin/eolian_gen

%make


%install
%makeinstall_std


%find_lang %{name}