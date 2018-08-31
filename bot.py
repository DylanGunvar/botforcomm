#https://github.com/Rapptz/discord.py
import discord
import discord.ext
import asyncio
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
import random
import os
import sys
from tkinter import *
from subprocess import call

BToken = (process.env.BOT_TOKEN);

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#LOGOS COMMANDS    
    if message.content.upper().startswith('-1ST LOGO'):
        embed = discord.Embed(title="The Deer", description="A deer folowed by are name and slogon!", color=0x8A2BE2)  
        embed.set_image(url="https://media.discordapp.net/attachments/482488997562810372/484291921695473665/Capture.PNG")
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('-2ND LOGO'):
        embed = discord.Embed(title="The Paint Splash", description="A splash of paint on a wall followed by are name and Slogon!", color=0x8A2BE2)
        embed.set_image(url="https://media.discordapp.net/attachments/482488997562810372/484291857078288384/logo-preview-6645700b-398a-4c93-946a-b643ac9d11dc.jpg?width=300&height=300")
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('-3RD LOGO'):
        embed = discord.Embed(title="The Crossed Arrows", description="2 arrows crossed followed by are name and slogon!", color=0x8A2BE2)  
        embed.set_image(url="https://media.discordapp.net/attachments/482488997562810372/484291855186395136/logo-preview-51aa1a3b-a500-496c-bbf9-48bc6ae9a402.jpg?width=300&height=300")
        await client.send_message(message.channel, embed=embed)

#STAFF APP COMMAND
    if message.content.upper().startswith('-STAFFAPP'):
        embed = discord.Embed(title="Staff Application", description="Click the link to be redirected to google were you can apply to be staff!", color=0x2B8AE2)  
        embed.add_field(name="Google Link", value="https://goo.gl/forms/NZuAAgVgQjU6NX743", inline=True)
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)

#COPY AND PASTE BELOW FOR EASY  TEMPLATEs

#Embed
    
#Line splitter \n
    
#SImple if's
    if 'VOIDED Grass(BLOCKER)' in message.content:
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Type -help for a list of out commands!" % (userID))
        await client.delete_message(message)     

#INVITE LINK
    if message.content.upper().startswith('-INV'):
        embed = discord.Embed(title="Here is the invite link for our server!", description="https://discord.gg/e9jwv6z", color=0xeef442)
        await client.send_message(message.channel, embed=embed)


#List of commands
        
    if message.content.upper().startswith('-HELP'):
        embed = discord.Embed(title="Here is a list of commands you can enter!", description="More commands will be added soon!", color=0xeeff00)
        embed.add_field(name="Commands", value="-Staffapp \n This is a link to are application for staff. \n -Inv \n This will instantly give you the invite link for our server. \n -1stLogo \n This will show 1 of 3 logo designs too wich one of them will eventually be the main logo. \n -2ndLogo \n This will show the 2nd of 3 logo designs too wich one of them will eventually be the main logo. \n -3rdLogo \n This will show the last of 3 logo designs too wich one of them will eventually be the main logo.", inline=True)
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('-123)'):
        embed = discord.Embed(title="Here is a list of out commands", description="Evntually there will be more", color=0xeef442)
        embed.add_field(name="-StaffApp", value="This is a link to are application for staff.", inline=True)
        embed.add_field(name="-Inv", value="This will instantly give you the invite link for our server.", inline=True)
        embed.add_field(name="-1stLogo", value="This will show 1 of 3 logo designs too wich one of them will eventually be the main logo..", inline=True)
        embed.add_field(name="-2ndLogo", value="This will show the 2nd of 3 logo designs too wich one of them will eventually be the main logo..", inline=True)
        embed.add_field(name="-3rdLogo", value="This will show the last of 3 logo designs too wich one of them will eventually be the main logo..", inline=True)
        await client.send_message(message.channel, embed=embed)



    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
        await client.delete_message(message)



    if '@484360841894821888' in message.content:
        embed = discord.Embed(title="Hello Good Morning, Good Evening, Good Night, Good Day you awoke me!", description="Dont do this too often please", color=0xa0132f)
        embed.add_field(name="Need Help?", value="Either do -help or contact a staff member!", inline=True)
        await client.send_message(message.channel, embed=embed)














#Login
@client.event
async def on_ready():
    print('Connected')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    await client.change_presence(game=Game(name="OOps"))

client.run(BToken)
