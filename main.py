import discord
import discord.utils
import sqlite3
import os.path
from os import path
import datetime



if str(path.exists('base.db')) == "False":
   connection = sqlite3.connect('base.db')
   cursor = connection.cursor()
   cursor.execute('CREATE TABLE base (id INTEGER PRIMARY KEY, datetime TEXT, user TEXT)')
   connection.commit()
else :
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    connection.commit()



client = discord.Client()


@client.event
async def on_ready():
    activity = discord.Activity(name='my activity', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    x = datetime.datetime.now()
    print("BOT ON : "+x.strftime("%x"+" %X"))
    return

@client.event
async def on_member_join(member):
    print(member)
    x = datetime.datetime.now()
    print(x.strftime("%x"+" %X"))
    cursor.execute('INSERT INTO base(datetime, user) VALUES(?, ?)', (str(x.strftime("%x"+" %X")), str(member)))
    connection.commit()
    return


client.run("TOKEN")

