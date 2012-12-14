%define prefix %{_prefix}

Summary:	A filemanager for X
Name:		xwc
Version:	0.91.4patch1
Release:	20
License:	GPL
Group:		File tools
URL:		http://sourceforge.net/projects/xwc/
Source0:	http://study.haifa.ac.il/~mbaranov/%{name}-%{version}.tar.bz2
Source1:	http://study.haifa.ac.il/~mbaranov/fox-0.99.42.tar.bz2 
Source10:	%{name}.16.png
Source11:	%{name}.32.png
Source12:	%{name}.48.png
Patch0:		fox-0.99.42.patch.bz2
Patch1:		fox-0.99.42.patch2.bz2
Patch2:		fox-0.99.42.patch3.bz2
Patch3:		xwc-compile.patch.bz2
Patch4:		xwc-better-desktop.patch.bz2 
BuildRequires:	X11-devel

%description
X file manager for X11 written using the FOX toolkit.
It has Windows Commander or MS-Explorer
look and it's very fast and simple. The main features are: file associations,
mount/umount devices, directory tree for quick cd, change file attributes, auto
save registry, compressed archives view/creation/extraction, automatic
query/install/upgrade of rpm's, and much more.

Not required but strongly encouraged to get full use of default file
associations :
. ee for graphics
. xmms for audios
. smpeg-player for videos
. gnozip for compressed archives

rpm utility and text viewer are provided.

# Yes there is the FOX lib inside this spec file. Since xwc is the only
# software to use this lib, and since the xwc binary is not dynamically
# linked, this decision has been taken in accord with QA.


%prep
%setup -q -a 1
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%build
cd fox
autoconf      # patched configure.in
%configure --without-opengl
%make
cd ..

make CCFLAGS="$RPM_OPT_FLAGS -DHAVE_UNISTD_H=1 -DHAVE_SYS_PARAM_H=1 -DHAVE_DIRENT_H=1 -fpermissive"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/foxicons
mkdir -p %{buildroot}%{_libdir}/foxrc
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

make INSTALLDIR=%{buildroot}/usr drop

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}} 
install %{SOURCE10}  %{buildroot}/%{_miconsdir}/%{name}.png
install %{SOURCE11}  %{buildroot}/%{_iconsdir}/%{name}.png
install %{SOURCE12}  %{buildroot}/%{_liconsdir}/%{name}.png 

cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Name=XWC File Manger
Comment=A MS-Explorer-like File Manager for X
Icon=%{name}
Categories=X-MandrivaLinux-System-FileTools;System;
EOF

#rm dub README
rm -rfd %{buildroot}/usr/doc/xwc-0.91.4patch1
 
%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_libdir}/foxicons
%{_libdir}/foxrc
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

