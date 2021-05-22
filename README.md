Telegram notifier for covid vaccine slots on cowin site India.
Setup: <br />

Create a bot on telegram BotFather and get the token.
Send a message to bot from your telegram id.
Check the bot inbox from browser:
Bot inbox url: https://api.telegram.org/bot<token\>/getUpdates
Replace <token\> with your bot token.
Get the message id of your message.
Add the bot token and message_id(can be multiple for multiple recipients) to consts.py

Install packages in requirements.txt

Usage: <br />
Then program can be run as follows:<br />
Modify the date daily in consts.py

python cowin.py 345 18 0 <br />
python cowin.py 345 18 1 <br />
python cowin.py 122001 18 2 <br />

The second argument is age which can be 18 or 45. <br />
The third argument choses the API to be used: <br />

If 3rd argument is 0 or 1: <br />
 district_id API is used so 1st argument will be district_id from cowin. (Can be fetched from inspect element) <br />

If 3rd argument is 2: <br />
 pincode can be used as 1st argument. <br />
