import discord
import random
import os
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def topla(ctx , sayi1:int, sayi2:int):
    await ctx.send(f'Sonuç: {sayi1 + sayi2}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ayrisma(ctx, *, esya=None):
    if esya is None:
        await ctx.send("Lütfen ayrışma süresini öğrenmek istediğin eşyayı yaz! Örnek: `$ayrisma plastik şişe`")
        return

    esya = esya.lower().strip()

    sureler = {
        "plastik": "Plastik ürünlerin doğada yok olması yaklaşık 450 yıl sürer!",
        "plastik şişe": "Plastik şişelerin doğada yok olması yaklaşık 450 yıl sürer!",
        "cam": "Cam şişe ve kavanozların doğada kaybolması 4000 yıldan uzun sürer.",
        "pil": "Pillerin doğada yok olması yaklaşık 100 yıl sürer ve toprağa zehirli maddeler bırakır.",
        "kagit": "Kağıt doğada ortalama 2 ila 6 haftada çözünür.",
        "alüminyum": "Alüminyum kutular doğada 200 ila 500 yıl arasında kaybolur."}

@bot.command()
async def copkutusu(ctx,esya=None,a=None):
    if esya == None:
        await ctx.send("Lütfen hangi cop kutusuna atman lazim oldugunu bilmek istedigini esya tipini yaz!")
        return

    esya = esya.lower().strip()

    ayrimlar = {
        "cam":"beyaz kutu",
        "kahverengi":"organik atik",
        "mavi":"kagit",
        "gri":"ev atiklari"}

    if a == None:
        img_name="kylian_dictator.jpg"
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send("sakin yanlis kutuya atma!")
            await ctx.send(file=picture)
          
bot.run("token")
