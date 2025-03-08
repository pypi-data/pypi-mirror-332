%global modname glue
%global srcname lscsoft-%{modname}
%global distname %{lua:name = string.gsub(rpm.expand("%{srcname}"), "[.-]", "_"); print(name)}

# -- srpm metadata ----------

Name:     python-%{srcname}
Summary:  The Grid LSC User Environment
Version:  4.1.0
Release:  1%{?dist}
Packager: Duncan Macleod <duncan.macleod@ligo.org>

License:  GPLv2+
Prefix:   %{_prefix}
Source0:  %pypi_source %distname
Url:      https://git.ligo.org/lscsoft/glue/

BuildArch: noarch

# -- requirements -----------

# static build requirements
%if 0%{?rhel} == 0 || 0%{?rhel} >= 9
BuildRequires: pyproject-rpm-macros
%endif

# build requirements
BuildRequires: python3-devel >= 3.6
BuildRequires: python3dist(pip)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(wheel)

# testing requirements
BuildRequires: python3dist(igwn-segments)
BuildRequires: python3dist(pytest)

%description
Glue (Grid LSC User Environment) is a suite of python modules and programs to
allow users to run LSC codes on the grid.

# -- python3 ----------------

%package -n python3-%{srcname}
Summary: Python %{python3_version} libraries for the Grid LSC User Environment
%description -n python3-%{srcname}
Glue (Grid LSC User Environment) is a suite of python modules and programs to
allow users to run LSC codes on the grid.
This package provides the Python %{python3_version} library.
%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

# -- build ------------------

%prep
%autosetup -n %{distname}-%{version}

# for RHEL < 10 (but not Fedora) create a setup.cfg because we have
# setuptools < 61 which can't read metadata from pyproject.toml
%if 0%{?rhel} && 0%{?rhel} < 10
cat > setup.cfg << SETUP_CFG
[metadata]
name = %{srcname}
version = %{version}
maintainer-email = %{packager}
description = %{summary}
license = %{license}
license_files = LICENSE
url = %{url}
[options]
packages = find:
python_requires = >=3.6
install_requires =
  igwn-segments
SETUP_CFG
%endif

%if %{undefined pyproject_wheel}
cat > setup.py << SETUP_PY
from setuptools import setup
setup()
SETUP_PY
%endif

%build
%if %{defined pyproject_wheel}
%pyproject_wheel
%else
%py3_build_wheel
%endif

%install
%if %{defined pyproject_install}
%pyproject_install
%else
%py3_install_wheel %{distname}-%{version}-*.whl
%endif

%check
%pytest --verbose -ra --pyargs glue.tests

# -- changelog --------------

%changelog
* Fri Mar 07 2025 Robert Bruntz <robert.bruntz@ligo.org> 4.1.0-1
- Removes unused/unnecessary requirements and makes changes related to changes in various packages, including tests; specifies new minimum version of setuptools (61.0.0); updates and modernizes packaging configuration

* Fri Mar 01 2024 Duncan Macleod <duncan.macleod@ligo.org> 4.0.0-1
- Update to 4.0.0
- Lots of library content, and all scripts, has been removed
- Removed lscsoft-glue-utils package
- Use pyproject-rpm-macros on EL9+, backport setup.{cfg,py} for older platforms

* Wed Jan 10 2024 Robert Bruntz <robert.bruntz@ligo.org> 3.0.2-1
- Remove P2/P3 transitional packages; update testing

* Sat Jan 22 2022 Robert Bruntz <robert.bruntz@ligo.org> 3.0.1-1
- Removed Python 2 support and lots of unused code, much cleanup of code base

* Fri Sep 11 2020 Ryan Fisher <ryan.fisher@ligo.org> 2.1.0-1
- Test release with deprecations.

* Fri Dec 6 2019 Duncan Macleod <duncan.macleod@ligo.org> 2.0.0-3
- Rename packages according to EPEL naming conventions

* Wed Feb 20 2019 Ryan Fisher <rpfisher@syr.edu>
- Major version update with many changes and removal of segments subpackage.

* Tue Jun 19 2018 Ryan Fisher <rpfisher@syr.edu>
- 1.59.2 removing old M2Crypto import hiding in LDBDWClient.py.

* Thu Jun 7 2018 Ryan Fisher <rpfisher@syr.edu>
- 1.59.1 adding more python 3 package generation.

* Tue Jun 5 2018 Ryan Fisher <rpfisher@syr.edu>
- Pre O-3 release with removal of old codes, more packaging changes, better testing and more Python 3 compatibility.

* Tue Mar 13 2018 Ryan Fisher <rpfisher@syr.edu>
- Pre O-3 release with packaging changes, better testing and more Python 3 compatibility.

* Tue Jun 13 2017 Ryan Fisher <rpfisher@syr.edu>
- Mid O2 release to include M2Crypto removal and Kipp packaging changes.

* Thu Apr 13 2017 Duncan Macleod <duncan.macleod@ligo.org>
- Switched dependency from M2Crypto -> pyOpenSSL.

* Fri Apr 7 2017 Ryan Fisher <ryan.fisher@ligo.org>
- Added install_requires for pip installations.

* Thu Apr 6 2017 Ryan Fisher <ryan.fisher@ligo.org>
- Cleaned up RPM and debian codes.

* Thu Apr 6 2017 Duncan Brown <duncan.brown@ligo.org>
- O2 mid-run updated release. Change sdist name for PyPi compatibility.

* Wed Jan 25 2017 Ryan Fisher <rpfisher@syr.edu>
- O2 mid-run updated release. Updated python 3 compatibility fix from Leo to fix Debian package build for lalsuite.  Various updates from Kipp.

* Wed Oct 19 2016 Ryan Fisher <rpfisher@syr.edu>
- ER10 updated release. Python 3 compatibility from Leo, various updates from Kipp.

* Tue Sep 13 2016 Ryan Fisher <rpfisher@syr.edu>
- ER10 release. (forgot to update this changelog for last several releases)

* Thu Jul 23 2015 Ryan Fisher <rpfisher@syr.edu>
- Pre-ER8 release, attempt 2.

* Wed Jul 22 2015 Ryan Fisher <rpfisher@syr.edu>
- Pre-ER8 release.

* Fri May 22 2015 Ryan Fisher <rpfisher@syr.edu>
- ER7 release.

* Wed Nov 19 2014 Ryan Fisher <rpfisher@syr.edu>
- ER6 pre-release bug fix for dmt files method of ligolw_segment_query.

* Thu Nov 13 2014 Ryan Fisher <rpfisher@syr.edu>
- ER6 pre-release.

* Tue May 6 2014 Ryan Fisher <rpfisher@syr.edu>
- Version update to match git tag.

* Tue May 6 2014 Ryan Fisher <rpfisher@syr.edu>
- Sub-version release to add datafind to debian package.

* Tue Dec 3  2013 Ryan Fisher <rpfisher@syr.edu>
- ER5 release.

* Tue Jul 2 2013 Ryan Fisher <rpfisher@syr.edu>
- ER4 release, matching spec file.

* Tue Jul 2 2013 Ryan Fisher <rpfisher@syr.edu>
- ER4 release.

* Thu Mar 7 2013 Ryan Fisher <rpfisher@syr.edu>
- Post ER3 release of glue for pegasus 4.2 transition, added new RFC Proxy
    support.

* Fri Mar 1 2013 Ryan Fisher <rpfisher@syr.edu>
- Post ER3 release of glue for pegasus 4.2 transition.

* Mon Nov 19 2012 Ryan Fisher <rpfisher@syr.edu>
- New Release of glue for ER3 with updates to ligolw and lal codes.

* Tue Sep 4 2012 Ryan Fisher <rpfisher@syr.edu>
- New Release of glue with upgrades and bugfixes to segment database infrastructure.

* Fri May 18 2012 Ryan Fisher <rpfisher@syr.edu>
- Bugfix release of 1.39 labelled 1.39.2.  Includes fix to ligolw for URL reading, and packaging fixes.

* Fri May 11 2012 Ryan Fisher <rpfisher@syr.edu>
- Bugfix release of 1.39 labelled 1.39.1

* Thu May 10 2012 Ryan Fisher <rpfisher@syr.edu>
- New release of glue to replace Apr 12 near-release.  This includes ligolw changes and updates for job submission over remote pools.

* Thu Apr 12 2012 Ryan Fisher <rpfisher@syr.edu>
- New release of glue with updates to ligolw library, including some bug fixes for ligowl_sqlite and ligolw_print.

* Wed Nov 16 2011 Ryan Fisher <rpfisher@syr.edu>
- New release of glue with glue-segments and glue-common split from glue, lvalerts, lars and gracedb removed.

* Mon Oct 10 2011 Ryan Fisher <rpfisher@syr.edu>
- New release of glue to fix build issues called 1.36.

* Fri Oct 7 2011 Ryan Fisher <rpfisher@syr.edu>
- New release of glue with Kipp's fixes to ligolw_sqlite bugs, Kipp's checksums added, and Peter and my change to the coalescing script for segment databases.

* Thu Sep 29 2011 Ryan Fisher <rpfisher@syr.edu>
- New release of glue with speedup to string to xml conversion and 10 digit gps fixes.

* Wed Sep 15 2010 Peter Couvares <pfcouvar@syr.edu>
- New release of glue with GEO publishing

* Thu Apr 22 2010 Duncan Brown <dabrown@physics.syr.edu>
- Third S6 release of glue

* Wed Nov 11 2009 Duncan Brown <dabrown@physics.syr.edu>
- Second S6 release of glue

* Mon Jul 27 2009 Duncan Brown <dabrown@physics.syr.edu>
- First S6 release of glue

* Wed Jul 01 2009 Duncan Brown <dabrown@physics.syr.edu>
- Pre S6 release of glue

* Wed Jun 24 2009 Duncan Brown <dabrown@physics.syr.edu>
- Post E14 release of glue

* Thu Jun 11 2009 Duncan Brown <dabrown@physics.syr.edu>
- Allow segment tools to see multiple ifos

* Wed Jun 10 2009 Duncan Brown <dabrown@physics.syr.edu>
- Restored LSCdataFindcheck and fixed debian control files

* Tue Jun 09 2009 Duncan Brown <dabrown@physics.syr.edu>
- Build for glue 1.19-1

* Tue Jun 24 2008 Ping Wei <piwei@syr.edu>
- Build for glue 1.18-1

* Thu Jun 19 2008 Duncan Brown <dabrown@physics.syr.edu>
- Build for glue 1.17

* Fri Nov 04 2005 Duncan Brown <dbrown@ligo.caltech.edu>
- Build for glue 1.6

* Tue Aug 23 2005 Duncan Brown <dbrown@ligo.caltech.edu>
- Initial build for glue 1.0
