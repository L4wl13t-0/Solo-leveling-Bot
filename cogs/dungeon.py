import discord
from discord.ext import commands, tasks
from database.mongo import db
import numpy, os, sys, yaml

if not os.path.isfile("dungeon.yaml"):
    sys.exit("'dungeon.yaml' not found! Please add it and try again.")
else:
    with open("dungeon.yaml") as file:
        dung = yaml.load(file, Loader=yaml.FullLoader)

class Dungeon(commands.Cog, name = 'dungeon'):
    def __init__(self, bot):
        self.bot = bot
        self.createdungeon.start()
    
    @tasks.loop(minutes = 15)
    async def createdungeon(self):
        payload = {'rank'       :       numpy.random.choice(dung['rank'], p = [0.33, 0.27, 0.20, 0.14, 0.05, 0.01]),
                   'monster'    :       numpy.random.choice(dung['monster'], p = [0.50, 0.50])}
        db.Dungeons.insert_one(payload)
        print("a")
        
    @commands.command(name = 'dungeonlist', aliases = ['dungl'])
    async def dungeonlist(self, ctx):
        users_list = []
        for user in db.Users.find():
            users_list.append(int(user['_id']))
        
        if int(ctx.message.author.id) in users_list:
            idg = []
            rank = []
            for x in db.Dungeons.find():
                idg.append(str(x['_id']))
                rank.append(x['rank'])
            dic = (dict(zip(rank, idg)))
            data = '\n'.join(":black_small_square: **{}:** `{}`".format(item, value) for item, value in dic.items())
            
            embed = discord.Embed(title = '**Dungeons List**',
                                color = 0x800080)
            embed.add_field(name = 'Complete all.', value = data)
            await ctx.send(embed = embed)
        else:
            await ctx.send('You do not have a registered account, use `start` to play.')
        
def setup(bot):
    bot.add_cog(Dungeon(bot))