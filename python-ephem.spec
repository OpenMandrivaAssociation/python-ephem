%define name python-ephem
%define version 3.7.3.4
%define srcname pyephem
%define release %mkrel 1

Summary:	Scientific-grade astronomical computations for python
Name:		%{name}
Version:	%{version}
License:	LGPLv3
Group:		Development/Python
Release:	%{release}
Source:		http://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
URL:		http://rhodesmill.org/pyephem/
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	python-devel >= 2.5
Provides:	%{srcname} = %{version}

%description
PyEphem provides scientific-grade astronomical computations for the
Python programming language. Given a date and location on the Earth’s
surface, it can compute the positions of the Sun and Moon, of the
planets and their moons, and of any asteroids, comets, or earth
satellites whose orbital elements the user can provide. Additional
functions are provided to compute the angular separation between two
objects in the sky, to determine the constellation in which an object
lies, and to find the times at which an object rises, transits, and
sets on a particular day.

The numerical routines that lie behind PyEphem are those from the
wonderful XEphem astronomy application, whose author, Elwood Downey,
generously gave permission for us to use them as the basis for
PyEphem.


%files
%defattr(-,root,root,-)
%doc INSTALL COPYING LICENSE-GPL LICENSE-LGPL README 
%py_platsitedir/ephem
%py_platsitedir/%{srcname}-*



%prep
%setup -q -n %{srcname}-%{version}


%build


%install

%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}


%clean
%__rm -rf %{buildroot}
