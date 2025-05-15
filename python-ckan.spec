# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-ckan
Epoch: 100
Version: 2.12.0~alpha0+20250829.89107b26
Release: 1%{?dist}
BuildArch: noarch
Summary: CKAN Software
License: BSD-3-Clause
URL: https://github.com/ckan/ckan/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-setuptools

%description
CKAN makes it easy to publish, share and work with data. It's a data
management system that provides a powerful platform for cataloging,
storing and accessing datasets with a rich front-end, full API (for both
data and catalog), visualization tools and more.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ckan
Summary: CKAN Software
Requires: python3
Requires: python3-alembic >= 1.16.1
Requires: python3-babel >= 2.17.0
Requires: python3-bleach >= 6.2.0
Requires: python3-blinker >= 1.9.0
Requires: python3-certifi >= 2025.01.31
Requires: python3-click >= 8.1.8
Requires: python3-dominate >= 2.9.1
Requires: python3-feedgen >= 1.0.0
Requires: python3-flask >= 3.1.1
Requires: python3-flask-babel >= 4.0.0
Requires: python3-flask-login >= 0.6.3
Requires: python3-flask-session >= 0.8.0
Requires: python3-flask-wtf >= 1.2.2
Requires: python3-jinja2 >= 3.1.6
Requires: python3-legacy-cgi
Requires: python3-markdown >= 3.8
Requires: python3-msgspec >= 0.19.0
Requires: python3-packaging >= 25.0
Requires: python3-passlib >= 1.7.4
Requires: python3-polib >= 1.2.0
Requires: python3-psycopg2 >= 2.9.10
Requires: python3-pyjwt >= 2.10.1
Requires: python3-pyparsing >= 3.2.3
Requires: python3-pysolr >= 3.10.0
Requires: python3-python-dateutil >= 2.9.0.post0
Requires: python3-python-magic >= 0.4.27
Requires: python3-pytz
Requires: python3-pyyaml >= 6.0.2
Requires: python3-requests >= 2.32.4
Requires: python3-rq >= 2.3.3
Requires: python3-simplejson >= 3.20.1
Requires: python3-sqlalchemy >= 2.0.41
Requires: python3-sqlparse >= 0.5.3
Requires: python3-typing-extensions >= 4.14.0
Requires: python3-tzlocal >= 5.3.1
Requires: python3-webassets >= 2.0
Requires: python3-werkzeug >= 3.1.3
Requires: python3-zope.interface >= 7.2
Provides: python3-ckan = %{epoch}:%{version}-%{release}
Provides: python3dist(ckan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ckan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ckan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ckan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ckan) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ckan
CKAN makes it easy to publish, share and work with data. It's a data
management system that provides a powerful platform for cataloging,
storing and accessing datasets with a rich front-end, full API (for both
data and catalog), visualization tools and more.

%files -n python%{python3_version_nodots}-ckan
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-ckan
Summary: CKAN Software
Requires: python3
Requires: python3-alembic >= 1.16.1
Requires: python3-babel >= 2.17.0
Requires: python3-bleach >= 6.2.0
Requires: python3-blinker >= 1.9.0
Requires: python3-certifi >= 2025.01.31
Requires: python3-click >= 8.1.8
Requires: python3-dominate >= 2.9.1
Requires: python3-feedgen >= 1.0.0
Requires: python3-flask >= 3.1.1
Requires: python3-flask-babel >= 4.0.0
Requires: python3-flask-login >= 0.6.3
Requires: python3-flask-session >= 0.8.0
Requires: python3-flask-wtf >= 1.2.2
Requires: python3-jinja2 >= 3.1.6
Requires: python3-legacy-cgi
Requires: python3-markdown >= 3.8
Requires: python3-msgspec >= 0.19.0
Requires: python3-packaging >= 25.0
Requires: python3-passlib >= 1.7.4
Requires: python3-polib >= 1.2.0
Requires: python3-psycopg2 >= 2.9.10
Requires: python3-pyjwt >= 2.10.1
Requires: python3-pyparsing >= 3.2.3
Requires: python3-pysolr >= 3.10.0
Requires: python3-python-dateutil >= 2.9.0.post0
Requires: python3-python-magic >= 0.4.27
Requires: python3-pytz
Requires: python3-pyyaml >= 6.0.2
Requires: python3-requests >= 2.32.4
Requires: python3-rq >= 2.3.3
Requires: python3-simplejson >= 3.20.1
Requires: python3-sqlalchemy >= 2.0.41
Requires: python3-sqlparse >= 0.5.3
Requires: python3-typing-extensions >= 4.14.0
Requires: python3-tzlocal >= 5.3.1
Requires: python3-webassets >= 2.0
Requires: python3-werkzeug >= 3.1.3
Requires: python3-zope.interface >= 7.2
Provides: python3-ckan = %{epoch}:%{version}-%{release}
Provides: python3dist(ckan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ckan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ckan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ckan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ckan) = %{epoch}:%{version}-%{release}

%description -n python3-ckan
CKAN makes it easy to publish, share and work with data. It's a data
management system that provides a powerful platform for cataloging,
storing and accessing datasets with a rich front-end, full API (for both
data and catalog), visualization tools and more.

%files -n python3-ckan
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-ckan
Summary: CKAN Software
Requires: python3
Requires: python3-alembic >= 1.16.1
Requires: python3-babel >= 2.17.0
Requires: python3-bleach >= 6.2.0
Requires: python3-blinker >= 1.9.0
Requires: python3-certifi >= 2024.01.31
Requires: python3-click >= 8.1.8
Requires: python3-dominate >= 2.9.1
Requires: python3-feedgen >= 1.0.0
Requires: python3-flask >= 3.1.1
Requires: python3-flask-babel >= 4.0.0
Requires: python3-flask-login >= 0.6.3
Requires: python3-flask-session >= 0.8.0
Requires: python3-flask-wtf >= 1.2.2
Requires: python3-jinja2 >= 3.1.6
Requires: python3-legacy-cgi
Requires: python3-markdown >= 3.8
Requires: python3-msgspec >= 0.19.0
Requires: python3-packaging >= 25.0
Requires: python3-passlib >= 1.7.4
Requires: python3-polib >= 1.2.0
Requires: python3-psycopg2 >= 2.9.10
Requires: python3-pyjwt >= 2.10.1
Requires: python3-pyparsing >= 3.2.3
Requires: python3-pysolr >= 3.10.0
Requires: python3-python-dateutil >= 2.9.0.post0
Requires: python3-python-magic >= 0.4.27
Requires: python3-pytz
Requires: python3-pyyaml >= 6.0.2
Requires: python3-requests >= 2.32.4
Requires: python3-rq >= 2.3.3
Requires: python3-simplejson >= 3.20.1
Requires: python3-sqlalchemy >= 2.0.41
Requires: python3-sqlparse >= 0.5.3
Requires: python3-typing-extensions >= 4.14.0
Requires: python3-tzlocal >= 5.3.1
Requires: python3-webassets >= 2.0
Requires: python3-werkzeug >= 3.1.3
Requires: python3-zope.interface >= 7.2
Provides: python3-ckan = %{epoch}:%{version}-%{release}
Provides: python3dist(ckan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ckan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ckan) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ckan = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ckan) = %{epoch}:%{version}-%{release}

%description -n python3-ckan
CKAN makes it easy to publish, share and work with data. It's a data
management system that provides a powerful platform for cataloging,
storing and accessing datasets with a rich front-end, full API (for both
data and catalog), visualization tools and more.

%files -n python3-ckan
%license LICENSE.txt
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
