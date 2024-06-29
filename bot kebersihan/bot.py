import discord
from discord.ext import commands
from main import get_fact, get_contoh, get_info, get_tips
import random

with open("token.txt", "r") as f:
    token = f.read()

jenis_sampah = {
    "Organik": ["Kulit buah", "Sisa sayuran", "Daun gugur", "Rumput", "Kopi bekas", "Kulit telur", "Sisa makanan", "Batang sayuran", "Serbuk kayu", "Bunga layu"],
    "Anorganik": ["Botol plastik", "Kantong plastik", "Sedotan plastik", "Gelas plastik", "Kaleng soda", "Botol kaca", "Kertas koran", "CD/DVD bekas", "Ban bekas", "Styrofoam"],
    "B3": ["Pestisida", "Obat nyamuk", "Baterai bekas", "Cat tembok", "Pelumas mesin", "Cairan pembersih", "Produk kimia rumah tangga", "Thermometer merkuri", "Bahan bakar minyak", "Asam sulfat"]
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def fact(ctx, loop = 1):
    """Memberikan fakta menarik tentang sampah."""
    await ctx.send(get_fact(loop))

@bot.command()
async def contoh(ctx, jenis):
    """Memberikan contoh dari jenis sampah."""
    await ctx.send(get_contoh(jenis))

@bot.command()
async def info(ctx, jenis):
    """Memberikan pengertian dari jenis sampah."""
    await ctx.send(get_info(jenis))

@bot.command()
async def tips(ctx, loop = 1):
    """Memberikan pengertian dari jenis sampah."""
    await ctx.send(get_tips(loop))

jawaban = ""

@bot.command()
async def sortir(ctx):
    global jawaban
    """Memberikan pertanyaan tentang jenis sampah"""
    sampah_acak = random.choice(list(jenis_sampah.values()))
    item_sampah_acak = random.choice(sampah_acak)
    if item_sampah_acak in jenis_sampah["Anorganik"]:
        jawaban = "Anorganik"
    elif item_sampah_acak in jenis_sampah["Organik"]:
        jawaban = "Organik"
    else:
        jawaban = "B3"
    await ctx.send(f"**{item_sampah_acak}** merupakan sampah jenis apa ?\n\nJawabannya ==> ||       {jawaban}       ||")

bot.run(token)
