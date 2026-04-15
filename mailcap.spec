Summary:	Associates helper applications with particular file types
Name:		mailcap
Version:	2.1.54
Release:	1
License:	Public Domain and MIT
Group:		System/Configuration/Networking 
URL:		https://pagure.io/mailcap
Source0:	https://pagure.io/releases/mailcap/%{name}-r2-1-54.tar.gz
Source1:	mime.types
Patch0:		mailcap-2.0.4.patch
Patch1:		mailcap-2.0.4-java-web-start.patch
Patch2:		mailcap-2.0.4-ooffice.patch
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	perl-base
BuildRequires:	pkgconfig(python)

%description
The mailcap file is used by the metamail program.  Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material.  Basically, mailcap associates a particular type of file
with a particular program that a mail agent or other program can call
in order to handle the file.

Mailcap should be installed to allow certain programs to be able to
handle non-text files.

#-----------------------------------------------------------------
%package -n nginx-mimetypes
Summary:	MIME type mappings for nginx
Group:		System/Configuration/Networking

%description -n nginx-mimetypes
MIME type mappings for nginx.

%files -n nginx-mimetypes
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/nginx/mime.types

#-----------------------------------------------------------------

%prep
%setup -q


%build
%make_build

%install
%make_install sysconfdir=%{_sysconfdir} mandir=%{_mandir}

%check
make check


%files
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/mailcap
%config(noreplace) %{_sysconfdir}/mime.types
%{_mandir}/man5/mailcap.*

