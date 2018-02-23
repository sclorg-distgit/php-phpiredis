# centos/sclo spec file for php-phpiredis, from:
#
# remirepo spec file for php-phpiredis
#
# Copyright (c) 2016-2018 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%if 0%{?scl:1}
%global sub_prefix %{scl_prefix}
%if "%{scl}" == "rh-php56"
%global sub_prefix sclo-php56-
%endif
%if "%{scl}" == "rh-php70"
%global sub_prefix sclo-php70-
%endif
%if "%{scl}" == "rh-php71"
%global sub_prefix sclo-php71-
%endif
%scl_package         php-phpiredis
%endif

%global gh_commit  981d455034a48bb19db39c578e9c16d889289b99
%global gh_short   %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner   nrk
%global gh_project phpiredis

%global pecl_name  phpiredis
%global ini_name   40-%{pecl_name}.ini

Name:           %{?sub_prefix}php-%{pecl_name}
Version:        1.0.0
Release:        1%{?dist}

Summary:        Client extension for Redis

Group:          Development/Languages
License:        BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{pecl_name}-%{version}-%{gh_short}.tar.gz

BuildRequires:  %{?scl_prefix}php-devel
BuildRequires:  %{?scl_prefix}php-pear
BuildRequires:  hiredis-devel >= 0.13.3

Requires:       %{?scl_prefix}php(zend-abi) = %{php_zend_api}
Requires:       %{?scl_prefix}php(api) = %{php_core_api}

%if "%{?scl_prefix}" != "%{?sub_prefix}"
Provides:       %{?scl_prefix}php-%{pecl_name}               = %{version}-%{release}
Provides:       %{?scl_prefix}php-%{pecl_name}%{?_isa}       = %{version}-%{release}
%endif

%if 0%{?fedora} < 20 && 0%{?rhel} < 7
# Filter private shared
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}
%endif


%description
Phpiredis is an extension for PHP 5.x and 7.x based on hiredis
that provides a simple and efficient client for Redis and a fast
incremental parser / serializer for the RESP protocol.


%prep
%setup -q -c
mv %{gh_project}-%{gh_commit} NTS

cd NTS
# Check extension version
ver=$(sed -n '/define PHP_PHPIREDIS_VERSION/{s/.* "//;s/".*$//;p}' php_phpiredis.h)
if test "$ver" != "%{version}%{?prever}%{?gh_date:-dev}"; then
   : Error: Upstream VERSION version is ${ver}, expecting %{version}%{?prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..

cat  << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF



%build
cd NTS
%{_bindir}/phpize
%configure --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}


%install
make -C NTS install INSTALL_ROOT=%{buildroot}

# install configuration
install -Dpm 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}


%check
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}


%files
%{!?_licensedir:%global license %%doc}
%license NTS/LICENSE
%doc NTS/README.md

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Fri Feb 23 2018 Remi Collet <remi@remirepo.net> - 1.0.0-1
- cleanup for SCLo build

* Tue Oct  3 2017 Remi Collet <remi@remirepo.net> - 1.0.0-6
- F27: release bump

* Tue Jul 18 2017 Remi Collet <remi@remirepo.net> - 1.0.0-3
- rebuild for PHP 7.2.0beta1 new API

* Thu Dec  1 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- rebuild with PHP 7.1.0 GA

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- update to 1.0.0 release

* Sun Nov 13 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.2.20160715gita64e3bf
- add minor fix for portability
- add full reflection for all functions
- open https://github.com/nrk/phpiredis/pull/53

* Sat Nov 12 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.20160715gita64e3bf
- Initial packaging of 1.0.0-dev

