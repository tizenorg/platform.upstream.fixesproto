Name:           fixesproto
Version:        5.0
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

Requires:       xextproto

%description
%{summary}.

%prep
%setup -q

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs

%files
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
