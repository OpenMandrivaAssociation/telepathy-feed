Name:           telepathy-feed
Version:        0.13
Release:        %mkrel 3
Summary:        A Galago feed for Telepathy

Group:          Communications
License:        LGPL
URL:            http://telepathy.freedesktop.org/wiki
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  %{_lib}telepathy-devel
BuildRequires:  libgalago-devel


%description
A Galago feed for Telepathy

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_libdir}/galago/%{name}

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT


