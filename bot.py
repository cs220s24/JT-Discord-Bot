import os
import certifi
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import json
import redis
# Ensure SSL certificates are correctly set for HTTPS requests
os.environ['SSL_CERT_FILE'] = certifi.where()

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')
TRIVIA_CHANNEL_ID = os.getenv('TRIVIA_CHANNEL_ID')
host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

if port is None:
    port = 6379

if host is None:
    host = 'localhost'

# Set the intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Initialize the client with the defined intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Load trivia questions
with open('trivia_questions.json', 'r') as file:
    trivia_questions = json.load(file)

# Active trivia sessions with questions and scores
active_sessions = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

def select_questions():
    return random.sample(trivia_questions, 5)



@bot.command(name="starttrivia")
async def start_trivia(ctx):
    if ctx.channel.id == int(TRIVIA_CHANNEL_ID):
        questions = select_questions()
        active_sessions[ctx.author.id] = {
            'questions': questions,
            'current_question': 0,
            'score': 0
        }
        question = questions[0]['question']
        options_text = "\n".join(f"{idx + 1}. {option}" for idx, option in enumerate(questions[0]["options"]))
        await ctx.send(f"Question 1: {question}\n{options_text}")

@bot.command(name="answer")
async def answer(ctx, *, user_response: str):
    session = active_sessions.get(ctx.author.id)
    if session:
        current_question = session['questions'][session['current_question']]
        correct_answer = current_question['answer'].lower()
        options = current_question['options']

        if user_response.lower() == correct_answer or \
           (user_response.isdigit() and int(user_response) <= len(options) and options[int(user_response) - 1].lower() == correct_answer):
            session['score'] += 1
            result_text = "Correct answer! 🎉\n"
        else:
            result_text = "Sorry, that's not correct.\n"

        session['current_question'] += 1
        if session['current_question'] < 5:
            next_question = session['questions'][session['current_question']]
            question_text = next_question['question']
            options_text = "\n".join(f"{idx + 1}. {option}" for idx, option in enumerate(next_question["options"]))
            await ctx.send(f"{result_text}Next question: {question_text}\n{options_text}")
        else:
            score = session['score']
            await ctx.send(f"{result_text}You've completed the trivia! Your score: {score}/5")
            del active_sessions[ctx.author.id]

bot.run(TOKEN)
