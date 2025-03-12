killall -9 emacs
killall -9 .emacs-30.0.93-
emacs --daemon --init-directory ~/.config/emacs
notify-send -a "Emacs" "Restarted" || hyprctl notify 1 3000 "rgb(0C1418)" "fontsize:19 Emacs Restarted"
