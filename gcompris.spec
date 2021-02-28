#
# Conditional build:
%bcond_without	gnet	# build without gnet support (disallow GCompris fetch content from a web server)
%bcond_with	info	# build info doc

Summary:	Educational suite for kids 2-10 years old
Summary(pl.UTF-8):	Zestaw edukacyjny dla dzieci w wieku 2-10 lat
Name:		gcompris
Version:	11.09
Release:	2
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://downloads.sourceforge.net/gcompris/%{name}-%{version}.tar.gz
# Source0-md5:	b0066d5e0bb4e2fbb7380f723b51c598
Patch0:		%{name}-info.patch
Patch1:		%{name}-desktop.patch
URL:		https://gcompris.net/
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

%package data
Summary:	GCompris data files
Summary(pl.UTF-8):	Pliki danych GCompris
Group:		Applications/Games
BuildArch:	noarch

%description data
GCompris data files.

%description data -l pl.UTF-8
Pliki danych GCompris.

%package sound-af
Summary:	GCompris voices in Afrikaans
Summary(pl.UTF-8):	Głosy GCompris w języku afrykanerskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-af
Voice samples for the GCompris games in Afrikaans.

%description sound-af -l pl.UTF-8
Próbki głosów dla gier GCompris w języku afrykanerskim.

%package sound-ar
Summary:	GCompris voices in Arabic (Tunisia)
Summary(pl.UTF-8):	Głosy GCompris w języku arabskim (dla Tunezji)
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-ar
Voice samples for the GCompris games in Arabic (Tunisia).

%description sound-ar -l pl.UTF-8
Próbki głosów dla gier GCompris w języku arabskim (dla Tunezji)

%package sound-ast
Summary:	GCompris voices in Asturian
Summary(pl.UTF-8):	Głosy GCompris w języku asturskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-ast
Voice samples for the GCompris games in Asturian.

%description sound-ast -l pl.UTF-8
Próbki głosów dla gier GCompris w języku asturskim.

%package sound-bg
Summary:	GCompris voices in Bulgarian
Summary(pl.UTF-8):	Głosy GCompris w języku bułgarskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-bg
Voice samples for the GCompris games in Bulgarian.

%description sound-bg -l pl.UTF-8
Próbki głosów dla gier GCompris w języku bułgarskim.

%package sound-br
Summary:	GCompris voices in Breton
Summary(pl.UTF-8):	Głosy GCompris w języku bretońskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-br
Voice samples for the GCompris games in Breton.

%description sound-br -l pl.UTF-8
Próbki głosów dla gier GCompris w języku bretońskim.

%package sound-cs
Summary:	GCompris voices in Czech
Summary(pl.UTF-8):	Głosy GCompris w języku czeskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-cs
Voice samples for the GCompris games in Czech.

%description sound-cs -l pl.UTF-8
Próbki głosów dla gier GCompris w języku czeskim.

%package sound-da
Summary:	GCompris voices in Danish
Summary(pl.UTF-8):	Głosy GCompris w języku duńskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-da
Voice samples for the GCompris games in Danish.

%description sound-da -l pl.UTF-8
Próbki głosów dla gier GCompris w języku duńskim.

%package sound-de
Summary:	GCompris voices in German
Summary(pl.UTF-8):	Głosy GCompris w języku niemieckim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-de
Voice samples for the GCompris games in German.

%description sound-de -l pl.UTF-8
Próbki głosów dla gier GCompris w języku niemieckim.

%package sound-el
Summary:	GCompris voices in Greek
Summary(pl.UTF-8):	Głosy GCompris w języku greckim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-el
Voice samples for the GCompris games in Greek.

%description sound-el -l pl.UTF-8
Próbki głosów dla gier GCompris w języku greckim.

%package sound-en
Summary:	GCompris voices in English
Summary(pl.UTF-8):	Głosy GCompris w języku angielskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-en
Voice samples for the GCompris games in English.

%description sound-en -l pl.UTF-8
Próbki głosów dla gier GCompris w języku angielskim.

%package sound-eo
Summary:	GCompris voices in Esperanto
Summary(pl.UTF-8):	Głosy GCompris w języku esperanto
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-eo
Voice samples for the GCompris games in Esperanto.

%description sound-eo -l pl.UTF-8
Próbki głosów dla gier GCompris w języku esperanto.

%package sound-es
Summary:	GCompris voices in Spanish
Summary(pl.UTF-8):	Głosy GCompris w języku hiszpańskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-es
Voice samples for the GCompris games in Spanish.

%description sound-es -l pl.UTF-8
Próbki głosów dla gier GCompris w języku hiszpańskim.

%package sound-eu
Summary:	GCompris voices in Basque
Summary(pl.UTF-8):	Głosy GCompris w języku baskijskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-eu
Voice samples for the GCompris games in Basque.

%description sound-eu -l pl.UTF-8
Próbki głosów dla gier GCompris w języku baskijskim.

%package sound-fi
Summary:	GCompris voices in Finish
Summary(pl.UTF-8):	Głosy GCompris w języku fińskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-fi
Voice samples for the GCompris games in Finish.

%description sound-fi -l pl.UTF-8
Próbki głosów dla gier GCompris w języku fińskim.

%package sound-fr
Summary:	GCompris voices in French
Summary(pl.UTF-8):	Głosy GCompris w języku francuskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-fr
Voice samples for the GCompris games in French.

%description sound-fr -l pl.UTF-8
Próbki głosów dla gier GCompris w języku francuskim.

%package sound-gd
Summary:	GCompris voices in Scottish Gaelic
Summary(pl.UTF-8):	Głosy GCompris w języku szkockim gaelickim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-gd
Voice samples for the GCompris games in Scottish Gaelic.

%description sound-gd -l pl.UTF-8
Próbki głosów dla gier GCompris w języku szkockim gaelickim.

%package sound-he
Summary:	GCompris voices in Hebrew
Summary(pl.UTF-8):	Głosy GCompris w języku hebrajskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-he
Voice samples for the GCompris games in Hebrew.

%description sound-he -l pl.UTF-8
Próbki głosów dla gier GCompris w języku hebrajskim.

%package sound-hi
Summary:	GCompris voices in Hindi
Summary(pl.UTF-8):	Głosy GCompris w języku hindi
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-hi
Voice samples for the GCompris games in Hindi.

%description sound-hi -l pl.UTF-8
Próbki głosów dla gier GCompris w języku hindi.

%package sound-hu
Summary:	GCompris voices in Hungarian
Summary(pl.UTF-8):	Głosy GCompris w języku węgierskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-hu
Voice samples for the GCompris games in Hungarian.

%description sound-hu -l pl.UTF-8
Próbki głosów dla gier GCompris w języku węgierskim.

%package sound-id
Summary:	GCompris voices in Indonesian
Summary(pl.UTF-8):	Głosy GCompris w języku indonezyjskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-id
Voice samples for the GCompris games in Indonesian.

%description sound-id -l pl.UTF-8
Próbki głosów dla gier GCompris w języku indonezyjskim.

%package sound-it
Summary:	GCompris voices in Italian
Summary(pl.UTF-8):	Głosy GCompris w języku włoskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-it
Voice samples for the GCompris games in Italian.

%description sound-it -l pl.UTF-8
Próbki głosów dla gier GCompris w języku włoskim.

%package sound-lt
Summary:	GCompris voices in Lithuanian
Summary(pl.UTF-8):	Głosy GCompris w języku litewskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-lt
Voice samples for the GCompris games in Lithuanian.

%description sound-lt -l pl.UTF-8
Próbki głosów dla gier GCompris w języku litewskim.

%package sound-mr
Summary:	GCompris voices in Indian Marathi
Summary(pl.UTF-8):	Głosy GCompris w indyjskim języku marathi
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-mr
Voice samples for the GCompris games in Indian Marathi.

%description sound-mr -l pl.UTF-8
Próbki głosów dla gier GCompris w indyjskim języku marathi.

%package sound-nb
Summary:	GCompris voices in Norwegian Bokmaal
Summary(pl.UTF-8):	Głosy GCompris w języku norweskim bokmaal
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-nb
Voice samples for the GCompris games in Norwegian Bokmaal.

%description sound-nb -l pl.UTF-8
Próbki głosów dla gier GCompris w języku norweskim bokmaal.

%package sound-nl
Summary:	GCompris voices in Dutch
Summary(pl.UTF-8):	Głosy GCompris w języku holenderskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-nl
Voice samples for the GCompris games in Dutch.

%description sound-nl -l pl.UTF-8
Próbki głosów dla gier GCompris w języku holenderskim.

%package sound-nn
Summary:	GCompris voices in Norwegian Nynorsk
Summary(pl.UTF-8):	Głosy GCompris w języku norweskim nynorsk
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-nn
Voice samples for the GCompris games in Norwegian Nynorsk.

%description sound-nn -l pl.UTF-8
Próbki głosów dla gier GCompris w języku norweskim nynorsk.

%package sound-pa
Summary:	GCompris voices in Punjabi
Summary(pl.UTF-8):	Głosy GCompris w języku pendżabskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-pa
Voice samples for the GCompris games in Punjabi.

%description sound-pa -l pl.UTF-8
Próbki głosów dla gier GCompris w języku pendżabskim.

%package sound-pt
Summary:	GCompris voices in Portuguese
Summary(pl.UTF-8):	Głosy GCompris w języku portugalskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-pt
Voice samples for the GCompris games in Portuguese.

%description sound-pt -l pl.UTF-8
Próbki głosów dla gier GCompris w języku portugalskim.

%package sound-ru
Summary:	GCompris voices in Russian
Summary(pl.UTF-8):	Głosy GCompris w języku rosyjskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-ru
Voice samples for the GCompris games in Russian.

%description sound-ru -l pl.UTF-8
Próbki głosów dla gier GCompris w języku rosyjskim.

%package sound-sk
Summary:	GCompris voices in Slovak
Summary(pl.UTF-8):	Głosy GCompris w języku słowackim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-sk
Voice samples for the GCompris games in Slovak.

%description sound-sk -l pl.UTF-8
Próbki głosów dla gier GCompris w języku słowackim.

%package sound-sl
Summary:	GCompris voices in Slovenian
Summary(pl.UTF-8):	Głosy GCompris w języku słoweńskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-sl
Voice samples for the GCompris games in Slovenian.

%description sound-sl -l pl.UTF-8
Próbki głosów dla gier GCompris w języku słoweńskim.

%package sound-so
Summary:	GCompris voices in Somali
Summary(pl.UTF-8):	Głosy GCompris w języku somalijskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-so
Voice samples for the GCompris games in Somali.

%description sound-so -l pl.UTF-8
Próbki głosów dla gier GCompris w języku somalijskim.

%package sound-sr
Summary:	GCompris voices in Serbian
Summary(pl.UTF-8):	Głosy GCompris w języku serbskim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-sr
Voice samples for the GCompris games in Serbian.

%description sound-sr -l pl.UTF-8
Próbki głosów dla gier GCompris w języku serbskim.

%package sound-sv
Summary:	GCompris voices in Swedish
Summary(pl.UTF-8):	Głosy GCompris w języku szwedzkim
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-sv
Voice samples for the GCompris games in Swedish.

%description sound-sv -l pl.UTF-8
Próbki głosów dla gier GCompris w języku szwedzkim.

%package sound-th
Summary:	GCompris voices in Thai
Summary(pl.UTF-8):	Głosy GCompris w języku tajskim
Group:		Applications/Games
BuildArch:	noarch

%description sound-th
Voice samples for the GCompris games in Thai.

%description sound-th -l pl.UTF-8
Próbki głosów dla gier GCompris w języku tajskim.

%package sound-tr
Summary:	GCompris voices in Turkish
Summary(pl.UTF-8):	Głosy GCompris w języku tureckim
Group:		Applications/Games
BuildArch:	noarch

%description sound-tr
Voice samples for the GCompris games in Turkish.

%description sound-tr -l pl.UTF-8
Próbki głosów dla gier GCompris w języku tureckim.

%package sound-ur
Summary:	GCompris voices in Urdu
Summary(pl.UTF-8):	Głosy GCompris w języku urdu
Group:		Applications/Games
BuildArch:	noarch

%description sound-ur
Voice samples for the GCompris games in Urdu.

%description sound-ur -l pl.UTF-8
Próbki głosów dla gier GCompris w języku urdu.

%package sound-zh_CN
Summary:	GCompris voices in Chinese, Simplified
Summary(pl.UTF-8):	Głosy GCompris w języku chińskim uproszczonym
Group:		Applications/Games
BuildArch:	noarch

%description sound-zh_CN
Voice samples for the GCompris games in Chinese, Simplified.

%description sound-zh_CN -l pl.UTF-8
Próbki głosów dla gier GCompris w języku chińskim uproszczonym.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's/-Werror -O2//' configure.ac
%{__sed} -i -e 's/-DG_DISABLE_DEPRECATED//' src/goocanvas/src/Makefile.am

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
%{__make} \
	%{!?with_info:INFO_DEPS=}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	%{!?with_info:INFO_DEPS=} \
	DESTDIR=$RPM_BUILD_ROOT

# replace fr with en one
%if %{with info}
cp -p docs/C/gcompris.info $RPM_BUILD_ROOT%{_infodir}/gcompris.info
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sr_ME

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with info}
%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.translators THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%{_desktopdir}/*.desktop
%{?with_info:%{_infodir}/*.info*}
# gcompris uses its own goocanvas libraries with some specific changes
%attr(755,root,root) %{_libdir}/gcompris/libgoocanvas.so.0
%attr(755,root,root) %{_libdir}/gcompris/libgoocanvas.so.0.0.0
%{_mandir}/man6/gcompris.*
%{_pixmapsdir}/*.png

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/gcompris
%{_datadir}/gcompris/boards
%exclude %{_datadir}/%{name}/boards/voices/*
%{_datadir}/gcompris/python

%files sound-af
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/af

%files sound-ar
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/ar

%files sound-ast
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/ast

%files sound-bg
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/bg

%files sound-br
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/br

%files sound-cs
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/cs

%files sound-da
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/da

%files sound-de
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/de

%files sound-el
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/el

%files sound-en
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/en

%files sound-eo
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/eo

%files sound-es
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/es

%files sound-eu
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/eu

%files sound-fi
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/fi

%files sound-fr
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/fr

#%files sound-gd
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/boards/voices/gd

%files sound-he
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/he

%files sound-hi
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/hi

%files sound-hu
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/hu

%files sound-id
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/id

%files sound-it
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/it

#%files sound-lt
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/boards/voices/lt

%files sound-mr
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/mr

%files sound-nb
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/nb

%files sound-nl
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/nl

%files sound-nn
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/nn

%files sound-pa
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/pa

%files sound-pt
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/pt
%{_datadir}/%{name}/boards/voices/pt_BR

%files sound-ru
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/ru

#%files sound-sk
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/boards/voices/sk

%files sound-sl
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/sl

%files sound-so
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/so

%files sound-sr
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/sr

%files sound-sv
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/sv

%files sound-th
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/th

%files sound-tr
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/tr

%files sound-ur
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/ur

%files sound-zh_CN
%defattr(644,root,root,755)
%{_datadir}/%{name}/boards/voices/zh_CN
