Summary:	Educational suite for kids 3-10 years old
Summary(pl):	Zestaw edukacyjny dla dzieci w wieku 3-10 lat
Name:		gcompris
Version:	5.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gcompris/%{name}-%{version}.tar.gz
# Source0-md5:	93145ecf6cc4629afa3c0ed959793ee1
Patch0:		%{name}-info.patch
Patch1:		%{name}-python-lib.patch
URL:		http://ofset.sf.net/gcompris/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libao-devel
BuildRequires:	libassetml-devel
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	popt-devel >= 1.5
BuildRequires:	python-gnome
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	texinfo
Requires:	assetml-flags
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCompris / I Have Understood is an educational game for children
starting at 3. Today several Boards are implemented:
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

The Game is included in the Gnome Desktop under the Game menu.

You should install it only if you have children using this computer.

%description -l fr
GCompris / J'ai Compris est un logiciel éducatif pour les enfants à
partir de 3 ans.

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

Le jeu est inclus dans le bureau Gnome sous le menu Jeux.

À installer si vous avez des enfants utilisant cet ordinateur.

%description -l pl
GCompris / Zrozumia³em to gra edukacyjna dla dzieci od 3 lat.
Aktualnie zaimplementowane jest kilka plansz:
- klikanie na zwierzêtach - nauka u¿ywania myszy/klikania
- wpisywanie spadaj±cych liter - nauka u¿ywania klawiatury
- spadaj±ce kostki
- spadaj±ce s³owa
- podstawowa algebra
- nauka czasu z zegarkiem analogowym
- uk³adanka ze s³ynnymi obrazami
- prowadzenie samolotu z ³apaniem coraz wiêkszej liczby chmur
- równowa¿enie wagi
- i wiele wiêcej...

Gra jest w³±czana do menu Gry na pulpicie GNOME.

Warto j± instalowaæ tylko je¶li mamy dzieci u¿ywaj±ce komputera.

%package -n assetml-voices-alphabet-de
Summary:	Alphabet voices in German
Summary(pl):	Wymowa alfabetu w jêzyku niemieckim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-de
Alphabet voices in German.

%description -n assetml-voices-alphabet-de -l pl
Wymowa alfabetu w jêzyku niemieckim.

%package -n assetml-voices-colors-de
Summary:	Colors voices in German
Summary(pl):	Wymowa nazw kolorów w jêzyku niemieckim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-colors-de
Colors voices in German.

%description -n assetml-voices-colors-de -l pl
Wymowa nazw kolorów w jêzyku niemieckim.

%package -n assetml-voices-geography-de
Summary:	Country name voices in German
Summary(pl):	Wymowa nazw pañstw w jêzyku niemieckim
Version:	0.0
Group:		X11/Applications/Games

%description -n assetml-voices-geography-de
Country name voices in German.

%description -n assetml-voices-geography-de -l pl
Wymowa nazw pañstw w jêzyku niemieckim.

%package -n assetml-voices-misc-de
Summary:	Miscelaneous voices in German
Summary(pl):	Wymowa ró¿nych s³ow w jêzyku niemieckim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-misc-de
Miscelaneous voices in German.

%description -n assetml-voices-misc-de -l pl
Wymowa ró¿nych s³ow w jêzyku niemieckim.

%package -n assetml-voices-alphabet-en
Summary:	Alphabet voices in English
Summary(pl):	Wymowa alfabetu w jêzyku angielskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-en
Alphabet voices in English.

%description -n assetml-voices-alphabet-en -l pl
Wymowa alfabetu w jêzyku angielskim.

%package -n assetml-voices-colors-en
Summary:	Colors voices in English
Summary(pl):	Wymowa nazw kolorów w jêzyku angielskim
Version:	1.1
Group:		X11/Applications/Games

%description -n assetml-voices-colors-en
Colors voices in English.

%description -n assetml-voices-colors-en -l pl
Wymowa nazw kolorów w jêzyku angielskim.

%package -n assetml-voices-geography-en
Summary:	Country name voices in English
Summary(pl):	Wymowa nazw pañstw w jêzyku angielskim
Version:	1.1
Group:		X11/Applications/Games

%description -n assetml-voices-geography-en
Country name voices in English.

%description -n assetml-voices-geography-en -l pl
Wymowa nazw pañstw w jêzyku angielskim.

%package -n assetml-voices-misc-en
Summary:	Miscelaneous voices in English
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku angielskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-misc-en
Miscelaneous voices in English.

%description -n assetml-voices-misc-en -l pl
Wymowa ró¿nych s³ów w jêzyku angielskim.

%package -n assetml-voices-alphabet-es
Summary:	Alphabet voices in Spanish
Summary(pl):	Wymowa alfabetu w jêzyku hiszpañskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-es
Alphabet voices in Spanish.

%description -n assetml-voices-alphabet-es -l pl
Wymowa alfabetu w jêzyku hiszpañskim.

%package -n assetml-voices-colors-es
Summary:	Colors voices in Spanish
Summary(pl):	Wymowa nazw kolorów w jêzyku hiszpañskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-colors-es
Colors voices in Spanish.

%description -n assetml-voices-colors-es -l pl
Wymowa nazw kolorów w jêzyku hiszpañskim.

%package -n assetml-voices-geography-es
Summary:	Country name voices in Spanish
Summary(pl):	Wymowa nazw pañstw w jêzyku hiszpañskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-geography-es
Country name voices in Spanish.

%description -n assetml-voices-geography-es -l pl
Wymowa nazw pañstw w jêzyku hiszpañskim.

%package -n assetml-voices-misc-es
Summary:	Miscelaneous voices in Spanish
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku hiszpañskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-misc-es
Miscelaneous voices in Spanish

%description -n assetml-voices-misc-es -l pl
Wymowa ró¿nych s³ów w jêzyku hiszpañskim.

%package -n assetml-voices-alphabet-fr
Summary:	Alphabet voices in French
Summary(pl):	Wymowa alfabetu w jêzyku francuskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-fr
Alphabet voices in French.

%description -n assetml-voices-alphabet-fr -l pl
Wymowa alfabetu w jêzyku francuskim.

%package -n assetml-voices-colors-fr
Summary:	Colors voices in French
Summary(pl):	Wymowa nazw kolorów w jêzyku francuskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-colors-fr
Colors voices in French.

%description -n assetml-voices-colors-fr -l pl
Wymowa nazw kolorów w jêzyku francuskim.

%package -n assetml-voices-geography-fr
Summary:	Country name voices in French
Summary(pl):	Wymowa nazw pañstw w jêzyku francuskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-geography-fr
Country name voices in French.

%description -n assetml-voices-geography-fr -l pl
Wymowa nazw pañstw w jêzyku francuskim.

%package -n assetml-voices-misc-fr
Summary:	Miscelaneous voices in French
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku francuskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-misc-fr
Miscelaneous voices in French.

%description -n assetml-voices-misc-fr -l pl
Wymowa ró¿nych s³ów w jêzyku francuskim.

%package -n assetml-voices-alphabet-pt
Summary:	Alphabet voices in Portuguese
Summary(pl):	Wymowa alfabetu w jêzyku portugalskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-pt
Alphabet voices in Portuguese.

%description -n assetml-voices-alphabet-pt -l pl
Wymowa alfabetu w jêzyku portugalskim.

%package -n assetml-voices-colors-pt
Summary:	Colors voices in Portuguese
Summary(pl):	Wymowa nazw kolorów w jêzyku portugalskim
Version:	1.0
Group:		X11/Applications/Games

%description -n assetml-voices-colors-pt
Colors voices in Portuguese.

%description -n assetml-voices-colors-pt -l pl
Wymowa nazw kolorów w jêzyku portugalskim.

%package -n assetml-voices-geography-pt
Summary:	Country name voices in Portuguese
Summary(pl):	Wymowa nazw pañstw w jêzyku portugalskim
Version:	1.1
Group:		X11/Applications/Games

%description -n assetml-voices-geography-pt
Country name voices in Portuguese.

%description -n assetml-voices-geography-pt -l pl
Wymowa nazw pañstw w jêzyku portugalskim.

%package -n assetml-voices-misc-pt
Summary:	Miscelaneous voices in Portuguese
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku portugalskim
Version:	1.1
Group:		X11/Applications/Games

%description -n assetml-voices-misc-pt
Miscelaneous voices in Portuguese.

%description -n assetml-voices-misc-pt -l pl
Wymowa ró¿nych s³ów w jêzyku portugalskim.

%package -n assetml-flags
Summary:	Country flags as 60x40 png files and an assetml description file
Summary(pl):	Flagi pañstw jako pliki png 60x40 oraz plik opisu assetml
Version:	1.1
Group:		X11/Applications/Games

%description -n assetml-flags
Contains png 60x40 country flags and an assetml description file.

%description -n assetml-flags -l pl
Pakiet zawiera flagi pañstw w formacie png 60x40 oraz plik opisu assetml.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GNUCHESS="/usr/bin/gnuchess"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_desktopdir}

# replace fr with en one
cp -f docs/C/gcompris.info $RPM_BUILD_ROOT%{_infodir}/gcompris.info

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/python
%dir %{_datadir}/gcompris
%dir %{_datadir}/gcompris/boards
%dir %{_datadir}/gcompris/boards/skins
%{_datadir}/gcompris/boards/skins/*
%{_datadir}/gcompris/boards/[!fs]*
%{_datadir}/gcompris/boards/f[iu]*
%{_datadir}/gcompris/boards/s[cmu]*
%dir %{_datadir}/gcompris/boards/sounds
%{_datadir}/gcompris/boards/sounds/*.ogg
%dir %{_datadir}/gcompris/boards/sounds/chronos
%dir %{_datadir}/gcompris/boards/sounds/chronos/space
%{_datadir}/gcompris/boards/sounds/chronos/space/*.ogg
%dir %{_datadir}/gcompris/boards/sounds/melody
%{_datadir}/gcompris/boards/sounds/melody/*.ogg
%{_datadir}/gcompris/boards/sounds/HOWTO_ENCODE
%dir %{_datadir}/assetml
%{_desktopdir}/*
%{_infodir}/*.info*
%{_pixmapsdir}/*.png

%files -n assetml-voices-alphabet-de
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/de/alphabet
%{_datadir}/assetml/gcompris_alphabet_de.assetml

%files -n assetml-voices-colors-de
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/de/colors
%{_datadir}/assetml/gcompris_colors_de.assetml

%files -n assetml-voices-geography-de
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/de/geography
%{_datadir}/assetml/gcompris_geography_de.assetml

%files -n assetml-voices-misc-de
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/de/misc
%{_datadir}/assetml/gcompris_misc_de.assetml

%files -n assetml-voices-alphabet-en
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/en/alphabet
%{_datadir}/assetml/gcompris_alphabet_en.assetml

%files -n assetml-voices-colors-en
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/en/colors
%{_datadir}/assetml/gcompris_colors_en.assetml

%files -n assetml-voices-geography-en
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/en/geography
%{_datadir}/assetml/gcompris_geography_en.assetml

%files -n assetml-voices-misc-en
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/en/misc
%{_datadir}/assetml/gcompris_misc_en.assetml

%files -n assetml-voices-alphabet-es
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/es/alphabet
%{_datadir}/assetml/gcompris_alphabet_es.assetml

%files -n assetml-voices-colors-es
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/es/colors
%{_datadir}/assetml/gcompris_colors_es.assetml

%files -n assetml-voices-geography-es
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/es/geography
%{_datadir}/assetml/gcompris_geography_es.assetml

%files -n assetml-voices-misc-es
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/es/misc
%{_datadir}/assetml/gcompris_misc_es.assetml

%files -n assetml-voices-alphabet-fr
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/fr/alphabet
%{_datadir}/assetml/gcompris_alphabet_fr.assetml

%files -n assetml-voices-colors-fr
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/fr/colors
%{_datadir}/assetml/gcompris_colors_fr.assetml

%files -n assetml-voices-geography-fr
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/fr/geography
%{_datadir}/assetml/gcompris_geography_fr.assetml

%files -n assetml-voices-misc-fr
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/fr/misc
%{_datadir}/assetml/gcompris_misc_fr.assetml

%files -n assetml-voices-alphabet-pt
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/pt/alphabet
%{_datadir}/assetml/gcompris_alphabet_pt.assetml

%files -n assetml-voices-colors-pt
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/pt/colors
%{_datadir}/assetml/gcompris_colors_pt.assetml

%files -n assetml-voices-geography-pt
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/pt/geography
%{_datadir}/assetml/gcompris_geography_pt.assetml

%files -n assetml-voices-misc-pt
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/pt/misc
%{_datadir}/assetml/gcompris_misc_pt.assetml

%files -n assetml-flags
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/flags
%{_datadir}/assetml/gcompris_flags.assetml
