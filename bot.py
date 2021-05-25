import discord
from models.basics import token, bot
import models.help

@bot.event
async def on_ready():
    game = discord.Game('Developing the API')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Bot ready...')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
