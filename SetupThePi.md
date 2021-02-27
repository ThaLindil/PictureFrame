# Befor first booting
Flash the SD card with Operating system you need. After flashing the SD you can mount the SD Card on you Laptop or Desktop and could configured befor the first run.

## Setup WIFI
Create a file in the boot folder, named wpa_supplicant.conf open the file
```
cmd# nano wpa_supplicant.conf
```
add the following part at that file. 
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```
if you use Linux you could generate the network block simply with 
```
cmd# wpa_passphrase "SSID"
```
## Setup SSH
To run ssh on the pi just touch a file in the boot folder
```
cmd# touch ssh
```

## Password less SSH
### Generate a new Key
```
cmd# ssh-keygen
```
### Share the key
```
cmd# ssh-copy-id pi@<IP-ADDRESS>
```
### Try the connection
```
cmd# ssh pi@<IP-ADDRESS>
```
## Update the System first
```
cmd# sudo apt update && upgrade --fix-missing
```
## Disable Display-Lock
```
cmd# sudo raspi-config
```
Got to **2 Display Options** -> **D4 Screen Blanking**

## Setup VNC
To be able so setup the GUI you will need a VNC client. 
```
cmd# sudo apt install realvnc-vnc-server
```
Next step enable VNC
```
cmd# sudo raspi-config
``` 
Got to **3 Interface Options** -> **P3 VNC**

