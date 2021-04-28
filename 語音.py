import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    a = bot.get_channel(835343604209287228)
    await a.send(">> Bot is online <<")
    print(">> Bot is online <<")



@bot.event
async def on_voice_state_update(member,before,after):
  b = bot.get_channel(835343604209287228)
  await b.send(f'{member}加入語音頻道!')
   



bot.run('token')