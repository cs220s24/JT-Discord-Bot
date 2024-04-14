import os
import certifi
import discord
import tweepy
from dotenv import load_dotenv

# Ensure SSL certificates are correctly set for HTTPS requests
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')
WELCOME_CHANNEL_ID = os.getenv('WELCOME_CHANNEL_ID')

# Twitter API credentials
twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret = os.getenv('TWITTER_API_SECRET')
twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitter_api = tweepy.API(auth)

# Set the intents
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

# Initialize the client with the defined intents
client = discord.Client(intents=intents)

# Function to fetch tweets
def get_latest_tweets(user_handle, tweet_count=5):
    try:
        tweets = twitter_api.user_timeline(screen_name=user_handle, count=tweet_count, tweet_mode='extended')
        if not tweets:
            print("No tweets returned by the API.")
        return [tweet.full_text for tweet in tweets]
    except tweepy.Forbidden as e:
        print(f"Access to Twitter API forbidden: {e}")
        return []
    except tweepy.HTTPException as e:
        print(f"HTTP error from Twitter API: {e}")
        return []
    except Exception as e:
        print(f"General error: {e}")
        return []



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
            print("Guild with ID {guild_id} not found")
    else:
        print("Invalid GUILD_ID. Please check your .env configuration.")

@client.event
async def on_member_join(member):
    if member.guild.id == int(GUILD_ID):
        welcome_channel_id = int(WELCOME_CHANNEL_ID) if WELCOME_CHANNEL_ID and WELCOME_CHANNEL_ID.isdigit() else None
        if welcome_channel_id:
            welcome_channel = client.get_channel(welcome_channel_id)
            if welcome_channel:
                await welcome_channel.send(f'Welcome to the server, {member.mention}! 🎉')
            else:
                print("Welcome channel with ID {welcome_channel_id} not found")
        else:
            print("Invalid WELCOME_CHANNEL_ID. Please check your .env configuration.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the command is from the "x-tweets" channel
    if message.channel.name == "x-tweets":
        if message.content.startswith('!tweets'):
            command_parts = message.content.split()
            if len(command_parts) >= 2:
                twitter_handle = command_parts[1]
                tweets = get_latest_tweets(twitter_handle)
                response = "\n".join(tweets) if tweets else "No tweets found or unable to retrieve tweets."
                await message.channel.send(response)

client.run(TOKEN)

