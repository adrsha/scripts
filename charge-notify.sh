#!/bin/sh

# Send a notification displaying that the battery is charging or discharging
# Pass 1 as an argument for charging, 0 for discharging
# Example usage: chargingnotify 1

# Check if argument is passed
[ $# != 1 ] && printf '0 or 1 must be passed as an argument.\nUsage: %s 0|1\n' "$0" && exit

export XAUTHORITY=/home/eric/.Xauthority
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"

BATTERY_CHARGING=$1
BATTERY_LEVEL=$( cat /sys/class/power_supply/BAT0/capacity ) 
# Send notifications
if [ "$BATTERY_CHARGING" -eq 1 ]; then
    /bin/notify-send -a "Plugged In." " ${BATTERY_LEVEL}%" -u normal 
    touch /tmp/b-charging
    rm -rf /tmp/b-discharging
elif [ "$BATTERY_CHARGING" -eq 0 ]; then
    /bin/notify-send -a "Plugged Out." "⬇ ${BATTERY_LEVEL}%" -u normal 
    touch /tmp/b-discharging
    rm -rf /tmp/b-charging
fi
