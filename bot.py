import discord
from default.basics import token, bot
import os

@bot.event
async def on_ready():
    game = discord.Game('Developing the API')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print('Bot ready...')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

bot.run(token)
