# Better Housing Bot

## Introduction

The Purdue Housing Bot is a specialized Discord bot designed to assist Purdue University students in finding available on-campus housing. Utilizing web scraping techniques, this bot provides real-time updates on available dorms and apartments, significantly simplifying the housing search process. This bot was instrumental in helping the creator and their roommates secure on-campus housing, avoiding the need for more expensive off-campus alternatives.

## Features

- **Real-time Housing Updates:** Automatically scrapes and reports available housing options on campus, including both residences and apartments.
- **Periodic Checks:** By default, the bot checks for housing availability every 10 seconds and sends updates to a designated Discord channel.
- **Mute Functionality:** Users can toggle the bot's periodic checks on and off with the `!mute` command, putting the bot into standby mode where it won't send messages.
- **Manual Checks:** The `!check` command allows users to perform an immediate check for available housing and receive an update.

## Setup and Configuration

1. **Install Dependencies:** Ensure you have Python 3.x installed along with the `discord.py`, `requests`, `python-dotenv`, and `beautifulsoup4` packages.
2. **Configure Environment Variables:** Use a `.env` file to store sensitive information such as your Discord bot token, channel ID, housing URLs, and any required cookies or headers for web scraping.
3. **Bot Permissions:** The bot requires permissions to send messages and manage channels within your Discord server. Ensure it's invited with the appropriate permissions.

## Usage

- **Starting the Bot:** Run the bot by executing the Python script. Once started, it will automatically begin its periodic checks.
- **Muting the Bot:** Send `!mute` in the Discord channel to toggle the periodic checks. This is useful for reducing spam or during times when housing updates are not needed.
- **Performing a Manual Check:** Use the `!check` command in the Discord channel to force the bot to perform a housing check and send an update immediately.
- **Updating .env File:** In the event that you get logged out, you likely have to update the .env with the new cookies/urls.

## Technical Details

The bot leverages the `discord.py` library for Discord integration and `requests` along with `beautifulsoup4` for web scraping. It's designed with extensibility in mind, allowing for future enhancements such as filtering by specific dorms or apartment complexes.

## Disclaimer

This bot is not officially affiliated with Purdue University or its housing services. It is a community-driven project aimed at assisting students in their housing search.

---

By utilizing this bot, Purdue students can stay informed about housing options with minimal effort, focusing on their studies and campus life instead of constantly monitoring housing availability.
