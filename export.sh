#!/bin/bash


git archive master --prefix=InternetMonitor-$1/ | gzip > ../InternetMonitor-$1.tar.gz
