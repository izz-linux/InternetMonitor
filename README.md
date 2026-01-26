# InternetMonitor

InternetMonitor is a set of scripts that monitors internet connectivity from an internal Linux host.

## Need

The need for a basic internet monitoring script came to be when my ISP couldn't see the dates and times when my cable modem was going offline.

## Meeting the Need

This simple script does a ping test against Google on a schedule (every minute) and writes the results to a logfile. The log is rotated daily with a delay on compression so that the results can be reviewed without extra steps for the previous two days at any time.

This specific set of scripts and configurations are packaged utilizing the Redhat Package Manager, built and packaged on a CentOS 8 rpm build box.

## Build Commands

**Create source tarball for RPM build:**
```bash
./export.sh <version>
# Example: ./export.sh 1.0.8
# Creates: ../InternetMonitor-1.0.8.tar.gz
```

**Build RPM package:**
```bash
rpmbuild -ba InternetMonitor.spec
```

## Architecture

**Execution Flow:**
1. Cron daemon (`/etc/cron.d/InternetMonitor`) triggers `mon.sh` every minute
2. `mon.sh` pings google.com and logs UP/DOWN status with timestamp
3. Logrotate manages `/opt/svc_intmon/internetMonitor/logs/netMon.log` (14-day retention, daily rotation)

**Runtime Layout (after RPM install):**
- `/opt/svc_intmon/internetMonitor/bin/mon.sh` - Main monitoring script
- `/opt/svc_intmon/internetMonitor/logs/netMon.log` - Output log
- `/etc/cron.d/InternetMonitor` - Cron schedule
- `/etc/logrotate.d/internetMonitor` - Log rotation config

**Service Account:** All components run under `svc_intmon:svc_intmon` (created during RPM pre-install)

## Key Files

| File | Purpose |
|------|---------|
| `InternetMonitor.spec` | RPM spec defining package build, dependencies, and install locations |
| `files/mon.sh` | Core monitoring script (ping test + logging) |
| `crontab/InternetMonitor` | Cron job definition (runs every minute) |
| `config/logrotate/internetMonitor` | Log rotation rules |
| `export.sh` | Creates versioned tarball from master branch for RPM source |

## Version Updates

When releasing a new version:
1. Update `version:` in `InternetMonitor.spec`
2. Add changelog entry in `InternetMonitor.spec` with date and changes
3. Run `./export.sh <new-version>` to create tarball