Summary:	Theme bundle for GNUstep to provide horizontal menus
Name:		WildMenus
Version:	0.06
Release:	1
License:	LGPL/GPL
Group:		X11/Libraries
Source0:	http://www.cc.utah.edu/~msh3/%{name}-%{version}.tgz
# Source0-md5:	cb6f669a8856c753c526f62827632693
BuildRequires:	gnustep-gui-devel >= 0.8.7
#BuildRequires:	gnustep-back-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
WildMenus is a theme bundle for GNUStep, loadable by settings in
UserDefaults.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System \

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%dir %{_prefix}/System/Library/Bundles/%{name}.themeEngine
%attr(755,root,root) %{_prefix}/System/Library/Bundles/%{name}.themeEngine/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/%{name}.themeEngine/Resources
#%{_prefix}/System/Library/Bundles/%{name}.themeEngine/Resources/*.tiff
%{_prefix}/System/Library/Bundles/%{name}.themeEngine/Resources/*.plist
