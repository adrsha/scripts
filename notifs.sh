#!/bin/bash


if [[ $( wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F '.' '{ print $NF }' ) == *"MUTE"* ]];then
  if [ $1 == 'mute' ];then
      wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle && notify-send -a "Volume Level:" "0%" -i "/home/chilly/Pictures/assets/sf-black/volume-low.png" -t 5000 -r 8880
    else
      notify-send -a "Volume Level: " "0% " -i "/home/chilly/Pictures/assets/sf-black/volume-low.png" -t 5000 -r 8880
    fi
else
if [ $1 == 'time' ];then
  notify-send -a "Current Time:" "$( date +'%l:%M %P')" -i "/home/chilly/Pictures/assets/sf-black/clock.png" -t 5000 -r 8881
elif [ $1 == 'date' ];then
  notify-send -a "Current Date:" "$( date +'%A, %B %d')" -i "/home/chilly/Pictures/assets/sf-black/calendar.png" -t 5000 -r 8882
elif [ $1 == 'battery' ];then
  if [ -f "/tmp/b-charging" ];then
    notify-send -a "Battery Level: " " $( cat /sys/class/power_supply/BAT0/capacity )%" -i "/home/chilly/Pictures/assets/sf-black/battery.png" -t 5000 -r 8883
  elif [ -f "/tmp/b-discharging" ];then
    notify-send -a "Battery Level:" "  $( cat /sys/class/power_supply/BAT0/capacity )%" -i "/home/chilly/Pictures/assets/sf-black/battery.png" -t 5000 -r 8883
  else
    notify-send -a "Battery Level:" "$( cat /sys/class/power_supply/BAT0/capacity )%" -i "/home/chilly/Pictures/assets/sf-black/battery.png" -t 5000 -r 8883
  fi
elif [ $1 == 'volup' ];then
  if [[ $(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F ' ' '{ print $NF }' ) < 1 ]];then
    wpctl set-volume @DEFAULT_AUDIO_SINK@ 10%+ && notify-send -a "Volume Level:" "$(expr "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F ' ' '{ print $NF }' ) * 100" | bc -l | awk -F '.' '{ print $1 }' )%" -i "/home/chilly/Pictures/assets/sf-black/volume.png" -t 500 -r 8880
  else
    notify-send -a "Volume Level is" "$(expr "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F ' ' '{ print $NF }' ) * 100" | bc -l | awk -F '.' '{ print $1 }' )%" -i "/home/chilly/Pictures/assets/sf-black/volume.png" -t 5000 -r 8880
  fi
elif [ $1 == 'voldown' ];then
  wpctl set-volume @DEFAULT_AUDIO_SINK@ 10%- && notify-send -a "Volume Level:" "$(expr "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F ' ' '{ print $NF }' ) * 100" | bc -l | awk -F '.' '{ print $1 }' )%" -i "/home/chilly/Pictures/assets/sf-black/volume.png" -t 500 -r 8880
elif [ $1 == 'mute' ];then
  if [[ $( wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F '.' '{ print $NF }' ) == *"MUTE"* ]];then
    wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle && notify-send -a "Volume Level:" "$( wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F '.' '{ print $NF }' )%" -i "/home/chilly/Pictures/assets/sf-black/volume.png" -t 5000 -r 8880
  else
    wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle && notify-send -a "Volume Level:" "0%" -i "/home/chilly/Pictures/assets/sf-black/volume-low.png" -t 5000 -r 8880
  fi
fi
fi
