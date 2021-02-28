#! /usr/bin/env python
import argparse
import os
import requests
import os.path
from os import path

BOT_TOKEN = "<BOT_ID>"
CHAT_IDS = ["<CHAT_ID 1>", "<CHAT_ID 2>", "<CHAT_ID 3>"]

def get_images(folder_path, chat_id):

    db_image_ids = read_db(folder_path);
    updates = post_json('getUpdates', data={"chat_id": chat_id})
    for message in updates["result"][-30:]:
        #print(u"{}\n".format(message["message"]["message_id"]))
        if "photo" in message["message"]:
            image_id = message["message"]["photo"][-1]["file_id"]
            image_exists = bool(False)
            for lokal_image_id in db_image_ids:
                if image_id == lokal_image_id:
                    image_exists = bool(True)
                    break
            if not image_exists:
                photo = get_json('getFile', params={"chat_id": chat_id, "file_id": image_id})
                image_path = photo['result']['file_path']
                download_image(image_id, image_path, folder_path)
                db_image_ids.append(image_id)

            if not db_image_ids:
                db_image_ids.append(message["message"]["photo"][-1]["file_id"])

    write_db(folder_path, db_image_ids)

def download_image(image_id, image_path, folder_path):
    print("Download Image")
    file_name = os.path.basename(image_path)
    response = requests.get('https://api.telegram.org/file/bot%s/%s' % (BOT_TOKEN, image_path))
    dst_file_path = os.path.join(folder_path, file_name)
    with open(dst_file_path, 'wb') as f:
        f.write(response.content)
    #print(u"Downloaded file to {}".format(dst_file_path))

def get_json(method_name, *args, **kwargs):
    return make_request('get', method_name, *args, **kwargs)

def post_json(method_name, *args, **kwargs):
    return make_request('post', method_name, *args, **kwargs)

def make_request(method, method_name, *args, **kwargs):
    response = getattr(requests, method)(
        'https://api.telegram.org/bot%s/%s' % (BOT_TOKEN, method_name),
        *args, **kwargs
    )
    if response.status_code > 200:
        raise DownloadError(response)
    return response.json()

def read_db(folder_path):
    image_id_db = []
    # open file and read the content in a list
    if not path.exists(folder_path+'/db.txt'):
        return image_id_db

    with open(folder_path+'/db.txt', 'r') as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            current_place = line[:-1]
            image_id_db.append(current_place)
    return image_id_db

def write_db(folder_path, image_ID_List):
    with open(folder_path+'/db.txt', 'w+') as filehandle:
        filehandle.writelines("%s\n" % id for id in image_ID_List)

def main():
    parser = argparse.ArgumentParser("Download photos")
    parser.add_argument("folder", help="Destination folder")
    args = parser.parse_args()
    for chat_id in CHAT_IDS:
        get_images(args.folder, chat_id)

if __name__ == "__main__":
    main()
