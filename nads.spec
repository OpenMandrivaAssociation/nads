%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Normalized Attack Detection System
Name:		nads
Version:	0.3
Release:	7
License:	GPLv2+
Group:		System/Servers
Url:		https://www.scaramanga.co.uk
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	libtool

%description
N.A.D.S. is an HTTP URL normalization library. It takes HTTP URIs
in any form and converts them to a form suitable for comparison,
or for matching against attack descriptions (signatures) in
intrusion detection / prevention systems.

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/nads
%{_bindir}/testnads

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Normalized Attack Detection System library
Group:		System/Libraries

%description -n %{libname}
N.A.D.S. is an HTTP URL normalization library. It takes HTTP URIs
in any form and converts them to a form suitable for comparison,
or for matching against attack descriptions (signatures) in
intrusion detection / prevention systems.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	lib%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
N.A.D.S. is an HTTP URL normalization library. It takes HTTP URIs
in any form and converts them to a form suitable for comparison,
or for matching against attack descriptions (signatures) in
intrusion detection / prevention systems.

This package contains the static %{name} library and its header
files.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib%{name}.so

#----------------------------------------------------------------------------

%prep
%setup -q
find . -name "Makefile*" -o -name "*.m4" -o -name "configure*" |xargs sed -i -e 's,configure.in,configure.ac,g'

%build
./autogen.sh
%configure2_5x \
	--disable-static \
	--enable-shared
%make LIBTOOL=%{_bindir}/libtool

%install
%makeinstall_std

