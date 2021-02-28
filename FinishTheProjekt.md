# Finish the digital image frame project

# Copy the files
```
scp StartTheFrame.sh pi@<IP>:/tmp
scp ClearTheFrame.sh pi@<IP>:/tmp
scp GetImages.py pi@<IP>:/tmp
```
```
ssh pi@<IP>
  
```
Create the main folder
```

sudo mkdir /mnt/images

```
Move the files there 
  
```
sudo mv StartTheFrame.sh /mnt/image
sudo mv ClearTheFrame.sh /mnt/image
sudo mv GetImages.py /mnt/image
```

## Crontab
To get alle the image automatically we setup a cronjob which download new images and also cleaning the frame from old images.
```
sudo crontab -e
```
add
```
0 */1 0 0 0 python3 /mnt/images/getImage.py /mnt/images/
0 0 */1 0 0 /bin/bash /mnt/images/cleanFrame.sh
