Summary:	Open Text Summarizer
Summary(pl.UTF-8):	Otwarte narzędzie do streszczania tekstu
Name:		ots
Version:	0.5.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libots/%{name}-%{version}.tar.gz
# Source0-md5:	1e140a4bf9d720b4339a5c2bdf4976e8
Patch0:		dic.patch
Patch1:		gtkdoc.patch
URL:		http://libots.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.5
Requires:	glib2 >= 1:2.12.0
Requires:	libxml2 >= 1:2.6.26
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

%description -l pl.UTF-8
OTS (Open Text Summarizer) to wolnodostępne narzędzie do streszczania
tekstów. Program czyta tekst i decyduje, które zdania są ważne, a
które nie.

Program może wypisać streszczenie w formacie tekstowym lub w postaci
HTML, gdzie ważne zdania są oznaczone na czerwono. Program jest
wielojęzyczny i działa z kodem UTF-8; aktualnie obsługiwane są tylko
angielski i hebrajski.

%package devel
Summary:	Header files for ots library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ots
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.0
Requires:	gtk-doc-common
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for ots library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ots.

%package static
Summary:	Static ots library
Summary(pl.UTF-8):	Statyczna biblioteka ots
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ots library.

%description static -l pl.UTF-8
Statyczna biblioteka ots.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# documentation build fails
%configure \
	--disable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/libots

%{__make}

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
%attr(755,root,root) %ghost %{_libdir}/lib*.so.0
%{_datadir}/%{name}
#%{_mandir}/man1/ots.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libots*
%{_pkgconfigdir}/*.pc
#%{_gtkdocdir}/libots

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
