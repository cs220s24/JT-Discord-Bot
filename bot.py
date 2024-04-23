import os
import certifi
import discord
from dotenv import load_dotenv
import random
import json  # Import the json module

# Ensure SSL certificates are correctly set for HTTPS requests
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')
TRIVIA_CHANNEL_ID = os.getenv('TRIVIA_CHANNEL_ID')

# Set the intents
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

# Initialize the client with the defined intents
client = discord.Client(intents=intents)

# Load trivia questions from JSON file
with open('trivia_questions.json', 'r') as file:
    trivia_questions = json.load(file)

# Active trivia session tracker
active_sessions = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild_id = int(GUILD_ID) if GUILD_ID and GUILD_ID.isdigit() else None
    if guild_id:
        guild = discord.utils.get(client.guilds, id=guild_id)
        if guild:
            print(f'{client.user} is connected to the following guild:\n'
                  f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == int(TRIVIA_CHANNEL_ID):
        if message.content.startswith('!starttrivia'):
            question = random.choice(trivia_questions)
            options_text = "\n".join(f"{idx+1}. {option}" for idx, option in enumerate(question["options"]))
            await message.channel.send(f"{question['question']}\n{options_text}")
            active_sessions[message.author.id] = {
                'answer': question['answer'],
                'options': question['options']
            }
            return

        if message.author.id in active_sessions:
            user_response = message.content.strip().lower()
            correct_answer = active_sessions[message.author.id]['answer'].lower()
            options = active_sessions[message.author.id]['options']

            if user_response == correct_answer or \
               (user_response.isdigit() and int(user_response) <= len(options) and options[int(user_response) - 1].lower() == correct_answer):
                await message.channel.send("Correct answer! 🎉")
                del active_sessions[message.author.id]
            else:
                await message.channel.send("Sorry, that's not correct. Try again!")

client.run(TOKEN)

