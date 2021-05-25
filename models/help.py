import discord
from models.mongo import db
from models.basics import bot

@bot.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title = "Help menu",
                          description = "Use `;help <command>` for extended information on a command.",
                          color = ctx.author.color)
    embed.add_field(name = "Statistics", value = "`profile`, `inventory`")
    await ctx.send(embed = embed)
    
@help.command()
async def profile(ctx):
    embed = discord.Embed(title = "Profile",
                          description = "To view your profile and stats.\nHere you can see everything related to your player, such as the money he has, level, armor, weapons, guild, floor and life.",
                          color = ctx.author.color)
    embed.add_field(name = "Use", value = "`;profile`")
    embed.set_footer(text = "Wrong command? use; help to see all the commands.")
    await ctx.send(embed = embed)