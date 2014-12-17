%global pkgname roboto
%global fontname google-roboto

Name: google-roboto-fonts
# No idea what version this is supposed to be. The last versioned tarball from
# http://developer.android.com/design/style/typography.html was version 1.2,
# so I will just continue using that version.
Version: 1.2
Release: 6%{?dist}
Summary: Google Roboto fonts

# Only the metainfo.xml files are CC0
License: ASL 2.0 and CC0
URL: https://www.google.com/fonts/specimen/Roboto
# Oh, yeah... Thank you for the predictable download URL, Google! And
# I really do not want versioned tarball, because I really love to play
# the "find if there has been a new release" game...
# Downloaded on: 2014-12-17
Source0: http://material-design.storage.googleapis.com/publish/v_2/material_ext_publish/0B08MbvYZK1iNZGNoWmJqVEhQYTQ/RobotoTTF.zip
Source1: 64-%{fontname}-condensed-fontconfig.conf
Source2: 64-%{fontname}-fontconfig.conf
Source3: %{fontname}-condensed.metainfo.xml
Source4: %{fontname}.metainfo.xml
Source5: LICENSE.txt

BuildArch: noarch

BuildRequires: fontpackages-devel

%global fontconf 64-%{fontname}

%description
Roboto is a sans-serif typeface family introduced with Android Ice Cream
Sandwich operating system. Google describes the font as "modern, yet
approachable" and "emotional".

%package -n %{fontname}-condensed-fonts
Summary: Google Roboto condensed fonts
Requires: %{fontname}-common = %{version}-%{release}

%description -n %{fontname}-condensed-fonts
Google Roboto condensed fonts.

%prep
%autosetup -c -n %{name}-%{version}

%build

%install
# install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

# install fontconfig files
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf
for fconf in %{fontconf}.conf %{fontconf}-condensed.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE3} %{SOURCE4} %{buildroot}%{_datadir}/appdata

# install license
install -m 0755 -d %{buildroot}%{_docdir}/%{fontname}-fonts \
                   %{buildroot}%{_docdir}/%{fontname}-condensed-fonts
install -m 0644 -p %{SOURCE5} %{buildroot}%{_docdir}/%{fontname}-fonts/LICENSE.txt
install -m 0644 -p %{SOURCE5} %{buildroot}%{_docdir}/%{fontname}-condensed-fonts/LICENSE.txt

%_font_pkg -f %{fontconf}.conf Roboto-*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%doc %{_docdir}/%{fontname}-fonts/LICENSE.txt

%_font_pkg -n condensed -f %{fontconf}-condensed.conf RobotoCondensed-*.ttf
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml
%doc %{_docdir}/%{fontname}-condensed-fonts/LICENSE.txt

%changelog
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
