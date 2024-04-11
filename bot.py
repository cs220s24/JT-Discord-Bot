import os
import certifi
import discord
from dotenv import load_dotenv

# Ensure SSL certificates are correctly set for HTTPS requests
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')  # This should be the environment variable for your guild ID
WELCOME_CHANNEL_ID = os.getenv('WELCOME_CHANNEL_ID')  # Add this environment variable for your welcome channel ID

# Set the intents
intents = discord.Intents.default()
intents.members = True  # If you're using the Members intent
intents.messages = True  # Enables the bot to receive messages in servers
intents.message_content = True  # Enable the Message Content Intent specifically

# Initialize the client with the defined intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
    guild_id = int(GUILD_ID) if GUILD_ID and GUILD_ID.isdigit() else None
    
    if guild_id:
        guild = discord.utils.get(client.guilds, id=guild_id)
        if guild:
            print(f'{client.user} is connected to the following guild:\n'
                  f'{guild.name}(id: {guild.id})')
        else:
            print(f"Guild with ID {guild_id} not found")
    else:
        print("Invalid GUILD_ID. Please check your .env configuration.")

@client.event
async def on_member_join(member):
    # Ensure the member is in the right guild before sending a welcome message
    if member.guild.id == int(GUILD_ID):
        # Convert WELCOME_CHANNEL_ID from string to integer
        welcome_channel_id = int(WELCOME_CHANNEL_ID) if WELCOME_CHANNEL_ID and WELCOME_CHANNEL_ID.isdigit() else None
        if welcome_channel_id:
            welcome_channel = client.get_channel(welcome_channel_id)
            if welcome_channel:
                await welcome_channel.send(f'Welcome to the server, {member.mention}! 🎉')
            else:
                print(f"Welcome channel with ID {WELCOME_CHANNEL_ID} not found")
        else:
            print("Invalid WELCOME_CHANNEL_ID. Please check your .env configuration.")

@client.event
async def on_message(message):
    # Avoid processing commands from the bot itself or without the specific command trigger
    if message.author == client.user:
        return

    # Add your command for listing online members here
    if message.content.startswith('!onlinemembers'):
        online_members = [member.name for member in message.guild.members if str(member.status) == "online"]
        online_members_list = ', '.join(online_members) if online_members else "No members are currently online."
        await message.channel.send(f"Online members: {online_members_list}")

client.run(TOKEN)