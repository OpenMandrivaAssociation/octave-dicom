%global octpkg dicom

Summary:	Digital communications in medicine (DICOM) file io for Octave
Name:		octave-dicom
Version:	0.5.1
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/dicom/
Source0:	https://downloads.sourceforge.net/octave/dicom-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.8.0
BuildRequires:  gdcm-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
File io for medical images and other data using Grassroots DICOM
(GDCM) library.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
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

