%define 	module	cmemcache
Summary:	Python extension for libmemcache written in C
Summary(pl.UTF-8):	Napisany w C moduł Pythona do libmemcache
Name:		python-%{module}
Version:	0.95
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://gijsbert.org/downloads/cmemcache/%{module}-%{version}.tar.bz2
# Source0-md5:	b4680c311201ee3c0456e123874a289b
URL:		http://gijsbert.org/cmemcache/
BuildRequires:	libmemcache-devel >= 1.2.2
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Written in C Python extension for libmemcache, the C API to memcached.
cmemcache API is the same as python-memcache, so it is easy to replace
python-memcache with cmemcache, and vice versa.

%description -l pl.UTF-8
Napisany w C moduł Pythona dla libmemcache - biblioteki będącej
interfejsem C do memcached. Interfejs jest taki sam jak dla
python-memcache, więc moduły mogą być stosowane zamiennie.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{pld_release}" != "ac"
%{py_sitedir}/TEMPLATE-*.egg-info
%endif
