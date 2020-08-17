# InternetMonitor
InternetMonitor is a set of scripts that monitors internet connectivity from an internal Linux host

## Need
The need for a basic internet monitoring script came to be when my ISP couldn't see the dates and times when my cable
modem was going offline.  

## Meeting the Need
This simple script does a ping test against Google on a schedule (every minute) and writes 
the results to a logfile.  The log is rotated daily with a delay on compression so that the results can be reviewed
without extra steps for the previous two days at any time.

This specific set of scripts and configurations are packaged utilizing the Redhat Package Manager, built and packaged
on a CentOS 8 rpm build box.