#!/usr/bin/env bash

get_volume() {
    wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{printf "%d\n", $2 * 100}'
}

get_bat() {
    cat /sys/class/power_supply/BAT0/capacity
}

day_percent() {
    hour=$(date +'%k')
    min=$(date +'%M')
    echo $(( (hour * 60 + min) * 100 / 1440 ))
}

send_notification() {
    local title="$1"
    local message="$2"
    local value="$3"
    local timeout="${4:-1000}"
    
    if [ -n "$value" ]; then
        notify-send -e "$title" -h string:x-canonical-private-synchronous:sys-notify -h int:value:"$value" "$message" -t "$timeout" || \
            hyprctl notify 1 3000 "rgb(0C1418)" "fontsize:19 $message"
    else
        notify-send "$title" "$message" -t "$timeout" || \
            hyprctl notify 1 3000 "rgb(0C1418)" "fontsize:19 $message"
    fi
}

notify_vol() {
    local volume=$(get_volume)
    if [ -z "$volume" ] || [ "$volume" = "0" ]; then
        send_notification "Volume " "It's Muted" "0"
    else
        send_notification "Volume " "$volume%" "$volume"
    fi
}

notify_mute() {
    local volume=$(get_volume)
    if [ -z "$volume" ] || [ "$volume" = "0" ]; then
        send_notification "Volume " "Muted" "0"
    else
        send_notification "Volume " "Unmuted" "$volume"
    fi
}

case "$1" in
    'mute')
        wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
        notify_mute
        ;;
    'time')
        send_notification "Time 󰥔" "It is $(date +'%l:%M %P')" "$(day_percent)"
        ;;
    'date')
        send_notification "Calendar " "$(date +'%A, %B %d')"
        ;;
    'battery')
        status=$(cat /sys/class/power_supply/BAT0/status)
        battery_level=$(get_bat)
        case "$status" in
            'Charging')    icon="󰂄" ;;
            'Discharging') icon="󰂂" ;;
            *)            icon="󰂃" ;;
        esac
        send_notification "Battery $icon" "$battery_level% $status" "$battery_level"
        ;;
    'volup')
        current_vol=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk '{print $2}')
        if [ "$(awk 'BEGIN{print ('"$current_vol"' < 1)}')" = "1" ]; then
            wpctl set-volume @DEFAULT_AUDIO_SINK@ 10%+
        fi
        notify_vol
        ;;
    'voldown')
        wpctl set-volume @DEFAULT_AUDIO_SINK@ 10%-
        notify_vol
        ;;
    'welcome')
        send_notification "Welcome" "It's $(date +'%A, %B %d')."
        ;;
esac
