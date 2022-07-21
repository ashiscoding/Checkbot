import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(intents=intents, command_prefix='.')
client.remove_command('help')

@client.event
async def on_message(message):
    if message.guild.id == 995429222497652796 and message.channel.id == 999597525172490311:
        if message.content.startswith("0x"):
            wallets = open("wallets.txt",encoding='utf-8').read().splitlines()
            wallets = [wallet.lower() for wallet in wallets]
            if message.content.lower() in wallets:
                await message.add_reaction("✅")
            else:
                await message.add_reaction("❌")

client.run(os.environ["DISCORD_TOKEN"])
