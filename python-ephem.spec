%define srcname pyephem

Summary:	Scientific-grade astronomical computations for python

Name:		python-ephem
Version:	3.7.5.2
Release:	2
License:	LGPLv3
Group:		Development/Python
Source:		http://pypi.python.org/packages/source/p/pyephem/pyephem-%{version}.tar.gz
Patch0:		pyephem-3.7.3.4-libm-fix.patch
URL:		https://rhodesmill.org/pyephem/
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
%doc INSTALL COPYING LICENSE-GPL LICENSE-LGPL  
%{py_platsitedir}/ephem
%{py_platsitedir}/%{srcname}-*


%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1
find . -type f -exec chmod a+r {} \;

%build


%install
%__python setup.py install --root=%{buildroot}

