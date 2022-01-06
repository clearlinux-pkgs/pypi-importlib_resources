#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-importlib_resources
Version  : 5.4.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/b5/d8/51ace1c1ea6609c01c7f46ca2978e11821aa0efaaa7516002ef6df000731/importlib_resources-5.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/d8/51ace1c1ea6609c01c7f46ca2978e11821aa0efaaa7516002ef6df000731/importlib_resources-5.4.0.tar.gz
Summary  : Read resources from Python packages
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-importlib_resources-license = %{version}-%{release}
Requires: pypi-importlib_resources-python = %{version}-%{release}
Requires: pypi-importlib_resources-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: importlib_resources
Provides: importlib_resources-python
Provides: importlib_resources-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi(zipp)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/importlib_resources.svg
:target: `PyPI link`_

%package license
Summary: license components for the pypi-importlib_resources package.
Group: Default

%description license
license components for the pypi-importlib_resources package.


%package python
Summary: python components for the pypi-importlib_resources package.
Group: Default
Requires: pypi-importlib_resources-python3 = %{version}-%{release}

%description python
python components for the pypi-importlib_resources package.


%package python3
Summary: python3 components for the pypi-importlib_resources package.
Group: Default
Requires: python3-core
Provides: pypi(importlib_resources)
Requires: pypi(zipp)

%description python3
python3 components for the pypi-importlib_resources package.


%prep
%setup -q -n importlib_resources-5.4.0
cd %{_builddir}/importlib_resources-5.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641444873
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-importlib_resources
cp %{_builddir}/importlib_resources-5.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-importlib_resources/3cd2faf9a752b7838f4b6a634116c24cc3053415
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-importlib_resources/3cd2faf9a752b7838f4b6a634116c24cc3053415

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
