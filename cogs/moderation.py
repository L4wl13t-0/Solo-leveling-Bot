import discord
from discord.ext import commands
import os, sys, yaml
from database.mongo import db, client

if not os.path.isfile("config.yaml"):
    sys.exit("'config.yaml' not found! Please add it and try again.")
else:
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

class Moderation(commands.Cog, name = 'moderation'):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = 'reloadcog')
    async def reloadcog(self, ctx, module = None):
        if not module:
            await ctx.send("Use `reloadcog <module>`.")
        else:
            if ctx.message.author.id in config["moderators"]:
                try:
                    self.bot.unload_extension(f"cogs.{module}")
                    self.bot.load_extension(f"cogs.{module}")
                    await ctx.send("**" + module + "**" + " has been updated successfully.")
                except:
                    await ctx.send("**" + module + "**" + " could not be found or could not restart.")
            else:
                await ctx.send("You do not have sufficient permissions to perform this action.")
            
            
    @commands.command(name = 'loadcog')
    async def loadcog(self, ctx, module = None):
        if not module:
            await ctx.send("Use `loadcog <module>`.")
        else:
            if ctx.message.author.id in config["moderators"]:
                try:
                    self.bot.load_extension(f"cogs.{module}")
                    await ctx.send("**" + module + "**" + " has been loaded successfully.")
                except:
                    await ctx.send("**" + module + "**" + " could not be found or could not load.")
            else:
                await ctx.send("You do not have sufficient permissions to perform this action.")
            
    @commands.command(name = 'unloadcog')
    async def unloadcog(self, ctx, module = None):
        if not module:
            await ctx.send("Use `unloadcog <module>`.")
        else:
            if ctx.message.author.id in config["moderators"]:
                try:
                    self.bot.unload_extension(f"cogs.{module}")
                    await ctx.send("**" + module + "**" + " has been unloaded successfully.")
                except:
                    await ctx.send("**" + module + "**" + " could not be found or could not load.")
            else:
                await ctx.send("You do not have sufficient permissions to perform this action.")
            
    @commands.command(name = 'deletealldbyes')
    async def deletealldbyes(self, ctx):
        if ctx.message.author.id in config["moderators"]:
            try:
                client.drop_database('RPG')
                await ctx.send("Database drop (Successful).")
            except:
                await ctx.send("Database drop (Fail).")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
            
    @commands.command(name = 'deletedungeons')
    async def deletedungeons(self, ctx):
        if ctx.message.author.id in config["moderators"]:
            try:
                db.Dungeons.drop()
                await ctx.send("Database drop (Successful).")
            except:
                await ctx.send("Database drop (Fail).")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
            
    @commands.command(name = 'addfirstuser')
    async def addfirstuser(self, ctx):
        if ctx.message.author.id in config["moderators"]:
            try:
                payload = {'_id'    :       34534634634634,
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
                
                db.Users.insert_one(payload)
                await ctx.send("Insert user (Successful).")
            except:
                await ctx.send("Insert user (Fail).")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
            
    @commands.command(name = 'showdungeons')
    async def showddungeons(self, ctx):
        if ctx.message.author.id in config["moderators"]:
            try:
                print(db.list_collection_names())
                for x in db.Dungeons.find():
                    print(x)
                await ctx.send("(Successful).")  
            except:
                await ctx.send("(Fail).")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
        
    @commands.command(name = 'showqueue')
    async def showdqueue(self, ctx):
        if ctx.message.author.id in config["moderators"]:
            try:
                print(db.list_collection_names())
                for x in db.Queuedg.find():
                    print(x)
                await ctx.send("(Successful).")  
            except:
                await ctx.send("(Fail).")
        else:
            await ctx.send("You do not have sufficient permissions to perform this action.")
            
def setup(bot):
    bot.add_cog(Moderation(bot))