# JT-Discord-Bot
Tutorial link: https://realpython.com/how-to-make-a-discord-bot-python/


# Discord Bot Project

This Discord bot is designed to connect to Discord servers (guilds), welcome new members, and deliver basketbalkl news. The bot uses the Python library `py-cord` to interact with the Discord API, and it also ensures secure HTTPS requests with SSL certificates via `certifi`.

## Setup Instructions

### Prerequisites

- Install python 
- pip (Python package installer)

### Installation

1. **Clone the repository:**

2. Create Virtual Enviroment
  `python3 -m venv .venv`

3. Activate Virtual Enviroment
  `source .venv/bin/activate`

4. Install the Requirements in `requirements.txt`
  `pip install -r requirements.txt`

5. **Set up environment variables:**

Create a `.env` file in the root directory of your project and add the following variables:

DISCORD_TOKEN=your_discord_bot_token
DISCORD_GUILD=your_guild_id
WELCOME_CHANNEL_ID=your_welcome_channel_id


Replace `your_discord_bot_token`, `your_guild_id`, and `your_welcome_channel_id` with the actual values.

6. ### Running the Bot

To run the bot, use the following command in the terminal:

  `python bot.py`









