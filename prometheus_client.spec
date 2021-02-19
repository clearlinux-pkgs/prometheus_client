#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prometheus_client
Version  : 0.9.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/18/9a/958cc52225370c9c7f66f4cea04250923db683d70fb2f45ba6f5f96169be/prometheus_client-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/18/9a/958cc52225370c9c7f66f4cea04250923db683d70fb2f45ba6f5f96169be/prometheus_client-0.9.0.tar.gz
Summary  : Python client for the Prometheus monitoring system.
Group    : Development/Tools
License  : Apache-2.0
Requires: prometheus_client-python = %{version}-%{release}
Requires: prometheus_client-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Prometheus Python Client
The official Python 2 and 3 client for [Prometheus](http://prometheus.io).

%package python
Summary: python components for the prometheus_client package.
Group: Default
Requires: prometheus_client-python3 = %{version}-%{release}

%description python
python components for the prometheus_client package.


%package python3
Summary: python3 components for the prometheus_client package.
Group: Default
Requires: python3-core
Provides: pypi(prometheus_client)

%description python3
python3 components for the prometheus_client package.


%prep
%setup -q -n prometheus_client-0.9.0
cd %{_builddir}/prometheus_client-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605543464
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
