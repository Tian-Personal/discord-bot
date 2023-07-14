import discord
import asyncio
from datetime import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Open the text file
with open('questions.txt', 'r') as file:
    # Read the contents of the file
    questions = file.readlines()

# Remove any trailing newline characters and whitespace
questions = [question.strip() for question in questions]
# Display the number of retrieved questions
num_questions = len(questions)
print(f"Retrieved {num_questions} questions.")

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot is ready.')
    await send_daily_question()


async def send_daily_question():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        # Check if it's the next day and send the question
        current_time = datetime.now().strftime('%H:%M:%S')
        if current_time == '20:00:00':
            # Get the day of the year as a number
            day_of_year = datetime.now().timetuple().tm_yday
            # Get the question corresponding to the day of the year
            question_of_the_day = questions[day_of_year - 1]  # Adjust for 0-based indexing
            formatted_question = f"# **QOTD: {question_of_the_day}**"  # Add bold and large text formatting
            await channel.send(content=formatted_question)

        # Sleep for 1 second before checking the time again
        await asyncio.sleep(1)

client.run(TOKEN)
