%define		source_name gmpc-awn
Summary:	Avant Window Navigator Plugin
Name:		gmpc-plugin-awn
Version:	11.8.16
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{source_name}-%{version}.tar.gz
# Source0-md5:	ac3b898fc0be8f6f568441b84f651986
Patch0:		libdir.patch
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_AWN
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gmpc-devel >= 0.15.4.96
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Integrates GMPC with Avant Window Navigator.

%prep
%setup -qn %{source_name}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/awnplugin.so
