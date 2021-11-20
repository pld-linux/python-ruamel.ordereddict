#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_with	python3	# CPython 3.2 module
%bcond_without	tests	# unit tests

%define		module		ruamel.ordereddict
Summary:	A version of dict that keeps keys in insertion resp. sorted order
Summary(pl.UTF-8):	Wersja słownika trzymająca klucze w kolejności wstawiania
Name:		python-%{module}
Version:	0.4.14
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel.ordereddict/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.ordereddict/%{module}-%{version}.tar.gz
# Source0-md5:	e0723a39e81fdf5d986d892dc5a94bb8
URL:		https://pypi.org/project/ruamel.ordereddict/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
# for dir
Requires:	python-ruamel.base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A version of dict that keeps keys in insertion resp. sorted order.

%description -l pl.UTF-8
Wersja słownika (dict) trzymająca klucze w kolejności wstawiania

%package -n python3-ruamel.ordereddict
Summary:	A version of dict that keeps keys in insertion resp. sorted order
Summary(pl.UTF-8):	Wersja słownika trzymająca klucze w kolejności wstawiania
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
# for dir
Requires:	python3-ruamel.base

%description -n python3-ruamel.ordereddict
A version of dict that keeps keys in insertion resp. sorted order.

%description -n python3-ruamel.ordereddict -l pl.UTF-8
Wersja słownika (dict) trzymająca klucze w kolejności wstawiania

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

touch $(echo build-2/lib.*/ruamel)/__init__.py
PYTHONPATH=$(readlink -f build-2/lib.*) \
%{__python} -m pytest test/test_{ordereddict,py2,py27}.py
%endif

%if %{with python3}
%py3_build

touch $(echo build-3/lib.*/ruamel)/__init__.py
PYTHONPATH=$(readlink -f build-3/lib.*) \
%{__python3} -m pytest test/test_{orderreddict,py3}.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitedir}/ruamel/ordereddict
%attr(755,root,root) %{py_sitedir}/_ordereddict.so
%{py_sitedir}/ruamel.ordereddict-%{version}-py*.egg-info
%{py_sitedir}/ruamel.ordereddict-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-ruamel.ordereddict
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitedir}/ruamel/ordereddict
%attr(755,root,root) %{py3_sitedir}/_ordereddict.cpython-*.so
%{py3_sitedir}/ruamel.ordereddict-%{version}-py*.egg-info
%{py3_sitedir}/ruamel.ordereddict-%{version}-py*-nspkg.pth
%endif
