##################
# Spec file for monitoring internet connectivity
#

name:      InternetMonitor
summary:   InternetMonitor is a set of scripts that monitors internet connectivity from an internal Linux host
version:   1.0.3
release:   2
vendor:    iztech
packager:  Izz Noland <izz@linux.com>
license:   GPL
group:     Networking/Utilities
url:       https://github.com/izz-linux/internetMonitor
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildarch: noarch
prefix:    %(echo %{_prefix})
requires:  bash
requires(pre): /usr/sbin/useradd, /usr/bin/getent
requires: crontabs
source:    %{name}-%{version}.tar.gz

%description
None.


%prep
%setup -q -n %{name}-%{version}
chmod -R u+w %{_builddir}/%{name}-%{version}

%pre
/usr/bin/getent group izz || /usr/sbin/groupadd -r izz
/usr/bin/getent passwd izz || /usr/sbin/useradd -r -d /home/izz -s /bin/bash -g izz izz


%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/home/izz/scripts/internetMonitor
mkdir -p $RPM_BUILD_ROOT/home/izz/scripts/internetMonitor/logs

install -D -m0644 crontab/InternetMonitor $RPM_BUILD_ROOT/etc/cron.d/InternetMonitor
install -D -m0755 files/mon.sh $RPM_BUILD_ROOT/home/izz/scripts/internetMonitor/mon.sh
install -D -m0644 files/logrotate/internetMonitor $RPM_BUILD_ROOT/etc/logrotate.d/internetMonitor


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%post

%postun

%files
%defattr(0644,izz,izz)
%config(noreplace) %attr(0644,root,root) /etc/cron.d/InternetMonitor
%config(noreplace) %attr(0644,root,root) /etc/logrotate.d/internetMonitor
%dir %attr(0755,izz,izz) /home/izz/scripts/internetMonitor
%dir %attr(0755,izz,izz) /home/izz/scripts/internetMonitor/logs
%attr(0755,izz,izz) /home/izz/scripts/internetMonitor/mon.sh

%changelog
* Sat Aug 15 2020 izz@linux.com
- Initial build.


