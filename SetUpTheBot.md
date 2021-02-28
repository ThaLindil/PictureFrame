# Setup the telegram Bot
You could find the instraction to setup a new bot [Bots: An introduction for developers](https://core.telegram.org/bots)
# Get the IDs you need
Copy the link below change the **<BOT_ID>** with your id an copy it in your favorit browser.
```
https://api.telegram.org/bot<BOT_ID>/getUpdates
```
You should see something like 
```
{

   "ok":true,

   "result":[

      {

         "update_id":497xxxxx,

         "message":{

            "message_id":5,

            "from":{

               "id":1197xxxxxx,

               "is_bot":false,

               "first_name":"NAME",

               "last_name":"NAME",

               "language_code":"de"

            },

            "chat":{

               "id":-410xxxxxx,

               "title":"Home",

               "type":"group",

               "all_members_are_administrators":true
```
     
