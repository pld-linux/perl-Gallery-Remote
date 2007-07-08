#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Gallery
%define	pnam	Remote
Summary:	Gallery::Remote - Perl extension for interacting with the Gallery remote protocol
Summary(pl.UTF-8):	Gallery::Remote - rozszerzenie Perla do współpracy z protokołem Gallery remote
Name:		perl-Gallery-Remote
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/L/LO/LOVELACE/Gallery-Remote-%{version}.tar.gz
# Source0-md5:	7cac0ed8d156668457f61174af6db00b
URL:		http://search.cpan.org/dist/Gallery-Remote/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gallery::Remote is a Perl module that allows remote access to a remote
gallery.

%description -l pl.UTF-8
Gallery::Remote to moduł Perla pozwalający na zdalny dostęp do
galerii.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Gallery/*.pm
%{_mandir}/man3/*
