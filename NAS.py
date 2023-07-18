sudo apt update
sudo apt install mdadm lvm2 samba nfs-kernel-server cifs-utils rsync
sudo fdisk -l
sudo mdadm --create --verbose /dev/md0 --level=6 --raid-devices=7 /dev/sdX1 /dev/sdX2 /dev/sdX3 /dev/sdX4 /dev/sdX5 /dev/sdX6 /dev/sdX7
sudo fdisk -l
sudo pvcreate /dev/sdY1 /dev/sdY2 /dev/sdY3
sudo vgcreate vg_scalable /dev/sdY1 /dev/sdY2 /dev/sdY3
sudo lvcreate -l 100%FREE -n lv_scalable vg_scalable
sudo mkfs.ext4 /dev/mapper/vg_scalable-lv_scalable
sudo nano /etc/samba/smb.conf
[Admin]
   path = /chemin/du/repertoire/partage/admin
   read only = no
   valid users = jeanluc eddie amin allyant celestin lirrtiry

[User]
   path = /chemin/du/repertoire/partage/user
   read only = yes
   valid users = jeanluc eddie medhi cautputma celestin lirrtiry
sudo nano /etc/exports
/chemin/du/repertoire/partage/admin *(rw,sync,no_subtree_check)
/chemin/du/repertoire/partage/user *(ro,sync,no_subtree_check)
sudo adduser jeanluc
sudo adduser amin
sudo adduser medhi
sudo adduser celestin
sudo usermod -aG users jeanluc
sudo usermod -aG users medhi
sudo usermod -aG users celestin

sudo usermod -aG admin amin
sudo usermod -aG admin celestin
