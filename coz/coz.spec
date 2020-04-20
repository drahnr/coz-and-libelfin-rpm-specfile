Name: coz
Version: 0.2.2
Release: %{?release}%{!?release:2}%{?dist}
Summary: causal optimization profiler

Group: Development/Tools
License:  BSD-2-Clause
URL: https://github.com/drahnr/coz
Source0: https://github.com/drahnr/coz/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Requires: libelfin

BuildRequires: %{?scl_prefix}clang, %{?scl_prefix}binutils
BuildRequires: sd, fd-find
BuildRequires: python3-docutils

%description

%prep
rm -rf %{buildroot}
%setup -n %{name}-%{version} -q

%build
export CFLAGS="-fpermissive -DCCUTIL_THREAD_H=1"
export CXXFLAGS="${CFLAGS}"
export CC="clang"
export CXX="clang++"
DESTDIR=%{buildroot} PREFIX=%{_prefix} make

%install

install -d %{buildroot}%{_prefix}
install -d %{buildroot}%{_libdir}

export CFLAGS="-fpermissive -DCCUTIL_THREAD_H=1"
export CXXFLAGS="${CFLAGS}"
export CC="clang"
export CXX="clang++"
DESTDIR=%{buildroot} PREFIX=%{_prefix} make install
#mv %{buildroot}%{_prefix}/include/* %{buildroot}%{_includedir}/
mv %{buildroot}%{_prefix}/lib/%{name}-profiler/*.so* %{buildroot}%{_libdir}/
if [ "lib"  != "%{_lib}" ] ; then
	mv %{buildroot}%{_prefix}/lib/%{name}-profiler %{buildroot}%{_libdir}/
fi
sd '%{buildroot}' ' ' $(fd '.*\.cmake$' %{buildroot}%{_libdir}/coz-profiler)


%files
%doc %{_mandir}/man1/%{name}.1.gz
%{_libdir}/*.so*
%{_libdir}/%{name}-profiler/*.cmake
%{_includedir}/*
%{_bindir}/%{name}


%changelog
* Mon Apr 20 2020 Bernhard Schuster <bernhard@ahoi.io> - 0.2.2-2.fc31
- Initial release


