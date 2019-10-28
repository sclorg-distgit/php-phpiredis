%global debug_package %{nil}

Name:           hiredis
Version:        0.13.3
Release:        0%{?dist}.1
Summary:        Minimalistic C client library for Redis
License:        BSD
URL:            https://github.com/redis/hiredis
Source0:        https://github.com/redis/hiredis/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/redis/hiredis/pull/554
Patch0:         0001-build-do-not-assume-that-INSTALL-is-cp.patch
BuildRequires:  gcc

%description 
Hiredis is a minimalistic C client library for the Redis database.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .pr554


%build
make %{?_smp_mflags} \
    PREFIX="%{_prefix}" \
    LIBRARY_PATH="%{_lib}"     \
    DEBUG="%{optflags}" \
    LDFLAGS="%{?__global_ldflags}"


%install
make install \
    DESTDIR=%{buildroot} \
    PREFIX="%{_prefix}" \
    LIBRARY_PATH="%{_lib}"

# Only keep the static library
rm %{buildroot}%{_libdir}/libhiredis.so*


%files
%doc COPYING

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/hiredis.pc
%{_libdir}/libhiredis.a

%changelog
* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 0.13.3-0.1
- rebuild

* Fri Feb 23 2018 Remi Collet <remi@remirepo.net> - 0.13.3-0
- only provides static library

* Mon Oct 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.3-6
- Fix FTBFS

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Christopher Meng <rpm@cicku.me> - 0.13.3-1
- Update to 0.13.3

* Thu Aug 27 2015 Christopher Meng <rpm@cicku.me> - 0.13.2-1
- Update to 0.13.2

* Fri Jul 31 2015 Christopher Meng <rpm@cicku.me> - 0.13.1-1
- Update to 0.13.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 0.12.1-2
- Bump for rebuild.

* Fri Jan 30 2015 Christopher Meng <rpm@cicku.me> - 0.12.1-1
- Update to 0.12.1

* Fri Jan 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.0-4
- Again build for f22-boost

* Fri Jan 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.0-3
- Once build on f22

* Tue Jan 27 2015 David Tardon <dtardon@redhat.com> - 0.12.0-2
- install all headers

* Fri Jan 23 2015 Christopher Meng <rpm@cicku.me> - 0.12.0-1
- Update to 0.12.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 29 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.11.0-1
- Updated to 0.11.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.1-3
- Removed Requires redis.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.1-1
- Updated to upstream 0.10.1-28-gd5d8843.

* Mon May 16 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.0-3
- Removed INSTALL_LIB from install target as we use INSTALL_LIBRARY_PATH.
- Use 'client library' in Summary.

* Wed May 11 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.0-2
- Updated devel sub-package description.
- Added optimization flags.
- Remove manual installation of shared objects.
- Use upstream .tar.gz sources.

* Tue May 10 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.0-1.gitdf203bc328
- Updated to upstream gitdf203bc328.
- Added TODO to the files.
- Updated to use libhiredis.so.0, libhiredis.so.0.10.

* Fri Apr 29 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.9.2-1
- First release.
