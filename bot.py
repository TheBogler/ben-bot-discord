import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext.commands import cooldown, BucketType
from threading import Thread, Lock
from discord.ext import commands
from dhooks import Webhook, Embed
from asyncio import sleep
from discord import Intents
from discord.ext import commands
from discord.utils import get
from requests import put
import discord
from asyncio import create_task
client = commands.Bot(command_prefix='b!', Intents=Intents)
client.remove_command('help')
owner = 848565511834566677
@client.event
async def on_ready():
  print(f'primary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')
  global startTime
  startTime = time.time()
  await client.change_presence(activity=discord.Game(name=f"b!help | {len(client.guilds)} servers"))
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(
        title='👨‍💻 | help.',
        description="""
`b!help` - This is command.\n
`b!ben [ask]` - Ben.\n 
""",
        colour=discord.Colour.blue())
    await ctx.send(embed=embed)

@client.command()
async def ben(ctx, *, arg=None):
	ben = random.randint(0, 2)
	if ben == 0:
	    embed = discord.Embed(title="Ring.. Ring...", description="*Убрал газету*", color=0x00ff00)
	    embed.add_field(name="Ho-ho-ho", value="⬇⬇", inline=False)
	    embed.add_field(name="Ask: ", value=arg, inline=False)
	    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/931941678217052274/945616885662236713/9C870055-0F34-49C4-AB88-EC38978CC3B3.gif")
	    await ctx.send(embed=embed)
	elif ben == 1:
	    embed = discord.Embed(title="Ring.. Ring...", description="*Убрал газету*", color=0x00ff00)
	    embed.add_field(name="Yes!", value="⬇⬇", inline=False)
	    embed.add_field(name="Ask: ", value=arg, inline=False)
	    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/931941678217052274/945616885922279454/DF254486-708C-428D-BC99-ADF67434949E.gif")
	    await ctx.send(embed=embed)
	elif ben == 2:
		embed = discord.Embed(title="Ring.. Ring...", description="*Убрал газету*", color=0x00ff00)
		embed.add_field(name="No!", value="⬇⬇", inline=False)
		embed.add_field(name="Ask: ", value=arg, inline=False)
		embed.set_thumbnail(url = "https://media.discordapp.net/attachments/931941678217052274/945616886220062750/F29469FE-7BD4-49F6-AD37-3F09FA4DDE1D.gif")
		await ctx.send(embed=embed)
	else:
		await ctx.send("Error..")
	
token = "yourtokenhere"
client.run(token)
