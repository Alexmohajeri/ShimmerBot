# ShimmerBot
Discord bot to send reminders of upcoming races. Currently set for the 2022 calendar with all times set to 00:00, since session times are not confirmed

This Discord bot is used to send text reminders of upcoming race times on a weekly basis.

The series included are: F1, F2, F3, DTM and Indycar

I used replit to host the bot on a web server, and used uptimerobot to keep the bot alive.

The following video was used as a reference: https://www.youtube.com/watch?v=SPTfmiYiuok

Remember to set up a TOKEN environment variable for your bot

The bot is programmed in python 3, and requires the following libraries to function:
- discord
- datetime
- os
- discord.ext
- pandas
- tabulate

Future updates will include:
- Bot will be able to create events for the server
