import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print('Pronto come ' + bot.user.name + "#" +bot.user.discriminator)

@bot.command()
async def ciao(ctx):
    await ctx.send(f"bella **{ctx.author.name}** (<@{ctx.author.id}>)")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="Nessun motivo specificato"
    await ctx.guild.ban(member)
    await ctx.send(f"**L'utente {member.mention} è stato bannato per {reason}**")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"**Non hai specificato un utente** {ctx.author.name}**, l'operazione non può completarsi**")

@bot.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(ctx.channel.mention + " ***è stato bloccato.***")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***è stato sbloccato.***")

@bot.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Ho messo il deelay di questo canale su **{seconds} secondi!**")

@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Specifica il tempo!")

@bot.command(aliases= ['purge','delete'])

async def clear(ctx, amount : int):
   if amount == None:
       await ctx.channel.purge(limit=1000000)
   else:
       await ctx.channel.purge(limit=amount)

