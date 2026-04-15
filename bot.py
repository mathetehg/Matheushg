import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')

@bot.group()
async def cool(ctx):
    
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


bot.run("")
