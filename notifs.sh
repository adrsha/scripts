#!/bin/bash
get_volume() {
    echo "$(expr "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F ' ' '{ print $NF }' ) * 100" | bc -l | awk -F '.' '{ print $1 }')"
}
get_bat(){
    echo "$( cat /sys/class/power_supply/BAT0/capacity )"
}
day_percent(){
    echo $(expr $(expr $(date +'%k') \* 60 + $(date +"%M")) \* 100 / 1440 )
}
notify_vol(){
    if [ ! $(get_volume) ];then
        notify-send -e -a "" -h string:x-canonical-private-synchronous:sys-notify -t 555 -h  int:value:0 "It's Muted"
    else
        notify-send -e -a "" -h string:x-canonical-private-synchronous:sys-notify -t 555 -h  int:value:"$(get_volume)" "$(get_volume)%"
    fi
}
notify_mute(){
    if [ ! $(get_volume) ];then
        notify-send -e -a "" -h string:x-canonical-private-synchronous:sys-notify -t 555 -h  int:value:0 "Muted"
    else
        notify-send -e -a "" -h string:x-canonical-private-synchronous:sys-notify -t 555 -h  int:value:$(get_volume) "Unmuted"
    fi
}

if [ $1 == 'mute' ];then
    wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle & notify_mute

    elif [ $1 == 'time' ];then
    # notify-send -e -a " " -h string:x-canonical-private-synchronous:sys-notify -t 2000 -h  int:value:"$(day_percent)" "$( date +'%l:%M %P')"
    notify-send -a " " "$( date +'%l:%M %P')" -t 2000

    elif [ $1 == 'date' ];then
    notify-send -a " " "$( date +'%A, %B %d')" -t 2000

    elif [ $1 == 'battery' ];then
    if [ -f "/tmp/b-charging" ];then
        notify-send -e -a "󰂄" -h string:x-canonical-private-synchronous:sys-notify -t 1000 -h  int:value:"$(get_bat)" "$(get_bat)%"
        elif [ -f "/tmp/b-discharging" ];then
        notify-send -e -a "󰂂" -h string:x-canonical-private-synchronous:sys-notify -t 1000 -h  int:value:"$(get_bat)" "$(get_bat)%"
    else
        notify-send -e -a "󰂃" -h string:x-canonical-private-synchronous:sys-notify -t 1000 -h  int:value:"$(get_bat)" "$(get_bat)%"
    fi

    elif [ $1 == 'volup' ];then
    if [[ $(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F ' ' '{ print $NF }' ) < 1 ]];then
        wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+ & notify_vol
    else
        notify_vol
    fi

    elif [ $1 == 'voldown' ];then
    wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%- & notify_vol
fi
