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
  if before.channel != None:#!= none 是否有加入語音頻道
        guild = before.channel#抓取頻道名稱
        print(f'{member}離開->{guild}語音頻道!')#print，記錄於本機伺服器檔案
        await b.send(f'{member}離開->{guild}語音頻道!')#await .send，發送於群組
  elif after.channel != None:#判斷是否離開，guild為頻道名稱變數
        guild = after.channel
        print(f'{member}加入->{guild}語音頻道!')
        await b.send(f'{member}加入->{guild}語音頻道!')
  





bot.run('token')