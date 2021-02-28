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

         "update_id":497851783,

         "message":{

            "message_id":5,

            "from":{

               "id":119749807,

               "is_bot":false,

               "first_name":"York",

               "last_name":"Keyser",

               "language_code":"de"

            },

            "chat":{

               "id":-410632878,

               "title":"Home",

               "type":"group",

               "all_members_are_administrators":true
```
     
