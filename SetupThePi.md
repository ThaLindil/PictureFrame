# Setup the Raspberry Pi headless
## Setup WIFI
After flashing the SD-Card go to the boot folder and add a new file 
wpa_supplicant.conf Content sould be 
```
cmd# nano wpa_supplicant.conf
```
Add the following part at that file. 
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter ISO 3166-1 country code here>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```
If you use Linux you could generate the network block simply with 
```
cmd# wpa_passphrase "SSID"
```
## Setup SSH
To run ssh on the pi just touch a file in the boot folder
```
cmd# touch ssh
```
## Password less SSH to your screen
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
# Update the System first
```
cmd# apt update && upgrade --fix-missing
```
