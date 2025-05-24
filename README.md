# Telegram Member Kick Bot

This bot kicks all members from a specific group except for admins.

## How It Works

The bot uses the Telethon library to interact with Telegram API. It performs the following steps:

1. Gets all admins in the group and saves them
2. Gets all members and kicks anyone who is not an admin

## How To Use

1. Go to [my.telegram.org/auth](https://my.telegram.org/auth) and create an API account

2. Set the API data in the `kick_aLL.py` file:
- `api` - API ID
- `h` - API hash
- `tok` - Bot token (you can get it from [@BotFather](https://t.me/BotFather))
- `userg` - Username of the group you want to kick members from (like "@groupname")

3. Run the bot:
   ```
   python kick_aLL.py
   ```

## Requirements

- Python 3.6+
- Telethon library
  ```
  pip install telethon
  ```

## by 
# [Tansh](https://t.me/xqxxqqxq)  , [RealCodz](https://t.me/RealCodz) 

## Important Notes

- I am not responsible for any misuse. It is for educational purposes only.
- The bot must be an admin in the group
- Use the bot carefully as kicking members may violate Telegram policies
- Make sure you want to kick all members before running the bot