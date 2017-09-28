#! /bin/bash

log="/home/pi/logs/"

#run the client

"/home/pi/development/humidity-sensor/dht" > temperature.txt

OUTPUT=`cat temperature.txt`

# Write values to the screen

TEMPERATURE=`echo "$OUTPUT"`

# Output data to a log file

sudo echo "$(date +"%Y-%m-%d %T" ): ""$TEMPERATURE" >>"$log"temperature.log
