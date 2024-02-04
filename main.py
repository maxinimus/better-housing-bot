import discord
from discord.ext import commands, tasks
from discord import app_commands
import asyncio
import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

load_dotenv()

# Setup your discord bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

# Global variables
mute_state = False  # This will keep track of whether the bot is muted

discord_token = os.getenv('DISCORD_TOKEN')
channel_id = int(os.getenv('CHANNEL_ID'))

url_res = os.getenv('URL_RES')
url_apt = os.getenv('URL_APT')

cookies = {
    "ptx-affinity-starrezportalx": os.getenv('PTX-AFFINITY-STARREZPORTALX'),
    "starrezportalx_si_StarRezPortalX": os.getenv('STARREZPORTALX_SI_STARREZPORTALX'),
}
headers = {'User-Agent': 'Your Browser User Agent String'}

# Function to fetch webpage content
def fetch_content(url):
    with requests.Session() as session:
        session.headers.update(headers)
        session.cookies.update(cookies)
        response = session.get(url)
        response.raise_for_status()
        return response.text

# Function to parse HTML and extract available rooms information
def get_available_rooms(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    class_name = "gap-below title ui-title"
    h3_tags = soup.find_all('h3', class_=class_name)
    return [tag.get_text().strip() for tag in h3_tags]

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    bot.loop.create_task(periodic_check())

@bot.command()
async def mute(ctx):
    global mute_state
    mute_state = not mute_state
    state_msg = "enabled" if mute_state else "disabled"
    await ctx.send(f"Mute is now {state_msg}.")

    if not mute_state:
        await check_housing(ctx.channel, True)

@bot.command()
async def check(ctx):
    await check_housing(ctx.channel, True)

async def check_housing(channel, single_check=False):
    # Adapted to work with both command and periodic checks
    try:
        residence_content = fetch_content(url_res)
        residence_rooms = get_available_rooms(residence_content)

        apartment_content = fetch_content(url_apt)
        apartment_rooms = get_available_rooms(apartment_content)

        messages = []
        if not single_check:
            messages.append("-------------------------------")
        if residence_rooms:
            messages.append("Available Residences:\n" + "\n".join(residence_rooms))
            messages[-1] = messages[-1] + "\n"
        if apartment_rooms:
            messages.append("Available Apartments:\n" + "\n".join(apartment_rooms))
        if messages:
            await channel.send("\n".join(messages))
        else:
            await channel.send("No available housing found.")

    except Exception as e:
        await channel.send(f"Error checking housing: {e}")

async def periodic_check():
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    await channel.send("-------------------------------\nBot is now running with periodic (10 sec) checks.")
    if not channel:
        logging.warning("Channel not found. Please check channel_id.")
        return
    while not bot.is_closed():
        if not mute_state:
            await check_housing(channel)
        await asyncio.sleep(10)

def main():
    bot.run(discord_token)

if __name__ == "__main__":
    main()
