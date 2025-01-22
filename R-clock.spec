#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-clock
Version  : 0.7.2
Release  : 10
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/clock_0.7.2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/clock_0.7.2.tar.gz
Summary  : Date-Time Types and Tools
Group    : Development/Tools
License  : MIT
Requires: R-clock-lib = %{version}-%{release}
Requires: R-cli
Requires: R-cpp11
Requires: R-lifecycle
Requires: R-rlang
Requires: R-tzdb
Requires: R-vctrs
BuildRequires : R-cli
BuildRequires : R-cpp11
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : R-tzdb
BuildRequires : R-vctrs
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
using a new family of orthogonal date-time classes (durations, time
    points, zoned-times, and calendars) that partition responsibilities so
    that the complexities of time zones are only considered when they are

%package lib
Summary: lib components for the R-clock package.
Group: Libraries

%description lib
lib components for the R-clock package.


%prep
%setup -q -n clock
pushd ..
cp -a clock buildavx2
popd
pushd ..
cp -a clock buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737561746

%install
export SOURCE_DATE_EPOCH=1737561746
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/clock/DESCRIPTION
/usr/lib64/R/library/clock/INDEX
/usr/lib64/R/library/clock/LICENSE
/usr/lib64/R/library/clock/Meta/Rd.rds
/usr/lib64/R/library/clock/Meta/data.rds
/usr/lib64/R/library/clock/Meta/features.rds
/usr/lib64/R/library/clock/Meta/hsearch.rds
/usr/lib64/R/library/clock/Meta/links.rds
/usr/lib64/R/library/clock/Meta/nsInfo.rds
/usr/lib64/R/library/clock/Meta/package.rds
/usr/lib64/R/library/clock/Meta/vignette.rds
/usr/lib64/R/library/clock/NAMESPACE
/usr/lib64/R/library/clock/NEWS.md
/usr/lib64/R/library/clock/R/clock
/usr/lib64/R/library/clock/R/clock.rdb
/usr/lib64/R/library/clock/R/clock.rdx
/usr/lib64/R/library/clock/R/sysdata.rdb
/usr/lib64/R/library/clock/R/sysdata.rdx
/usr/lib64/R/library/clock/data/Rdata.rdb
/usr/lib64/R/library/clock/data/Rdata.rds
/usr/lib64/R/library/clock/data/Rdata.rdx
/usr/lib64/R/library/clock/doc/clock.R
/usr/lib64/R/library/clock/doc/clock.Rmd
/usr/lib64/R/library/clock/doc/clock.html
/usr/lib64/R/library/clock/doc/faq.R
/usr/lib64/R/library/clock/doc/faq.Rmd
/usr/lib64/R/library/clock/doc/faq.html
/usr/lib64/R/library/clock/doc/index.html
/usr/lib64/R/library/clock/doc/recipes.R
/usr/lib64/R/library/clock/doc/recipes.Rmd
/usr/lib64/R/library/clock/doc/recipes.html
/usr/lib64/R/library/clock/help/AnIndex
/usr/lib64/R/library/clock/help/aliases.rds
/usr/lib64/R/library/clock/help/clock.rdb
/usr/lib64/R/library/clock/help/clock.rdx
/usr/lib64/R/library/clock/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/clock/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/clock/help/figures/logo.png
/usr/lib64/R/library/clock/help/paths.rds
/usr/lib64/R/library/clock/html/00Index.html
/usr/lib64/R/library/clock/html/R.css
/usr/lib64/R/library/clock/tests/testthat.R
/usr/lib64/R/library/clock/tests/testthat/_snaps/arithmetic.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/calendar.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/clock-deprecated.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/clock-labels.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/clock-locale.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/date.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/duration.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/getters.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/gregorian-year-day.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/gregorian-year-month-day.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/gregorian-year-month-weekday.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/invalid.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/iso-year-week-day.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/naive-time.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/posixt.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/quarterly-year-quarter-day.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/sys-time.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/time-point.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/week-year-week-day.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/weekday.md
/usr/lib64/R/library/clock/tests/testthat/_snaps/zoned-time.md
/usr/lib64/R/library/clock/tests/testthat/helper-format.R
/usr/lib64/R/library/clock/tests/testthat/helper-os.R
/usr/lib64/R/library/clock/tests/testthat/test-arithmetic.R
/usr/lib64/R/library/clock/tests/testthat/test-calendar.R
/usr/lib64/R/library/clock/tests/testthat/test-clock-codes.R
/usr/lib64/R/library/clock/tests/testthat/test-clock-deprecated.R
/usr/lib64/R/library/clock/tests/testthat/test-clock-labels.R
/usr/lib64/R/library/clock/tests/testthat/test-clock-locale.R
/usr/lib64/R/library/clock/tests/testthat/test-date.R
/usr/lib64/R/library/clock/tests/testthat/test-duration.R
/usr/lib64/R/library/clock/tests/testthat/test-getters.R
/usr/lib64/R/library/clock/tests/testthat/test-gregorian-year-day.R
/usr/lib64/R/library/clock/tests/testthat/test-gregorian-year-month-day.R
/usr/lib64/R/library/clock/tests/testthat/test-gregorian-year-month-weekday.R
/usr/lib64/R/library/clock/tests/testthat/test-invalid.R
/usr/lib64/R/library/clock/tests/testthat/test-iso-year-week-day.R
/usr/lib64/R/library/clock/tests/testthat/test-naive-time.R
/usr/lib64/R/library/clock/tests/testthat/test-posixt.R
/usr/lib64/R/library/clock/tests/testthat/test-quarterly-year-quarter-day.R
/usr/lib64/R/library/clock/tests/testthat/test-sys-time.R
/usr/lib64/R/library/clock/tests/testthat/test-time-point.R
/usr/lib64/R/library/clock/tests/testthat/test-utils.R
/usr/lib64/R/library/clock/tests/testthat/test-week-year-week-day.R
/usr/lib64/R/library/clock/tests/testthat/test-weekday.R
/usr/lib64/R/library/clock/tests/testthat/test-zoned-time.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/clock/libs/clock.so
/V4/usr/lib64/R/library/clock/libs/clock.so
/usr/lib64/R/library/clock/libs/clock.so
