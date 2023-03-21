# H616-mangopi
DTS file for setting MQ-Quad / MCore-H616 board

[MQ-Quad H616](https://mangopi.org/mqquad)
# Compile DTS fit to DTB binary and reboot

```ps
sudo apt-get install sunxi-tools device-tree-compiler

cd /boot/dtb/allwinner/
dtc -I dts -O dtb -f sun50i-h616-biqu.dts -o sun50i-h616-biqu.dtb
```
