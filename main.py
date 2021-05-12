import discord
import logging, sys, datetime

from bot import bot

from dotenv import dotenv_values

# Init Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord'+str(datetime.date.today())+'.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Initialize Client
bot.run(dotenv_values(".env")["TOKEN"])