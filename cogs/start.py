import discord
from discord.ext import commands
from database.mongo import db

class Start(commands.Cog, name = 'start'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = 'start')
    async def start(self, ctx):
        
        startinfo = 'Every so often dungeons will appear in the city, your duty is to enter and defeat the monsters. Each dungeon has a time limit to be completed, if it is not done the dungeon will be opened and the monsters will be able to escape to the world.'
        dungeonlist = ':white_small_square: Use :crossed_swords: `dungeonlist` to see the list of dungeons that can enter, each dungeon has a statistical range that determines its difficulty, you can enter any dungeon you want, you decide the difficulty.'
        enterdungeon = ':white_small_square: To enter join a dungeon use :dagger: `enterdungeon <id>` and wait for it to start.'
        getitems = ':white_small_square: When entering a dungeon and killing monsters, you have a chance that they will drop an item. At the end of the dungeon, the items found inside will be distributed equally to all players. To see your items use :briefcase: `inventory`'
        getmoney = ':white_small_square: For killing and finishing a dungeon these will give you a monetary reward, you can also sell your items using :scales: `sell <item>`. To see your money use :moneybag: `money` or :credit_card: `bank`.'
        
        embed = discord.Embed(title = 'You have earned the right to be a player.',
                              description = 'Welcome player! Your duty is to protect this world and its people, save them from destruction.\n`Don\'t die`, you won\'t have another chance.',
                              color = 0x18a4f8)
        embed.add_field(name = 'HOW TO START?', value = f'{startinfo}\n\n{dungeonlist}\n{enterdungeon}', inline = False)
        embed.add_field(name = 'AND AFTER?', value = f'{getitems}\n{getmoney}', inline = False)
        embed.add_field(name = 'MORE', value = ':white_small_square: For more information use :question: `help` and `help <command>` for a detailed explanation.')
        
        payload = {'_id'    :       int(ctx.message.author.id),
                   'level'      :       1,
                   'rank'       :       "E",
                   'atk'        :       10,
                   'def'        :       10,
                   'life'       :       100,
                   'money'      :       10000,
                   'bank'       :       1000,
                   'weapon'     :       0,
                   'armor'      :       0,
                   'inv'        :       {'white crystal' :   1,
                                         'wolf tooth' :   1},
                   'hab'        :       ['Double hit',
                                         'Whip'],
                   'guild'      :       None,
                   'class'      :       None,
                   'oncommand'  :       0,
                   'ondungeon'  :       0}
        
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