import random

import discord
from discord.utils import get
from discord.ext import commands

token = 'Your token here!'
bot = commands.Bot(command_prefix='!', pm_help=True)

messg = 645712605129867264
secret_elves = 646527764718944257
unf = 514525580503416853

server = discord.Guild

###################################################################################################

@bot.command()
async def assign_santa(ctx):
    chan = get(server.channels, id=unf)
    print(chan)
    msg = await chan.fetch_message(messg)

    for react in msg.reactions:
        async for user in react.users():
            print(user.display_name)
            await user.add_roles(server.get_role(secret_elves))


@bot.command()
async def secret_santa(ctx):
    
    people = dict()
    i = 0

    for member in server.members:
        if server.get_role(secret_elves) in member.roles:
            people[i] = [member, False]
            i += 1
    
    for person in people:
        rando = random.randint(0, i - 1)
        while True:
            if people[person][0] == people[rando][0]:
                rando = random.randint(0, i - 1)
            elif not people[rando][1]:
                people[rando][1] = True
                await people[person][0].send("Hey {}! You the person you were given for secret santa is **{}**. Don't tell anyone and don't delete this message, it's not going to be saved so there's no way to track it.".format(people[person][0].display_name, people[rando][0].display_name))
                break
            else:
                rando = random.randint(0, i - 1)

    

###################################################################################################

@assign_santa.error
async def assign_santa_error(ctx, error):
    print("__assign_santa_error__: {} ".format(error))    

@secret_santa.error
async def secret_santa_error(ctx, error):
    print("__secret_santa_error__: {} ".format(error))

###################################################################################################

@bot.event
async def on_ready():
    print("Logged in.")
    print("Name: {0.user.name}  (ID: {0.user.id})".format(bot))
    print("----------------------------------")

    global server

    server = bot.guilds[1]

bot.run(token, reconnect=True)