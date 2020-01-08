%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-vault
Version: 5.17.5
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Plasma Vault - a tool for encrypted storage
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NetworkManagerQt)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5SysGuard)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
Requires: cryfs

%description
Plasma Vault - a tool for encrypted storage.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_libdir}/qt5/plugins/kf5/kfileitemaction/plasmavaultfileitemaction.so
%{_libdir}/qt5/plugins/kf5/kded/plasmavault.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_vault.so
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.vault.desktop
%{_datadir}/metainfo/org.kde.plasma.vault.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault
