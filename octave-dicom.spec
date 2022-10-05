%global octpkg dicom

Summary:	Digital communications in medicine (DICOM) file io
Name:		octave-%{octpkg}
Version:	0.5.0
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel > 3.8.0
BuildRequires:	gdcm-devel

Requires:	octave(api) = %{octave_api}
Requires:	gdcm-devel

Requires(post): octave
Requires(postun): octave

%description
Digital communications in medicine (DICOM) file io. 

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
export CXXFLAGS="%{optflags} -I%{_includedir}/gdcm"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

