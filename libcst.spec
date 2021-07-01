#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcst
Version  : 0.3.19
Release  : 2
URL      : https://files.pythonhosted.org/packages/72/56/52e396bc827303f56c92268ca06d989f71a7dfaca0c7276de2c8d1e24821/libcst-0.3.19.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/56/52e396bc827303f56c92268ca06d989f71a7dfaca0c7276de2c8d1e24821/libcst-0.3.19.tar.gz
Summary  : A concrete syntax tree with AST-like properties for Python 3.5, 3.6, 3.7 and 3.8 programs.
Group    : Development/Tools
License  : MIT
Requires: libcst-python = %{version}-%{release}
Requires: libcst-python3 = %{version}-%{release}
Requires: PyYAML
Requires: dataclasses
Requires: typing_extensions
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : dataclasses
BuildRequires : pip
BuildRequires : typing_inspect-python

%description
.. image:: docs/source/_static/logo/horizontal.svg
:width: 600 px
:alt: LibCST
A Concrete Syntax Tree (CST) parser and serializer library for Python

%package python
Summary: python components for the libcst package.
Group: Default
Requires: libcst-python3 = %{version}-%{release}

%description python
python components for the libcst package.


%package python3
Summary: python3 components for the libcst package.
Group: Default
Requires: python3-core
Provides: pypi(libcst)
Requires: pypi(pyyaml)
Requires: pypi(typing_extensions)
Requires: pypi(typing_inspect)

%description python3
python3 components for the libcst package.


%prep
%setup -q -n libcst-0.3.19
cd %{_builddir}/libcst-0.3.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622647004
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
