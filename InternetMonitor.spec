##################
# Spec file for monitoring internet connectivity
#

name:      InternetMonitor
summary:   InternetMonitor is a set of scripts that monitors internet connectivity from an internal Linux host
version:   1.0.6
release:   1
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
/usr/bin/getent group svc_intmon || /usr/sbin/groupadd -r svc_intmon
/usr/bin/getent passwd svc_intmon || /usr/sbin/useradd -r -d /opt/svc_intmon -s /bin/bash -g svc_intmon svc_intmon


%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/opt/svc_intmon/internetMonitor
mkdir -p $RPM_BUILD_ROOT/opt/svc_intmon/internetMonitor/logs
mkdir -o $RPM_BUILD_ROOT/opt/svc_intmon/internetMonitor/bin

install -D -m0644 crontab/InternetMonitor $RPM_BUILD_ROOT/etc/cron.d/InternetMonitor
install -D -m0755 files/mon.sh $RPM_BUILD_ROOT/opt/svc_intmon/internetMonitor/bin/mon.sh
install -D -m0644 config/logrotate/internetMonitor $RPM_BUILD_ROOT/etc/logrotate.d/internetMonitor


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%post

%postun

%files
%defattr(0644,svc_intmon,svc_intmon)
%config(noreplace) %attr(0644,root,root) /etc/cron.d/InternetMonitor
%config(noreplace) %attr(0644,root,root) /etc/logrotate.d/internetMonitor
%dir %attr(0755,svc_intmon,svc_intmon) /opt/svc_intmon/internetMonitor
%dir %attr(0755,svc_intmon,svc_intmon) /opt/svc_intmon/internetMonitor/logs
%attr(0755,svc_intmon,svc_intmon) /opt/svc_intmon/internetMonitor/bin/mon.sh

%changelog
* Mon Aug 17 2020 Izz Noland <izz@linux.com> 1.0.4-1-InternetMonitor-Moved to Service Account.
* Sat Aug 15 2020 Izz Noland <izz@linux.com> 1.0.3-3-InternetMonitor-Initial build.


