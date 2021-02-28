# Setup the telegram Bot
You could find the instraction to setup a new bot [Bots: An introduction for developers](https://core.telegram.org/bots)
## Set the privacy 
You need to set the privacy from you bot. So go to the BotFather Channel and type
```
/setprivacy
```
Choose your bot and **disable** the privacy. If you have done this you will now get the Chat ID which you need for futher steps. 

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
Here you can see the Chat_ID **-410xxxxxx** you need, it is the Number withou the minus infront.    
 Repeat that step if you add the bot to other chats or groups. Don't forget to start the bot in the chat.
 ```
 \start
 ```
 
