#!/bin/bash

ping -q -c 1 -W 1 google.com >/dev/null
status=$?
now=`date`
if [ $status -eq 0 ]; then
    echo -e "$now -- [INFO] -- The network is up" >> /opt/svc_intmon/InternetMonitor/logs/netMon.log
else
    echo -e "$now -- [ALERT] -- The network is down" >> /opt/svc_intmon/internetMonitor/logs/netMon.log	    
fi
