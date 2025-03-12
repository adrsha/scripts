#!/usr/bin/env bash

# Battery notification script
BATTERY_PATH="/sys/class/power_supply/BAT0"
LOW_THRESHOLD=20
CRITICAL_THRESHOLD=10
MAX_BATTERY_THRESHOLD=60  # Recommended max charge to protect battery health
MAX_BATTERY_STOP_THRESHOLD=100

# Check battery capacity and charging status
if [ -f "$BATTERY_PATH/capacity" ] && [ -f "$BATTERY_PATH/status" ]; then
    CAPACITY=$(cat "$BATTERY_PATH/capacity")
    STATUS=$(cat "$BATTERY_PATH/status")
    
    # Low battery notifications
    if [ "$CAPACITY" -le "$CRITICAL_THRESHOLD" ]; then
        # Critical battery level
        DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
        notify-send -u critical "Battery Critical" "Battery level is critically low: $CAPACITY%"
    elif [ "$CAPACITY" -le "$LOW_THRESHOLD" ]; then
        # Low battery level
        DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
        notify-send -u normal "Battery Low" "Battery level is low: $CAPACITY%"
    fi
    
    # Max battery protection notifications
    if [ "$STATUS" = "Charging" ]; then
        if [ "$CAPACITY" -ge "$MAX_BATTERY_THRESHOLD" ] && [ "$CAPACITY" -lt "$MAX_BATTERY_STOP_THRESHOLD" ]; then
            # Recommend unplugging to protect battery health
            DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
            notify-send -u normal "Battery Health" "Consider unplugging to prevent overcharging. Current level: $CAPACITY%"
        elif [ "$CAPACITY" -ge "$MAX_BATTERY_STOP_THRESHOLD" ]; then
            # Strong recommendation to unplug
            DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
            notify-send -u critical "Battery Health Warning" "Unplug charger! Battery at $CAPACITY% to protect battery longevity."
        fi
    fi
fi
