Summary:	Open Text Summarizer
Summary(pl):	Otwarte narzêdzie do streszczania tekstu
Name:		ots
Version:	0.4.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libots/%{name}-%{version}.tar.gz
# Source0-md5:	f5768210dfcb4c2afade80803877145c
URL:		http://libots.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk-doc >= 0.9
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
Requires:	glib2 >= 2.0
Requires:	libxml2 >= 2.4.23
Requires:	popt >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The open text summarizer is an open source tool for summarizing texts.
The program reads a text and decides which sentences are important and
which are not.

The program can either print the summarized text in text format or in
HTML form where the important sentences are highlighted in red. The
program is multi lingual and work with UTF-8 code; at the moment only
English and Hebrew are supported.

%description -l pl
OTS (Open Text Summarizer) to wolnodostêpne narzêdzie do streszczania
tekstów. Program czyta tekst i decyduje, które zdania s± wa¿ne, a
które nie.

Program mo¿e wypisaæ streszczenie w formacie tekstowym lub w postaci
HTML, gdzie wa¿ne zdania s± oznaczone na czerwono. Program jest
wielojêzyczny i dzia³a z kodem UTF-8; aktualnie obs³ugiwane s± tylko
angielski i hebrajski.

%package devel
Summary:	Header files for ots library
Summary(pl):	Pliki nag³ówkowe biblioteki ots
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	glib2-devel >= 2.0
Requires:	gtk-doc-common
Requires:	libxml2-devel >= 2.4.23

%description devel
Header files for ots library.

%description devel -l pl
Pliki nag³ówkowe biblioteki ots.

%package static
Summary:	Static ots library
Summary(pl):	Statyczna biblioteka ots
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static ots library.

%description static -l pl
Statyczna biblioteka ots.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}/libots

# hack for proper linking - remove when in sources
%{__make} \
	libots_1_la_LIBADD="\$(OTS_LIBS)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ots
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}
%{_mandir}/man1/ots.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libots*
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/libots

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
