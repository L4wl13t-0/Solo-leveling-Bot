import discord
from discord.ext import commands

class Help(commands.Cog, name = 'help'):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name = "help", aliases = ['h'], invoke_without_command = True) #invoke_without_command = True
    async def help(self, ctx):
        embed = discord.Embed(title = "Help menu",
                              description = "Use `;help <command>` for extended information on a command.",
                              color = ctx.author.color)
        embed.add_field(name = "Statistics", value = "`profile`, `inventory`")
        await ctx.send(embed = embed)
      
    @help.command()
    async def profile(self, ctx):
        embed = discord.Embed(title = "Profile",
                              description = "To view your profile and stats.\nHere you can see everything related to your player, such as the money he has, level, armor, weapons, guild, floor and life.",
                              color = ctx.author.color)
        embed.add_field(name = "Use", value = "`;profile`")
        embed.add_field(name = "Alias", value = "`;p`")
        embed.set_footer(text = "Wrong command? use; help to see all the commands.")
        await ctx.send(embed = embed)
        
    @help.command()
    async def inventory(self, ctx):
        embed = discord.Embed(title = "Inventory",
                              description = "To view your inventory.",
                              color = ctx.author.color)
        embed.add_field(name = "Use", value = "`;inventory`")
        embed.add_field(name = "Alias", value = "`;i`")
        embed.set_footer(text = "Wrong command? use; help to see all the commands.")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))