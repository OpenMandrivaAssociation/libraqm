%define api		0
%define libname		%mklibname raqm
%define develname	%mklibname raqm -d

Name:		libraqm
Version:	0.10.5
Release:	1
License:	MIT
Group:		System/Libraries
Summary:	A library for complex text layout 
URL:		https://github.com/HOST-Oman/libraqm
Source:		https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(fribidi)

%description
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package -n	%{libname}
Summary:	Complex Textlayout Library
Group:		System/Libraries

%description -n	%{libname}
Library that encapsulates the logic for complex
text layout and provides a convenient API.

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	raqm-devel = %{EVRD}

%description -n	%{develname}
Header files for development with %{name}.

%prep
%autosetup -n raqm-%{version} -p1

%build
%meson -Ddocs=true
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libraqm.so.%{api}.*

%files -n %{develname}
%doc AUTHORS NEWS README*
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc
%{_datadir}/gtk-doc/html/raqm
