# TODO:
# - make desktop file
#
Summary:	Gmencoder - front-end to mencoder
Summary(pl.UTF-8):   Gmencoder - nakładka na mencoder
Name:		gmencoder
Version:	0.1.0
Release:	0.2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gmencoder/%{name}-%{version}.tgz
# Source0-md5:	2b011c02f9a9cf3d94554a02d052c938
Patch0:		%{name}-mpeg2.patch
URL:		http://gmencoder.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmencoder is a gnome-2 front-end to mplayer/mencoder. It support much
of the output codecs as well as postprocesing, cropping, scale,
subtitles ripping, 1, 2 and 3 passes for encoding and a lot of more
options are planned.

%description -l pl.UTF-8
Gmencoder jest graficzna nakładką na mplayer/mencoder przygotowaną do
pracy w środowisku Gnome-2. Wspiera wiele kodeków, skalowanie obrazu,
wyciąganie napisów, 1-, 2- a także 3-przebiegową kompresję. Wiele
innych pomysłów czeka na implementację.

%prep
%setup -q
%patch0 -p1

%build
%{__sed} -i 's,PATH_MP=.*,PATH_MP=/usr/bin,' etc/gmencoder_opts

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install man/gmencoder.1 $RPM_BUILD_ROOT%{_mandir}/man1
install etc/gmencoder_opts $RPM_BUILD_ROOT%{_sysconfdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/gmencoder
