from re import A
import discord
from discord.ext import commands, tasks
from database.mongo import db
import numpy, os, sys, yaml
from bson.objectid import ObjectId

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
                       'players'    :       int(0)}
            db.Dungeons.insert_one(payload)
            print("Dungeon created.")
            print(db.Dungeons.find().count())
        
    @commands.command(name = 'dungeonlist', aliases = ['dglist'])
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
            data = '\n'.join(":black_small_square: **{}:** `{}`".format(value, item) for item, value in dic.items())
            pnum = '\n'.join("`{}/10`".format(num) for num in players)
            embed = discord.Embed(title = '**Dungeons List**',
                                color = 0x800080)
            embed.add_field(name = 'IDS', value = data)
            embed.add_field(name = 'PLAYER', value = pnum)
            await ctx.send(embed = embed)
        else:
            await ctx.send('You do not have a registered account, use `start` to play.')
            
    @commands.command(name = 'dungeonjoin', aliases = ['dgjoin'])
    async def dungeonjoin(self, ctx, dung = None):
        if not dung:
            await ctx.send("Use `dungeonjoin <id>`.")
        else:
            users_list = []
            for user in db.Users.find():
                users_list.append(int(user['_id']))
            
            if int(ctx.message.author.id) in users_list:
                idg = []
                playersL = []
                
                for x in db.Queuedg.find():
                    idg.append(str(x['_id']))
                    playersL.append(x['players'])
                
                pList = [j for i in playersL for j in i]
                
                query = {'_id': ObjectId(dung)}
                
                if not dung in idg:
                    if ctx.message.author.id in pList:
                        await ctx.send(f"{ctx.message.author.mention} You are already in a queue.")
                    else:
                        payload = {'_id'        :       dung,
                                   'players'    :       [ctx.message.author.id]}
                        db.Queuedg.insert_one(payload)
                        db.Dungeons.update_one(query, {'$inc': {'players': 1}})
                        await ctx.send(f"{ctx.message.author.mention} You have entered the queue, wait for it to start.")
                else:
                    if ctx.message.author.id in pList:
                        await ctx.send(f"{ctx.message.author.mention} You are already in a queue.")
                    else:
                        db.Queuedg.update_one({'_id': dung}, {'$push': {'players': ctx.message.author.id}})
                        db.Dungeons.update_one(query, {'$inc': {'players': 1}})
                        await ctx.send(f"{ctx.message.author.mention} you have entered the queue, wait for it to start.")
            else:
                await ctx.send(f'{ctx.message.author.mention} You do not have a registered account, use `start` to play.')
                
    @commands.command(name = 'dungeonleave', aliases = ['dgleave'])
    async def dungeonleave(self, ctx, dung = None):
        if not dung:
            await ctx.send(f"{ctx.message.author.mention} Use `dungeonleave <id>`.")
        else:
            users_list = []
            for user in db.Users.find():
                users_list.append(int(user['_id']))
            
            if int(ctx.message.author.id) in users_list:
                idg = []
                listP = []
                
                for x in db.Queuedg.find():
                    idg.append(str(x['_id']))
                    
                for x in db.Queuedg.find({'_id': dung}):
                    listP.append(x['players'])
                    
                pList = [j for i in listP for j in i]
                query = {'_id': ObjectId(dung)}
                
                if not dung in idg:
                    await ctx.send(f'{ctx.message.author.mention} The queue does not exist, please verify the id.')
                else:
                    if ctx.message.author.id in pList:
                        db.Queuedg.update_one({'_id': dung}, {'$pull': {'players': ctx.message.author.id}})
                        db.Dungeons.update_one(query, {'$inc': {'players': -1}})
                        await ctx.send(f'{ctx.message.author.mention} You just got out of the queue.')
                    else:
                        await ctx.send(f'{ctx.message.author.mention} You are not in this queue.')
                        print(pList)
            else:
                await ctx.send(f'{ctx.message.author.mention} You do not have a registered account, use `start` to play.')
        
def setup(bot):
    bot.add_cog(Dungeon(bot))