#!/bin/bash
# Default the last 30 images will stay and the older one will be moved to the folder backup. If you want another number of image change the -n-30.
ls -ltr  /mnt/images/ | grep ".jpg" | head -n-30 |  awk '{print $9}' | mv `xarg$ backup

