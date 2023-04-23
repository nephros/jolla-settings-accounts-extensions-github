# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       jolla-settings-accounts-extensions-github

# >> macros
# << macros

Summary:    Extension plugin for GitHub accounts
Version:    0.1.5
Release:    0
Group:      Applications
License:    ASL 2.0
BuildArch:  noarch
URL:        https://github.com/nephros/%{name}
Source0:    %{name}-%{version}.tar.gz
Source100:  jolla-settings-accounts-extensions-github.yaml
Source101:  jolla-settings-accounts-extensions-github-rpmlintrc
Requires:   buteo-sync-plugins-social-github
Requires:   jolla-settings-accounts-extensions
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake
BuildRequires:  qml-rpm-macros
BuildRequires:  sailfish-svg2png

%description
${summary}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%post
# >> post
/usr/libexec/manage-groups add account-github || :
# << post

%postun
# >> postun
if [ "$1" -eq 0 ]; then
/usr/libexec/manage-groups remove account-github || :
fi
# << postun

%files
%defattr(-,root,root,-)
%{_datadir}/accounts/*/*
%{_datadir}/themes/sailfish-default/meegotouch/*/icons/*.png
%{_datadir}/icons/*/scalable/apps/*.svg
# >> files
# << files
