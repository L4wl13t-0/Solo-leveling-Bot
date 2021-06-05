import discord
from discord.ext import commands, tasks
from database.mongo import db
import numpy, os, sys, yaml, time

if not os.path.isfile("dungeon.yaml"):
    sys.exit("'dungeon.yaml' not found! Please add it and try again.")
else:
    with open("dungeon.yaml") as file:
        dung = yaml.load(file, Loader=yaml.FullLoader)

class Dungeon(commands.Cog, name = 'dungeon'):
    def __init__(self, bot):
        self.bot = bot
        self.createdungeon.start()
    
    @tasks.loop(seconds = 10)
    async def createdungeon(self):
        if db.Dungeons.find().count() < 15:
            payload = {'rank'       :       numpy.random.choice(dung['rank'], p = [0.33, 0.27, 0.20, 0.14, 0.05, 0.01]),
                       'monster'    :       numpy.random.choice(dung['monster'], p = [0.50, 0.50]),
                       'players'    :       0}
            db.Dungeons.insert_one(payload)
            print("Dungeon created.")
            print(db.Dungeons.find().count())
        
    @commands.command(name = 'dungeonlist', aliases = ['dungl'])
    async def dungeonlist(self, ctx):
        users_list = []
        for user in db.Users.find():
            users_list.append(int(user['_id']))
        
        if int(ctx.message.author.id) in users_list:
            idg = []
            rank = []
            players = []
            for x in db.Dungeons.find():
                idg.append(str(x['_id']))
                rank.append(x['rank'])
                players.append(x['players'])
            dic = (dict(zip(idg, rank)))
            for pnum in players:
                data = '\n'.join(":black_small_square: **{}:** `{}`  `{}/10`".format(value, item, pnum) for item, value in dic.items())
            embed = discord.Embed(title = '**Dungeons List**',
                                color = 0x800080)
            embed.add_field(name = 'Complete all.', value = data)
            await ctx.send(embed = embed)
        else:
            await ctx.send('You do not have a registered account, use `start` to play.')
        
def setup(bot):
    bot.add_cog(Dungeon(bot))