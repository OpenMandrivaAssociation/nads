%define	name	nads
%define	version	0.3
%define	release	4

%define	major	0
%define libname	%mklibname nads %{major}
%define develname %mklibname -d nads

Summary:	Normalized Attack Detection System
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
URL:		http://www.scaramanga.co.uk
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Group:		System/Servers
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
N.A.D.S. is an HTTP URL normalization library. It takes HTTP URIs
in any form and converts them to a form suitable for comparison,
or for matching against attack descriptions (signatures) in
intrusion detection / prevention systems.

%package -n	%{libname}
Summary:	Normalized Attack Detection System library
Group:          System/Libraries

%description -n	%{libname}
N.A.D.S. is an HTTP URL normalization library. It takes HTTP URIs
in any form and converts them to a form suitable for comparison,
or for matching against attack descriptions (signatures) in
intrusion detection / prevention systems.

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Provides:	lib%{name}-devel
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname -d nads 0

%description -n	%{develname}
N.A.D.S. is an HTTP URL normalization library. It takes HTTP URIs
in any form and converts them to a form suitable for comparison,
or for matching against attack descriptions (signatures) in
intrusion detection / prevention systems.

This package contains the static %{name} library and its header
files.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x \
    --enable-static \
    --enable-shared
%make LIBTOOL=%{_bindir}/libtool

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/nads
%{_bindir}/testnads

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
