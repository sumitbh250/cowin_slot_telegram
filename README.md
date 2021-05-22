Usage:
Telegram notifier for covid vaccine slots on cowin site India.

Create a bot on telegram BotFather and get the token.
Send a message to bot from your telegram id.
Check the bot inbox from browser:
Bot inbox url: https://api.telegram.org/bot<token>/getUpdates
Replace <token> with your bot token.
Get the message id of your message.
Add the bot token and message_id(can be multiple for multiple recipients) to consts.py

Install packages in requirements.txt

Then program can be run as follows:
Modify the date daily in consts.py

python cowin.py 345 18 0
python cowin.py 345 18 1
python cowin.py 122001 18 2

The second argument is age which can be 18 or 45.
The third argument choses the API to be used:

If 3rd argument is 0 or 1:
 district_id API is used so 1st argument will be district_id from cowin. (Can be fetched from inspect element)

If 3rd argument is 2:
 pincode can be used as 1st argument.
