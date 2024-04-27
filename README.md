# JT-Discord-Bot
Tutorial link: https://realpython.com/how-to-make-a-discord-bot-python/


# Discord Sports Bot 

This Discord bot is designed to enhance server engagement by hosting trivia games and delivering sports news. The bot connects to a Discord server, engages members through trivia games, and tracks their scores. Additionally, the bot utilizes webhooks to fetch and relay sports news updates directly from Twitter, keeping your community informed of the latest sports events.

# Commands 
`!starttrivia`: Initiates a trivia game in the designated trivia channel. The bot randomly selects five questions from the loaded trivia question pool and presents them one at a time to the participants.

`!answer <response>`: Allows participants to submit their answers. The bot evaluates the response, updates the score accordingly, and proceeds to the next question.

## Setup Instructions

### Prerequisites
- Amazon Web Services (AWS)


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

  `python bot.py`  Ensure that your .env file, trivia_questions.json, and webhook settings are correctly set up in your project directory.









