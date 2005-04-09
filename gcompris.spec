Summary:	Educational suite for kids 2-10 years old
Summary(pl):	Zestaw edukacyjny dla dzieci w wieku 2-10 lat
Name:		gcompris
Version:	6.4
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gcompris/%{name}-%{version}.tar.gz
# Source0-md5:	6e77dbe3fdaecd9d039695f59985b9c9
Patch0:		%{name}-info.patch
Patch1:		%{name}-python-lib.patch
Patch2:		%{name}-desktop.patch
URL:		http://gcompris.net/
BuildRequires:	SDL_mixer-devel
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
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel
BuildRequires:	texinfo
Requires:	assetml-flags
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

%description -l fr
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

%description -l pl
GCompris / Zrozumia³em to gra edukacyjna dla dzieci od 2 lat.
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

%package devel
Summary:        gcompris development package
Summary(pl):    Pliki dla programistów gcompris
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
gcompris development package.

%description devel -l pl
Pliki dla programistów gcompris.

%package -n assetml-voices-alphabet-da
Summary:        Alphabet voices in Danish
Summary(pl):    Wymowa alfabetu w jêzyku duñskim
Group:          X11/Applications/Games

%description -n assetml-voices-alphabet-da
Alphabet voices in Danish.

%description -n assetml-voices-alphabet-da -l pl
Wymowa alfabetu w jêzyku duñskim.

%package -n assetml-voices-colors-da
Summary:        Colors voices in Danish
Summary(pl):    Wymowa nazw kolorów w jêzyku duñskim
Group:          X11/Applications/Games 

%description -n assetml-voices-colors-da
Colors voices in Danish.

%description -n assetml-voices-colors-da -l pl
Wymowa nazw kolorów w jêzyku duñskim.

%package -n assetml-voices-geography-da
Summary:        Country name voices in Danish
Summary(pl):    Wymowa nazw pañstw w jêzyku duñskim
Group:          X11/Applications/Games

%description -n assetml-voices-geography-da
Country name voices in Danish.

%description -n assetml-voices-geography-da -l pl
Wymowa nazw pañstw w jêzyku duñskim.

%package -n assetml-voices-misc-da
Summary:        Miscelaneous voices in Danish
Summary(pl):    Wymowa ró¿nych s³ów w jêzyku duñskim
Group:          X11/Applications/Games

%description -n assetml-voices-misc-da
Miscelaneous voices in Danish.

%description -n assetml-voices-misc-da -l pl
Wymowa ró¿nych s³ów w jêzyku duñskim.

%package -n assetml-voices-alphabet-de
Summary:	Alphabet voices in German
Summary(pl):	Wymowa alfabetu w jêzyku niemieckim
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-de
Alphabet voices in German.

%description -n assetml-voices-alphabet-de -l pl
Wymowa alfabetu w jêzyku niemieckim.

%package -n assetml-voices-colors-de
Summary:	Colors voices in German
Summary(pl):	Wymowa nazw kolorów w jêzyku niemieckim
Group:		X11/Applications/Games

%description -n assetml-voices-colors-de
Colors voices in German.

%description -n assetml-voices-colors-de -l pl
Wymowa nazw kolorów w jêzyku niemieckim.

%package -n assetml-voices-geography-de
Summary:	Country name voices in German
Summary(pl):	Wymowa nazw pañstw w jêzyku niemieckim
Group:		X11/Applications/Games

%description -n assetml-voices-geography-de
Country name voices in German.

%description -n assetml-voices-geography-de -l pl
Wymowa nazw pañstw w jêzyku niemieckim.

%package -n assetml-voices-misc-de
Summary:	Miscelaneous voices in German
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku niemieckim
Group:		X11/Applications/Games

%description -n assetml-voices-misc-de
Miscelaneous voices in German.

%description -n assetml-voices-misc-de -l pl
Wymowa ró¿nych s³ów w jêzyku niemieckim.

%package -n assetml-voices-alphabet-en
Summary:	Alphabet voices in English
Summary(pl):	Wymowa alfabetu w jêzyku angielskim
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-en
Alphabet voices in English.

%description -n assetml-voices-alphabet-en -l pl
Wymowa alfabetu w jêzyku angielskim.

%package -n assetml-voices-colors-en
Summary:	Colors voices in English
Summary(pl):	Wymowa nazw kolorów w jêzyku angielskim
Group:		X11/Applications/Games

%description -n assetml-voices-colors-en
Colors voices in English.

%description -n assetml-voices-colors-en -l pl
Wymowa nazw kolorów w jêzyku angielskim.

%package -n assetml-voices-geography-en
Summary:	Country name voices in English
Summary(pl):	Wymowa nazw pañstw w jêzyku angielskim
Group:		X11/Applications/Games

%description -n assetml-voices-geography-en
Country name voices in English.

%description -n assetml-voices-geography-en -l pl
Wymowa nazw pañstw w jêzyku angielskim.

%package -n assetml-voices-misc-en
Summary:	Miscelaneous voices in English
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku angielskim
Group:		X11/Applications/Games

%description -n assetml-voices-misc-en
Miscelaneous voices in English.

%description -n assetml-voices-misc-en -l pl
Wymowa ró¿nych s³ów w jêzyku angielskim.

%package -n assetml-voices-alphabet-es
Summary:	Alphabet voices in Spanish
Summary(pl):	Wymowa alfabetu w jêzyku hiszpañskim
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-es
Alphabet voices in Spanish.

%description -n assetml-voices-alphabet-es -l pl
Wymowa alfabetu w jêzyku hiszpañskim.

%package -n assetml-voices-colors-es
Summary:	Colors voices in Spanish
Summary(pl):	Wymowa nazw kolorów w jêzyku hiszpañskim
Group:		X11/Applications/Games

%description -n assetml-voices-colors-es
Colors voices in Spanish.

%description -n assetml-voices-colors-es -l pl
Wymowa nazw kolorów w jêzyku hiszpañskim.

%package -n assetml-voices-geography-es
Summary:	Country name voices in Spanish
Summary(pl):	Wymowa nazw pañstw w jêzyku hiszpañskim
Group:		X11/Applications/Games

%description -n assetml-voices-geography-es
Country name voices in Spanish.

%description -n assetml-voices-geography-es -l pl
Wymowa nazw pañstw w jêzyku hiszpañskim.

%package -n assetml-voices-misc-es
Summary:	Miscelaneous voices in Spanish
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku hiszpañskim
Group:		X11/Applications/Games

%description -n assetml-voices-misc-es
Miscelaneous voices in Spanish

%description -n assetml-voices-misc-es -l pl
Wymowa ró¿nych s³ów w jêzyku hiszpañskim.

%package -n assetml-voices-alphabet-fr
Summary:	Alphabet voices in French
Summary(pl):	Wymowa alfabetu w jêzyku francuskim
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-fr
Alphabet voices in French.

%description -n assetml-voices-alphabet-fr -l pl
Wymowa alfabetu w jêzyku francuskim.

%package -n assetml-voices-colors-fr
Summary:	Colors voices in French
Summary(pl):	Wymowa nazw kolorów w jêzyku francuskim
Group:		X11/Applications/Games

%description -n assetml-voices-colors-fr
Colors voices in French.

%description -n assetml-voices-colors-fr -l pl
Wymowa nazw kolorów w jêzyku francuskim.

%package -n assetml-voices-geography-fr
Summary:	Country name voices in French
Summary(pl):	Wymowa nazw pañstw w jêzyku francuskim
Group:		X11/Applications/Games

%description -n assetml-voices-geography-fr
Country name voices in French.

%description -n assetml-voices-geography-fr -l pl
Wymowa nazw pañstw w jêzyku francuskim.

%package -n assetml-voices-misc-fr
Summary:	Miscelaneous voices in French
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku francuskim
Group:		X11/Applications/Games

%description -n assetml-voices-misc-fr
Miscelaneous voices in French.

%description -n assetml-voices-misc-fr -l pl
Wymowa ró¿nych s³ów w jêzyku francuskim.

%package -n assetml-voices-france_region-fr
Summary:	Region name voices in French
Summary(pl):	Wymowa nazw regionów w jêzyku francuskim
Group:		X11/Applications/Games

%description -n assetml-voices-france_region-fr
Region name voices in French.

%description -n assetml-voices-france_region-fr -l pl
Wymowa nazw regionów w jêzyku francuskim.

%package -n assetml-voices-alphabet-it
Summary:	Alphabet voices in Italian
Summary(pl):	Wymowa alfabetu w jêzyku w³oskim
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-it
Alphabet voices in Itaian.

%description -n assetml-voices-alphabet-it -l pl
Wymowa alfabetu w jêzyku w³oskim.

%package -n assetml-voices-colors-it
Summary:	Colors voices in Italian
Summary(pl):	Wymowa nazw kolorów w jêzyku w³oskim
Group:		X11/Applications/Games

%description -n assetml-voices-colors-it
Colors voices in Italian.

%description -n assetml-voices-colors-it -l pl
Wymowa nazw kolorów w jêzyku w³oskim.

%package -n assetml-voices-geography-it
Summary:	Country name voices in Italian
Summary(pl):	Wymowa nazw pañstw w jêzyku w³oskim
Group:		X11/Applications/Games

%description -n assetml-voices-geography-it
Country name voices in Italian.

%description -n assetml-voices-geography-it -l pl
Wymowa nazw pañstw w jêzyku w³oskim.

%package -n assetml-voices-misc-it
Summary:	Miscelaneous voices in Italian
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku w³oskim
Group:		X11/Applications/Games

%description -n assetml-voices-misc-it
Miscelaneous voices in Italian.

%description -n assetml-voices-misc-it -l pl
Wymowa ró¿nych s³ów w jêzyku w³oskim.

%package -n assetml-voices-alphabet-pt
Summary:	Alphabet voices in Portuguese
Summary(pl):	Wymowa alfabetu w jêzyku portugalskim
Group:		X11/Applications/Games

%description -n assetml-voices-alphabet-pt
Alphabet voices in Portuguese.

%description -n assetml-voices-alphabet-pt -l pl
Wymowa alfabetu w jêzyku portugalskim.

%package -n assetml-voices-colors-pt
Summary:	Colors voices in Portuguese
Summary(pl):	Wymowa nazw kolorów w jêzyku portugalskim
Group:		X11/Applications/Games

%description -n assetml-voices-colors-pt
Colors voices in Portuguese.

%description -n assetml-voices-colors-pt -l pl
Wymowa nazw kolorów w jêzyku portugalskim.

%package -n assetml-voices-geography-pt
Summary:	Country name voices in Portuguese
Summary(pl):	Wymowa nazw pañstw w jêzyku portugalskim
Group:		X11/Applications/Games

%description -n assetml-voices-geography-pt
Country name voices in Portuguese.

%description -n assetml-voices-geography-pt -l pl
Wymowa nazw pañstw w jêzyku portugalskim.

%package -n assetml-voices-misc-pt
Summary:	Miscelaneous voices in Portuguese
Summary(pl):	Wymowa ró¿nych s³ów w jêzyku portugalskim
Group:		X11/Applications/Games

%description -n assetml-voices-misc-pt
Miscelaneous voices in Portuguese.

%description -n assetml-voices-misc-pt -l pl
Wymowa ró¿nych s³ów w jêzyku portugalskim.

%package -n assetml-voices-alphabet-ru
Summary:        Alphabet voices in Russian
Summary(pl):    Wymowa alfabetu w jêzyku rosyjskim
Group:          X11/Applications/Games

%description -n assetml-voices-alphabet-ru
Alphabet voices in Russian.

%description -n assetml-voices-alphabet-ru -l pl
Wymowa alfabetu w jêzyku rosyjskim.

%package -n assetml-voices-colors-ru
Summary:        Colors voices in Russian
Summary(pl):    Wymowa nazw kolorów w jêzyku rosyjskim
Group:          X11/Applications/Games

%description -n assetml-voices-colors-ru
Colors voices in Russian.

%description -n assetml-voices-colors-ru -l pl
Wymowa nazw kolorów w jêzyku rosyjskim.

%package -n assetml-voices-geography-ru
Summary:        Country name voices in Russian
Summary(pl):    Wymowa nazw pañstw w jêzyku rosyjskim
Group:          X11/Applications/Games

%description -n assetml-voices-geography-ru
Country name voices in Russian.

%description -n assetml-voices-geography-pt -l ru
Wymowa nazw pañstw w jêzyku rosyjskim.

%package -n assetml-voices-misc-ru
Summary:        Miscelaneous voices in Russian
Summary(pl):    Wymowa ró¿nych s³ów w jêzyku rosyjskim
Group:          X11/Applications/Games

%description -n assetml-voices-misc-ru
Miscelaneous voices in Russian.

%description -n assetml-voices-misc-ru -l pl
Wymowa ró¿nych s³ów w jêzyku rosyjskim.

%package -n assetml-flags
Summary:	Country flags as 60x40 png files and an assetml description file
Summary(pl):	Flagi pañstw jako pliki png 60x40 oraz plik opisu assetml
Group:		X11/Applications/Games

%description -n assetml-flags
Contains png 60x40 country flags and an assetml description file.

%description -n assetml-flags -l pl
Pakiet zawiera flagi pañstw w formacie png 60x40 oraz plik opisu
assetml.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%dir %{_datadir}/gcompris
%dir %{_datadir}/gcompris/boards
%{_datadir}/gcompris/boards/[!fs]*
%{_datadir}/gcompris/boards/f[iu]*
%{_datadir}/gcompris/boards/s[ckmu]*
%dir %{_datadir}/gcompris/boards/sounds
%{_datadir}/gcompris/boards/sounds/*.ogg
%{_datadir}/gcompris/boards/sounds/chronos
%{_datadir}/gcompris/boards/sounds/melody
%{_datadir}/gcompris/python
%dir %{_datadir}/assetml
%{_desktopdir}/*
%{_infodir}/*.info*
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libgcompris-1.0
%{_pkgconfigdir}/*.pc

%files -n assetml-voices-alphabet-da
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/da/alphabet
%{_datadir}/assetml/gcompris_alphabet_da.assetml

%files -n assetml-voices-colors-da
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/da/colors
%{_datadir}/assetml/gcompris_colors_da.assetml

%files -n assetml-voices-geography-da
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/da/geography
%{_datadir}/assetml/gcompris_geography_da.assetml

%files -n assetml-voices-misc-da
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/da/misc
%{_datadir}/assetml/gcompris_misc_da.assetml

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

%files -n assetml-voices-france_region-fr
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/fr/france_region
%{_datadir}/assetml/gcompris_franceregion_fr.assetml

%files -n assetml-voices-alphabet-it
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/it/alphabet
%{_datadir}/assetml/gcompris_alphabet_it.assetml

%files -n assetml-voices-colors-it
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/it/colors
%{_datadir}/assetml/gcompris_colors_it.assetml

%files -n assetml-voices-geography-it
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/it/geography
%{_datadir}/assetml/gcompris_geography_it.assetml

%files -n assetml-voices-misc-it
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/it/misc
%{_datadir}/assetml/gcompris_misc_it.assetml

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

%files -n assetml-voices-alphabet-ru
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/ru/alphabet
%{_datadir}/assetml/gcompris_alphabet_ru.assetml

%files -n assetml-voices-colors-ru
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/ru/colors
%{_datadir}/assetml/gcompris_colors_ru.assetml

%files -n assetml-voices-geography-ru
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/ru/geography
%{_datadir}/assetml/gcompris_geography_ru.assetml

%files -n assetml-voices-misc-ru
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/sounds/ru/misc
%{_datadir}/assetml/gcompris_misc_ru.assetml

%files -n assetml-flags
%defattr(644,root,root,755)
%{_datadir}/gcompris/boards/flags
%{_datadir}/assetml/gcompris_flags.assetml
