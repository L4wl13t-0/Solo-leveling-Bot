import discord
from discord.ext import commands
import os, sys, yaml

if not os.path.isfile("config.yaml"):
    sys.exit("'config.yaml' not found! Please add it and try again.")
else:
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

class Moderation(commands.Cog, name = 'moderation'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = 'reloadcog')
    async def reloadcog(self, ctx, module):
        if ctx.message.author.id in config["moderators"]:
            try:
                self.bot.unload_extension(f"cogs.{module}")
                self.bot.load_extension(f"cogs.{module}")
                await ctx.send("**" + module + "**" + " has been updated successfully.")
            except:
                await ctx.send("**" + module + "**" + " could not be found or could not restart.")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
            
            
    @commands.command(name = 'loadcog')
    async def loadcog(self, ctx, module):
        if ctx.message.author.id in config["moderators"]:
            try:
                self.bot.load_extension(f"cogs.{module}")
                await ctx.send("**" + module + "**" + " has been loaded successfully.")
            except:
                await ctx.send("**" + module + "**" + " could not be found or could not load.")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
            
    @commands.command(name = 'unloadcog')
    async def unloadcog(self, ctx, module):
        if ctx.message.author.id in config["moderators"]:
            try:
                self.bot.unload_extension(f"cogs.{module}")
                await ctx.send("**" + module + "**" + " has been unloaded successfully.")
            except:
                await ctx.send("**" + module + "**" + " could not be found or could not load.")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
            
def setup(bot):
    bot.add_cog(Moderation(bot))