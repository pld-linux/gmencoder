Summary:	Gmencoder - front-end to mencoder
Summary(pl):	Gmencoder - nak³adka na mencoder
Name:		gmencoder
Version:	0.1.0
Release:	0.1
License:	GPL
Group:          X11/Applications/Multimedia
Source0:	http://mesh.dl.sourceforge.net/sourceforge/gmencoder/%{name}-%{version}.tgz
# Source0-md5:	2b011c02f9a9cf3d94554a02d052c938
URL:		http://gmencoder.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#BuildRequires:	??
Requires:	mplayer

%description
Gmencoder is a gnome-2 front-end to mplayer/mencoder. It support
much of the output codecs as well as postprocesing, cropping, 
scale, subtitles ripping, 1, 2 and 3 passes for encoding and 
a lot of more options are planned.

%description -l pl
Gmencoder jest graficzna nak³adk± na mplayer/mencoder 
przygotowan± do pracy w ¶rodowisku Gnome-2. Wspiera wiele 
kodeków, skalowanie obrazu, wyci±ganie napisów, 1, 2 a tak¿e
2 przebiegow± kompresjê. Wiele innych pomys³ów czeka na 
implementacjê.

%prep
%setup

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS man/gmencoder.1
%attr(755,root,root) %{_bindir}/%{name}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
