#
# Conditional build:
%bcond_without	gnet	# build without gnet support (disallow GCompris fetch content from a web server)
#
Summary:	Educational suite for kids 2-10 years old
Summary(pl.UTF-8):	Zestaw edukacyjny dla dzieci w wieku 2-10 lat
Name:		gcompris
Version:	11.09
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/gcompris/%{name}-%{version}.tar.gz
# Source0-md5:	b0066d5e0bb4e2fbb7380f723b51c598
Patch0:		%{name}-info.patch
Patch1:		%{name}-desktop.patch
URL:		http://gcompris.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnet-devel
BuildRequires:	gnome-common
BuildRequires:	gstreamer-devel
BuildRequires:	intltool
BuildRequires:	libao-devel
BuildRequires:	libogg-devel
BuildRequires:	librsvg-devel >= 1:2.34.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	python-devel
BuildRequires:	python-pycairo-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	python-sqlite
BuildRequires:	sqlite3-devel
BuildRequires:	texi2html
BuildRequires:	texinfo
Requires:	gstreamer-audio-formats
Requires:	gstreamer-audiosink
Requires:	gstreamer-vorbis
Requires:	python-gnome-canvas
Requires:	python-modules
Requires:	python-sqlite
Suggests:	gnuchess
Suggests:	tuxpaint
Obsoletes:	gcompris-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCompris / I Have Understood is an educational game for children
starting at 2. Today several Boards are implemented:
- Click on the animals => learn the mouse/click usage
- Type the falling letters => learn the keyboard usage
- Falling Dices
- Falling words
- Basic algebra
- Time learning with an analog clock
- Puzzle game with famous paintings
- Drive Plane to catch clouds in increasing number
- Balance the scales
- And much more ...

The game is included in the GNOME desktop under the Game menu.

You should install it only if you have children using this computer.

%description -l fr.UTF-8
GCompris / J'ai Compris est un logiciel éducatif pour les enfants à
partir de 2 ans.

Aujourd'hui, plusieurs tableaux sont implémentés :
- Cliquer sur les animaux => apprentissage du click et de la souris
- Entrer les lettres qui tombent => Apprentissage du clavier
- Les dés qui tombent
- Les mots qui tombent
- Algèbre simple
- Apprentissage de la lecture de l'heure sur une horloge analogique
- Puzzle avec des tableaux célèbres
- Pilote un avion pour attraper les nuages dans l'ordre
- Equilibre la balance

Le jeu est inclus dans le bureau GNOME sous le menu Jeux.

À installer si vous avez des enfants utilisant cet ordinateur.

%description -l pl.UTF-8
GCompris / Zrozumiałem to gra edukacyjna dla dzieci od 2 lat.
Aktualnie zaimplementowane jest kilka plansz:
- klikanie na zwierzętach - nauka używania myszy/klikania
- wpisywanie spadających liter - nauka używania klawiatury
- spadające kostki
- spadające słowa
- podstawowa algebra
- nauka czasu z zegarkiem analogowym
- układanka ze słynnymi obrazami
- prowadzenie samolotu z łapaniem coraz większej liczby chmur
- równoważenie wagi
- i wiele więcej...

Gra jest włączana do menu Gry na pulpicie GNOME.

Warto ją instalować tylko jeśli mamy dzieci używające komputera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp %{_datadir}/gettext/config.rpath .
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GNUCHESS="%{_bindir}/gnuchess" \
	--%{!?with_gnet:dis}%{?with_gnet:en}able-gnet \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# replace fr with en one
cp -a docs/C/gcompris.info $RPM_BUILD_ROOT%{_infodir}/gcompris.info

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/sr_ME

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.translators THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%dir %{_datadir}/gcompris
%{_datadir}/gcompris/boards
%{_datadir}/gcompris/python
%{_desktopdir}/*.desktop
%{_infodir}/*.info*
# gcompris uses its own goocanvas libraries with some specific changes
%attr(755,root,root) %{_libdir}/gcompris/libgoocanvas.so.0
%attr(755,root,root) %{_libdir}/gcompris/libgoocanvas.so.0.0.0
%{_mandir}/man6/gcompris.*
%{_pixmapsdir}/*.png
