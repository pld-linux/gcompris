# TODO
# - error: gcompris-8.4.2-1: req /usr/share/locale/ar_TN/LC_MESSAGES not found
Summary:	Educational suite for kids 2-10 years old
Summary(pl.UTF-8):	Zestaw edukacyjny dla dzieci w wieku 2-10 lat
Name:		gcompris
Version:	8.4.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gcompris/%{name}-%{version}.tar.gz
# Source0-md5:	226508072c72c0d78a66e918ef82715d
Patch0:		%{name}-info.patch
Patch1:		%{name}-desktop.patch
URL:		http://gcompris.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gstreamer-devel
BuildRequires:	intltool
BuildRequires:	libao-devel
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-sqlite
BuildRequires:	sqlite3-devel
BuildRequires:	tetex
BuildRequires:	texinfo
Requires:	python-gnome-canvas
Requires:	python-modules
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
cp /usr/share/gettext/config.rpath .
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GNUCHESS="%{_bindir}/gnuchess"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# replace fr with en one
cp -f docs/C/gcompris.info $RPM_BUILD_ROOT%{_infodir}/gcompris.info

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%dir %{_datadir}/gcompris
%dir %{_datadir}/gcompris/boards
%{_datadir}/gcompris/boards/[!fs]*
%{_datadir}/gcompris/boards/f[iou]*
%{_datadir}/gcompris/boards/s[cekmu]*
%dir %{_datadir}/gcompris/boards/sounds
%{_datadir}/gcompris/boards/sounds/*.wav
%{_datadir}/gcompris/boards/flags
%{_datadir}/gcompris/boards/sounds/LuneRouge
%{_datadir}/gcompris/boards/sounds/chronos
%{_datadir}/gcompris/boards/sounds/melody
%{_datadir}/gcompris/boards/sounds/memory
%{_datadir}/gcompris/python
%{_desktopdir}/*.desktop
%{_infodir}/*.info*
%{_mandir}/man6/*.6*
%{_pixmapsdir}/*.png
