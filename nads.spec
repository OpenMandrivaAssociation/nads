%define	major	0
%define libname	%mklibname nads %{major}
%define develname %mklibname -d nads

Summary:	Normalized Attack Detection System
Name:		nads
Version:	0.3
Release:	6
URL:		http://www.scaramanga.co.uk
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Group:		System/Servers
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool

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
Requires:	%{libname} = %{version}
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
    --disable-static \
    --enable-shared
%make LIBTOOL=%{_bindir}/libtool

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/nads
%{_bindir}/testnads

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-5mdv2011.0
+ Revision: 620430
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2010.0
+ Revision: 430145
- rebuild

* Fri Jul 25 2008 Funda Wang <fwang@mandriva.org> 0.3-3mdv2009.0
+ Revision: 249331
- new devel package policy
- fix building

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Andreas Hasenack <andreas@mandriva.com> 0.3-3mdv2007.0
+ Revision: 107999
- rebuild
- Import nads

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-2mdk
- rebuild

* Thu Nov 18 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3-1mdk
- initial mandrake package

