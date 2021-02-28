#!/bin/bash
ls -ltr  /mnt/images/ | grep ".jpg" | head -n-30 |  awk '{print $9}' | mv `xarg$

