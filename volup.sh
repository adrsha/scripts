#!/bin/bash
# requires pamixer package to read out volume

currentvolume() {
  wpctl get-volume @DEFAULT_AUDIO_SINK@
}

if [[ $(( $(currentvolume) + 10 )) -ge 100 ]]; then
  wpctl set-volume @DEFAULT_AUDIO_SINK@ 100%
else
  wpctl set-sink-volume @DEFAULT_SINK@ +10%
fi

intensity() {
  volume=$(currentvolume)
  if [[ $volume -ge 70 ]]; then
    echo high
  else
    if [[ $volume -le 30 ]]; then
      echo low
    else
      echo medium
    fi
  fi
}

result=$(intensity)

send_notification() {
  volume=$(currentvolume)
  makoctl dismiss --all && \
  notify-send -i audio-volume-$result-symbolic.symbolic "$volume"
}

correctly_notify() {
	volume=$(currentvolume)
	if [[ $volume -le 0 ]]; then
		makoctl dismiss --all && \
		notify-send -i audio-volume-$result-symbolic.symbolic "$volume"
	else
		send_notification
	fi
}

correctly_notify

# uncomment below if you want a bell on volumeup
XDG_RUNTIME_DIR=/run/user/1000 paplay /usr/share/sounds/freedesktop/stereo/bell.oga
