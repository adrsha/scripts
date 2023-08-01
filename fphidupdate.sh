fd --color=never --search-path /home/chilly -t f --exclude 'node_modules,.bin' -I -l -F |awk '{print $NF}' > /home/chilly/Scripts/data/filepaths.txt
fd --color=never --search-path /home/chilly -t d --exclude node_modules -I -l -F |awk '{print $NF}' > /home/chilly/Scripts/data/dirpaths.txt
fd --color=never --search-path /home/chilly/.config/ -t d --exclude node_modules -I -l -F |awk '{print $NF}' >> /home/chilly/Scripts/data/dirpaths.txt
fd --color=never --search-path /hdd -t d --exclude node_modules -I -l -F |awk '{print $NF}' >> /home/chilly/Scripts/data/dirpaths.txt
fd --color=never --search-path /home/chilly/.config/ -t f --exclude node_modules -I -l -F |awk '{print $NF}' >> /home/chilly/Scripts/data/filepaths.txt
fd --color=never --search-path /hdd -t f --exclude node_modules -I -l -F |awk '{print $NF}' >> /home/chilly/Scripts/data/filepaths.txt

notify-send -a "Filesystem Reloaded!" "Filesystem has been reloaded."
