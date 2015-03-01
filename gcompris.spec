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

%package data
Summary:	GCompris data files
Group:		Applications/Games
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description data
GCompris data files.

%package sound-af
Summary:	GCompris voices in Afrikaans
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-af
Voice samples for the GCompris games in Afrikaans.

%package sound-ar
Summary:	GCompris voices in Arabic (Tunisia)
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-ar
Voice samples for the GCompris games in Arabic (Tunisia).

%package sound-ast
Summary:	GCompris voices in Asturian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-ast
Voice samples for the GCompris games in Asturian.

%package sound-bg
Summary:	GCompris voices in Bulgarian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-bg
Voice samples for the GCompris games in Bulgarian.

%package sound-br
Summary:	GCompris voices in Breton
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-br
Voice samples for the GCompris games in Breton.

%package sound-cs
Summary:	GCompris voices in Tsjech
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-cs
Voice samples for the GCompris games in Tsjech.

%package sound-da
Summary:	GCompris voices in Danish
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-da
Voice samples for the GCompris games in Danish.

%package sound-de
Summary:	GCompris voices in German
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-de
Voice samples for the GCompris games in German.

%package sound-el
Summary:	GCompris voices in Greek
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-el
Voice samples for the GCompris games in Greek.

%package sound-en
Summary:	GCompris voices in English
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-en
Voice samples for the GCompris games in English.

%package sound-eo
Summary:	GCompris voices in Esperanto
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-eo
Voice samples for the GCompris games in Esperanto.

%package sound-es
Summary:	GCompris voices in Spanish
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-es
Voice samples for the GCompris games in Spanish.

%package sound-eu
Summary:	GCompris voices in Basque
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-eu
Voice samples for the GCompris games in Basque.

%package sound-fi
Summary:	GCompris voices in Finish
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-fi
Voice samples for the GCompris games in Finish.

%package sound-fr
Summary:	GCompris voices in French
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sound-fr
Voice samples for the GCompris games in French.

%package sound-gd
Summary:	GCompris voices in Scottish Gaelic
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-gd
Voice samples for the GCompris games in Scottish Gaelic.

%package sound-he
Summary:	GCompris voices in Hebrew
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-he
Voice samples for the GCompris games in Hebrew.

%package sound-hi
Summary:	GCompris voices in Hindi
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-hi
Voice samples for the GCompris games in Hindi.

%package sound-hu
Summary:	GCompris voices in Hungarian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-hu
Voice samples for the GCompris games in Hungarian.

%package sound-id
Summary:	GCompris voices in Indonesian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-id
Voice samples for the GCompris games in Indonesian.

%package sound-it
Summary:	GCompris voices in Italian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-it
Voice samples for the GCompris games in Italian.

%package sound-lt
Summary:	GCompris voices in Lithuanian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-lt
Voice samples for the GCompris games in Lithuanian.

%package sound-mr
Summary:	GCompris voices in Indian Marathi
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-mr
Voice samples for the GCompris games in Indian Marathi.

%package sound-nb
Summary:	GCompris voices in Norwegian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-nb
Voice samples for the GCompris games in Norwegian.

%package sound-nl
Summary:	GCompris voices in Dutch
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-nl
Voice samples for the GCompris games in Dutch.

%package sound-nn
Summary:	GCompris voices in Norwegian Nynorsk
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-nn
Voice samples for the GCompris games in Norwegian Nynorsk.

%package sound-pa
Summary:	GCompris voices in Punjabi
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-pa
Voice samples for the GCompris games in Punjabi.

%package sound-pt
Summary:	GCompris voices in Portuguese
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-pt
Voice samples for the GCompris games in Portuguese.

%package sound-ru
Summary:	GCompris voices in Russian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-ru
Voice samples for the GCompris games in Russian.

%package sound-sk
Summary:	GCompris voices in Slovak
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-sk
Voice samples for the GCompris games in Slovak.

%package sound-sl
Summary:	GCompris voices in Slovenian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-sl
Voice samples for the GCompris games in Slovenian.

%package sound-so
Summary:	GCompris voices in Somali
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-so
Voice samples for the GCompris games in Somali.

%package sound-sr
Summary:	GCompris voices in Serbian
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-sr
Voice samples for the GCompris games in Serbian.

%package sound-sv
Summary:	GCompris voices in Swedish
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-sv
Voice samples for the GCompris games in Swedish.

%package sound-th
Summary:	GCompris voices in Thai
Group:		Applications/Games
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-th
Voice samples for the GCompris games in Thai.

%package sound-tr
Summary:	GCompris voices in Turk
Group:		Applications/Games
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-tr
Voice samples for the GCompris games in Turk.

%package sound-ur
Summary:	GCompris voices in Urdu
Group:		Applications/Games
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-ur
Voice samples for the GCompris games in Urdu.

%package sound-zh_CN
Summary:	GCompris voices in Chinese, Simplified
Group:		Applications/Games
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description sound-zh_CN
Voice samples for the GCompris games in Chinese, Simplified.

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
