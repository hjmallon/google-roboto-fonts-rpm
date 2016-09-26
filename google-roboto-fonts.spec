%global pkgname roboto
%global srcname %{pkgname}-unhinted
%global fontname google-roboto
%global fontconf 64-%{fontname}

Name: google-roboto-fonts
Version: 2.134
Release: 1%{?dist}
Summary: Google Roboto fonts

# Only the metainfo.xml files are CC0
License: ASL 2.0 and CC0
URL: https://github.com/google/roboto
Source0: https://github.com/google/%{pkgname}/releases/download/v%{version}/%{srcname}.zip
Source1: https://raw.githubusercontent.com/google/%{pkgname}/v%{version}/LICENSE
Source2: %{fontconf}-condensed-fontconfig.conf
Source3: %{fontconf}-fontconfig.conf
Source4: %{fontname}-condensed.metainfo.xml
Source5: %{fontname}.metainfo.xml
BuildArch: noarch

BuildRequires: fontpackages-devel

Obsoletes: %{fontname}-common < 2.134-1

%description
Roboto is a sans-serif typeface family introduced with Android Ice Cream
Sandwich operating system. Google describes the font as "modern, yet
approachable" and "emotional".

%package -n %{fontname}-condensed-fonts
Summary: Google Roboto condensed fonts
Obsoletes: %{fontname}-common < 2.134-1

%description -n %{fontname}-condensed-fonts
Google Roboto condensed fonts.

%prep
%autosetup -n %{srcname}
cp -p %{SOURCE1} .

%build

%install
# install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Roboto*.ttf %{buildroot}%{_fontdir}

# install fontconfig files
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf
for fconf in %{fontconf}.conf %{fontconf}-condensed.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE4} %{SOURCE5} %{buildroot}%{_datadir}/appdata

%_font_pkg -f %{fontconf}.conf Roboto-*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%license LICENSE

%_font_pkg -n condensed -f %{fontconf}-condensed.conf RobotoCondensed-*.ttf
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml
%license LICENSE

%changelog
* Mon Sep 26 2016 David Tardon <dtardon@redhat.com> - 2.134-1
- update to latest release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 David Tardon <dtardon@redhat.com> - 1.2-8
- revert the previous "update"
- Resolves: rhbz#1174935 fix font metadata

* Tue Dec 23 2014 David Tardon <dtardon@redhat.com> - 1.2-7
- drop obsolete requires

* Wed Dec 17 2014 David Tardon <dtardon@redhat.com> - 1.2-6
- Resolves: rhbz#1174935 update to what is presumably the latest release
  of the font

* Mon Nov 24 2014 David Tardon <dtardon@redhat.com> - 1.2-5
- use just Roboto as the font's name in metainfo

* Thu Nov 20 2014 David Tardon <dtardon@redhat.com> - 1.2-4
- add AppData files

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 07 2014 David Tardon <dtardon@redhat.com> - 1.2-2
- integrate package review suggestions

* Thu Apr 03 2014 David Tardon <dtardon@redhat.com> - 1.2-1
- initial import
