Summary:	Educational suite for kids 3-10 years old
Name:		gcompris
Version:	5.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gcompris/%{name}-%{version}.tar.gz
# Source0-md5:	93145ecf6cc4629afa3c0ed959793ee1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://ofset.sf.net/gcompris
BuildRequires:	gnuchess >= 5.00
BuildRequires:	libassetml-devel
BuildRequires:	libogg-devel
BuildRequires:	libxml2-devel
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libvorbis-devel
BuildRequires:	libao-devel
BuildRequires:	texinfo
BuildRequires:	python-gnome
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
Requires:	assetml-flags

%description
GCompris / I Have Understood is an educationnal game for children
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

%package -n assetml-voices-alphabet-de
Summary:	Alphabet voices in German
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-alphabet-de
Alphabet voices in German

%package -n assetml-voices-colors-de
Summary:	Colors voices in German
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-colors-de
Colors voices in German

%package -n assetml-voices-geography-de
Summary:	Country name voices in German
Group:		X11/Applications/Games
Version:	0.0

%description -n assetml-voices-geography-de
Country name voices in German

%package -n assetml-voices-misc-de
Summary:	Miscelaneous voices in German
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-misc-de
Miscelaneous voices in German


%package -n assetml-voices-alphabet-en
Summary:	Alphabet voices in English
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-alphabet-en
Alphabet voices in English

%package -n assetml-voices-colors-en
Summary:	Colors voices in English
Group:		X11/Applications/Games
Version:	1.1

%description -n assetml-voices-colors-en
Colors voices in English

%package -n assetml-voices-geography-en
Summary:	Country name voices in English
Group:		X11/Applications/Games
Version:	1.1

%description -n assetml-voices-geography-en
Country name voices in English

%package -n assetml-voices-misc-en
Summary:	Miscelaneous voices in English
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-misc-en
Miscelaneous voices in English


%package -n assetml-voices-alphabet-es
Summary:	Alphabet voices in Spanish
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-alphabet-es
Alphabet voices in Spanish

%package -n assetml-voices-colors-es
Summary:	Colors voices in Spanish
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-colors-es
Colors voices in Spanish

%package -n assetml-voices-geography-es
Summary:	Country name voices in Spanish
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-geography-es
Country name voices in Spanish

%package -n assetml-voices-misc-es
Summary:	Miscelaneous voices in Spanish
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-misc-es
Miscelaneous voices in Spanish


%package -n assetml-voices-alphabet-fr
Summary:	Alphabet voices in French
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-alphabet-fr
Alphabet voices in French

%package -n assetml-voices-colors-fr
Summary:	Colors voices in French
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-colors-fr
Colors voices in French

%package -n assetml-voices-geography-fr
Summary:	Country name voices in French
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-geography-fr
Country name voices in French

%package -n assetml-voices-misc-fr
Summary:	Miscelaneous voices in French
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-misc-fr
Miscelaneous voices in French


%package -n assetml-voices-alphabet-pt
Summary:	Alphabet voices in Portuguese
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-alphabet-pt
Alphabet voices in Portuguese

%package -n assetml-voices-colors-pt
Summary:	Colors voices in Portuguese
Group:		X11/Applications/Games
Version:	1.0

%description -n assetml-voices-colors-pt
Colors voices in Portuguese

%package -n assetml-voices-geography-pt
Summary:	Country name voices in Portuguese
Group:		X11/Applications/Games
Version:	1.1

%description -n assetml-voices-geography-pt
Country name voices in Portuguese

%package -n assetml-voices-misc-pt
Summary:	Miscelaneous voices in Portuguese
Group:		X11/Applications/Games
Version:	1.1

%description -n assetml-voices-misc-pt
Miscelaneous voices in Portuguese


%package -n assetml-flags
Summary:	Contains png 60x40 country flags and an assetml description file
Group:		X11/Applications/Games
Version:	1.1

%description -n assetml-flags
Contains png 60x40 country flags and an assetml description file

%prep
%setup -q

%build

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*
%dir %{_libdir}/%{name}
%dir %{_datadir}/gcompris
%dir %{_datadir}/gcompris/boards
%dir %{_datadir}/gcompris/boards/skins
%dir %{_datadir}/gcompris/boards/sounds
%{_datadir}/gcompris/boards/skins/*
%{_datadir}/gcompris/boards/[^fs]*
%{_datadir}/gcompris/boards/f[iu]*
%{_datadir}/gcompris/boards/s[cmu]*
%{_datadir}/gcompris/boards/sounds/*.ogg
%{_datadir}/gcompris/boards/sounds/melody/*.ogg
%{_datadir}/gcompris/boards/sounds/chronos/space/*.ogg
%{_datadir}/gcompris/boards/sounds/HOWTO_ENCODE
%{_desktopdir}/*
%{_infodir}/*
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
%{_datadir}/gcompris/boards/flags/*
%{_datadir}/assetml/gcompris_flags.assetml
