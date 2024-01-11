import discord
from datetime import datetime
import os

TOKEN = 'MTEyOTM4MDcyNjkwNzg3OTQzNA.G7DaD9.A25UgkhGvslsAW1uN3wt8QUSVP5lI8w1Gu-gFg'
CHANNEL_ID = 1129383593291038782

with open('questions.txt', 'r') as file:
    questions = file.readlines()
# Remove any trailing newline characters and whitespace
questions = [question.strip() for question in questions]
num_questions = len(questions)
print(f"Retrieved {num_questions} questions.")


def get_question_formatted():
    # Get the day of the year as a number
    day_of_year = datetime.now().timetuple().tm_yday
    # Get the question corresponding to the day of the year
    question_of_the_day = questions[day_of_year - 1]  # Adjust for 0-based indexing
    return f"# **QOTD: {question_of_the_day}**"  # Add bold and large text formatting


# initialize discord client
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot is ready.')
    await send_daily_question()
    await client.close()
    raise SystemExit


async def send_daily_question():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(content=get_question_formatted()) # force run once

client.run(TOKEN)
