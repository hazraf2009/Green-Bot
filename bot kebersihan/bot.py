import discord
from discord.ext import commands
from discord.ui import Button, View
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


# masih belajar belum bisa dibilang sempurna(coba-coba)
jumlah_soal = 0
betul = 0
salah = 0
sampah_acak = random.choice(list(jenis_sampah.values()))
item_sampah_acak = random.choice(sampah_acak)
@bot.command()
async def sortir(ctx):
    """Memberikan pertanyaan tentang jenis sampah"""
    
    
    
    async def button_callback(interaction: discord.Interaction):
        global jumlah_soal, betul, salah, sampah_acak, item_sampah_acak
        custom_id = interaction.data["custom_id"]
        
        if custom_id == "anorganik" and item_sampah_acak in jenis_sampah["Anorganik"]:
            await interaction.response.edit_message(content="Benar! Ini adalah sampah Anorganik.")
            
            jumlah_soal += 1
            betul += 1
            sampah_acak = random.choice(list(jenis_sampah.values()))
            item_sampah_acak = random.choice(sampah_acak)

            await interaction.followup.send(f"**{item_sampah_acak}** merupakan sampah jenis apa?", view=view)
            
        elif custom_id == "organik" and item_sampah_acak in jenis_sampah["Organik"]:
            await interaction.response.edit_message(content="Benar! Ini adalah sampah Organik.")
            
            jumlah_soal += 1
            betul += 1
            sampah_acak = random.choice(list(jenis_sampah.values()))
            item_sampah_acak = random.choice(sampah_acak)

            await interaction.followup.send(f"**{item_sampah_acak}** merupakan sampah jenis apa?", view=view)
            
        elif custom_id == "b3" and item_sampah_acak in jenis_sampah["B3"]:
            await interaction.response.edit_message(content="Benar! Ini adalah sampah B3.")
             
            jumlah_soal += 1
            betul += 1
            sampah_acak = random.choice(list(jenis_sampah.values()))
            item_sampah_acak = random.choice(sampah_acak)

            await interaction.followup.send(f"**{item_sampah_acak}** merupakan sampah jenis apa?", view=view)
        
        elif custom_id == "keluar":
            await interaction.response.send_message(f"**Scoremu :**\n**Jumlah Soal :** {jumlah_soal}\n**Betul :** {betul}\n**Salah :** {salah}")
           
        else:
            await interaction.response.edit_message(content="Salah! Coba lagi.")
            
            jumlah_soal += 1
            salah += 1
            sampah_acak = random.choice(list(jenis_sampah.values()))
            item_sampah_acak = random.choice(sampah_acak)

            await interaction.followup.send(f"**{item_sampah_acak}** merupakan sampah jenis apa?", view=view)
    
    button_anorganik = Button(label="Anorganik", custom_id="anorganik")
    button_organik = Button(label="Organik", style=discord.ButtonStyle.green, custom_id="organik")
    button_b3 = Button(label="B3", style=discord.ButtonStyle.red, custom_id="b3")
    button_keluar = Button(label="Keluar", emoji="❌", custom_id="keluar")
    
    button_anorganik.callback = button_callback
    button_organik.callback = button_callback
    button_b3.callback = button_callback
    button_keluar.callback = button_callback

    view = View()
    view.add_item(button_anorganik)
    view.add_item(button_organik)
    view.add_item(button_b3)
    view.add_item(button_keluar)
    
    await ctx.send(f"**{item_sampah_acak}** merupakan sampah jenis apa?", view=view)

bot.run(token)
