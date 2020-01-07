#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prometheus_client
Version  : 0.7.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/b3/23/41a5a24b502d35a4ad50a5bb7202a5e1d9a0364d0c12f56db3dbf7aca76d/prometheus_client-0.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b3/23/41a5a24b502d35a4ad50a5bb7202a5e1d9a0364d0c12f56db3dbf7aca76d/prometheus_client-0.7.1.tar.gz
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

%description python3
python3 components for the prometheus_client package.


%prep
%setup -q -n prometheus_client-0.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561041440
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
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
