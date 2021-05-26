import discord
from discord.ext import commands
from database.mongo import db

class Start(commands.Cog, name = 'start'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = 'start')
    async def start(self, ctx):
        embed = discord.Embed(title = 'Your adventure begins here!',
                              description = 'Enter dungeons, kill monsters, get unique items, create a family and complete this world. All this you can from now on, level up and be the best of **VOW**.\n\n**Don\'t die, this is not a game** If you die, your character is completely erased without the opportunity to recover them, take a good look at your life.',
                              color = 0xff00e1)
        embed.add_field(name = 'HOW TO START?', value = ':white_small_square: You start in **Solaris**, the city of beginners.\n:white_small_square: Use :coin:`shop` to see the elements of the store, use :moneybag: `buy <item>` and buy your basic equipment and go to an area to start your adventure, use :airplane: `zone <zone>` go to it and start gaining levels.', inline = False)
        embed.add_field(name = 'HOW TO FARM?', value = ':white_small_square: To farm **EXP** and **MONEY** use :dagger: `hunt`, where you will have to complete the hunt. Do not forget to use :syringe: `life` to regenerate your life, you can buy more in the store.\n:white_small_square: To farm items you must go `hunt`, `adventure` or `dungeon` and find treasures.', inline = False)
        embed.add_field(name = 'MORE', value = ':white_small_square: For more information use :question: `help` and `help <command>` for a detailed explanation.')
        
        payload = {'_id'    :       int(ctx.message.author.id),
                   'level'      :       1,
                   'world'      :       'Earth',
                   'zone'       :       'Solaris',
                   'atk'        :       10,
                   'def'        :       10,
                   'life'       :       100,
                   'money'      :       10000,
                   'bank'       :       1000,
                   'weapon'     :       0,
                   'Armor'      :       0,
                   'inv'        :       {'fish' :   1,
                                         'wood' :   1},
                   'guild'      :       None}
        
        users_list = []
        for user in db.Users.find():
            users_list.append(int(user['_id']))
            
        if int(ctx.message.author.id) in users_list:
            await ctx.send(f"{ctx.message.author.mention} You already have the account registered.")
        else:
            db.Users.insert_one(payload)
            await ctx.send(f"{ctx.message.author.mention} Successfully registered account.")
        
        await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(Start(bot))