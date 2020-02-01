# Conditional build:
%bcond_without	tests	# unit tests

%define		module		ruamel.ordereddict
Summary:	A version of dict that keeps keys in insertion resp. sorted order
Name:		python-%{module}
Version:	0.4.14
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ruamel.ordereddict/
Source0:	https://files.pythonhosted.org/packages/source/r/ruamel.ordereddict/%{module}-%{version}.tar.gz
# Source0-md5:	e0723a39e81fdf5d986d892dc5a94bb8
URL:		https://pypi.org/project/ruamel.ordereddict/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-modules
BuildRequires:	python-setuptools
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A version of dict that keeps keys in insertion resp. sorted order.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitedir}/ruamel/ordereddict
%attr(755,root,root) %{py_sitedir}/_ordereddict.so
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%{py_sitedir}/%{module}-%{version}-py*-nspkg.pth
