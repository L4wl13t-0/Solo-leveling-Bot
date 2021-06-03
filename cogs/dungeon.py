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
    
    @tasks.loop(minutes = 10)
    async def createdungeon(self):
        payload = {'rank'       :       numpy.random.choice(dung['rank'], p = [0.33, 0.27, 0.20, 0.14, 0.05, 0.01]),
                   'monster'    :       numpy.random.choice(dung['monster'], p = [0.50, 0.50])}
        db.Dungeons.insert_one(payload)
        print("a")
        
    @commands.command(name = 'dungeonlist', aliases = ['dungl'])
    async def dungeonlist(self, ctx):
        for x in db.Dungeons.find():
            print(x)
        
def setup(bot):
    bot.add_cog(Dungeon(bot))