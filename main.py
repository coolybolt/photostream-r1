import discord
#imports
r=0
import os
import time
from datetime import datetime
import asyncio
import datetime as dt
from discord.ext import commands, tasks
intents = discord.Intents(members =True,messages=True, guilds=True)
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DTOKEN')
GUILD = os.getenv('GTOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='$')#Sets prefix for commands(!Command)
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
#Await word then delete said word leaving the remainder fo the message
image_types = ["png", "jpeg", "gif", "jpg"]

@bot.event
async def on_message(message: discord.Message):
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            await attachment.save(attachment.filename)
  




#    if 'EBAY' in msg.content:
#        print('Keyword found')
#        message1=msg.content
#        newmsg = message1.replace('EBAY', '')
#        print(message1)
#        print(newmsg)
#        image = msg.attachments[0].url
#        print (image)
#        f = open("EBAY.txt", "a")
#        f.write(image+'\n')
#        f.close()    
#    if msg.content.startswith('Poste'):
#      channel = bot.get_channel(905921778931622028)
#      IMAGESEBAY = open('EBAY.txt', 'r')
#      lines = IMAGESEBAY.readlines()
#      for line in lines:
#           line =str(line)
#           print(line)
 #          print (line)
#           embed = discord.Embed(title=line, url=line)
#           await channel.send(line)


 #     yourResult = [line.split(',') for line in IMAGESEBAY.readlines()]    
 #     list.remove("[['\n'],")       
  #    for char in yourResult:
    #       if char in "[['\n'],":
  #          yourResult.replace(char,'')      
 #         print (yourResult)    
  #    await channel.send(yourResult)
#      return


#905921778931622028



#Run         
bot.run(TOKEN)
