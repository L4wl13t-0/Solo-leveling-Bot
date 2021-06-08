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
        embed.add_field(name = "Statistics", value = "`profile`, `inventory`", inline = False)
        embed.add_field(name = "Dungeons", value = "`dungeonlist`, `dungeonjoin`, `dungeonleave`", inline = False)
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
        
    @help.command()
    async def dungeonlist(self, ctx):
        embed = discord.Embed(title = 'Dungeonlist',
                              description = 'Show all active dungeons.',
                              color = ctx.author.color)
        embed.add_field(name = 'Use', value = '`;dungeonlist`')
        embed.add_field(name = 'Alias', value = '`;dglist`')
        embed.set_footer(text = "Wrong command? use; help to see all the commands.")
        await ctx.send(embed = embed)
        
    @help.command()
    async def dungeonjoin(self, ctx):
        embed = discord.Embed(title = 'Dungeonjoin',
                              description = 'To enter the queue of a dungeon.',
                              color = ctx.author.color)
        embed.add_field(name = 'Use', value = '`;dungeonjoin <id>`')
        embed.add_field(name = 'Alias', value = '`;dgjoin <id>`')
        embed.set_footer(text = "Wrong command? use; help to see all the commands.")
        await ctx.send(embed = embed)
        
    @help.command()
    async def dungeonleave(self, ctx):
        embed = discord.Embed(title = 'Dungeonleave',
                              description = 'To leave the queue of a dungeon.',
                              color = ctx.author.color)
        embed.add_field(name = 'Use', value = '`;dungeonleave <id>`')
        embed.add_field(name = 'Alias', value = '`;dgleave <id>`')
        embed.set_footer(text = "Wrong command? use; help to see all the commands.")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))