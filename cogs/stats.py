import discord
from discord.ext import commands
from database.mongo import db

class Stats(commands.Cog, name = 'stats'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'profile')
    async def profile(self, ctx):
        data = db.Users.find_one({'_id' :   ctx.message.author.id})
        
        embed = discord.Embed(title = f"{ctx.message.author.name}\'s profile.",
                              color = 0xe534eb)
        embed.add_field(name = '**ADVANCE**', value = f":diamond_shape_with_a_dot_inside: **Level:** {data['level']}\n:anger: **Rank:** {data['rank']}\n:tools: **Class:** {data['class']}", inline = False)
        embed.add_field(name = '**STATS**', value = f":crossed_swords: **Atack:** {data['atk']}\n:shield: **Defense:** {data['def']}\n:syringe: **Life:** {data['life']}", inline = False)
        embed.add_field(name = '**MONEY**', value = f":moneybag: **Money:** {data['money']}\n:credit_card: **Bank:** {data['bank']}")
        embed.add_field(name = '**EQUIPMENT**', value = f":white_small_square: **Weapon:** {data['weapon']}\n:white_small_square: **Armor:** {data['armor']}")
        embed.set_thumbnail(url = ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(Stats(bot))