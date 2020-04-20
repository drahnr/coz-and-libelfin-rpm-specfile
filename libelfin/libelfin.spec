Name: libelfin	
Version: 0.2
Release: %{?release}%{!?release:2}%{?dist}
Summary: libelfin	

Group: Development/Libraries
License: MIT
URL: https://github.com/aclements/libelfin	
Source0: https://github.com/aclements/libelfin/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: %{?scl_prefix}gcc, %{?scl_prefix}binutils, %{?scl_prefix}gcc-c++, sd

%description

%prep
%setup -n %{name}-%{version} -q

%build
make

%install

install -d %{buildroot}%{_prefix}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_libdir}/pkgconfig

PREFIX=%{buildroot}%{_prefix} make install
#mv %{buildroot}%{_prefix}/include/* %{buildroot}%{_includedir}/
if [ "lib"  != "%{_lib}" ] ; then 
	mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}/
fi
sd '%{buildroot}' '' %{buildroot}%{_libdir}/pkgconfig/*.pc

%files
%doc
%{_libdir}/libdwarf++.*
%{_libdir}/libelf++.*
%{_includedir}/libelfin/*
%{_libdir}/pkgconfig/*.pc


%changelog
