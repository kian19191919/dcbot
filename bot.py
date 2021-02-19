import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ban(ctx, member : discord.Member, *, reason-None):
    await member.ban(reason+reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guilt.bans():
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (memner_name, member_discriminator):
            await ctx.guilt.unban(user)
            await ctx.send(f'Unbanned {user.mention')          
            return

@client.run('ODEwNTAxMzk0OTIxNDIyOTE4.YCkkPg.ufoM_QXx2MUwxaCvVGuCUZqMHjQ')
