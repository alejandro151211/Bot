import discord
from discord.ext import commands
import random
import string
from datetime import datetime


# Configura el prefijo de comandos y los permisos de intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="#", intents=intents)

# Evento: Cuando el bot esté listo
@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

# Comando: Saludo
@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! ¿Cómo estás?")

# Comando: Despedida
@bot.command()
async def adios(ctx):
    await ctx.send("¡Adiós! Nos vemos pronto. ")

@bot.command()
async def comandos(ctx):
    await ctx.send("Los comandos son: #hola, #adios, #contraseña, #chiste1, #chiste2, #chiste3, #chiste4, #chiste5, #fecha, #repetir (despues del repetir tienes que poner lo que quieras que el bot repita), #juego, #comandos (que lo acabas de usar). Se seguiran añadiendo mas comandos por que ahora mismo este bot esta en una fase beta.")

# Comando: Generar contraseña aleatoria
@bot.command()
async def contraseña(ctx):
    # Define los caracteres permitidos
    caracteres = string.ascii_letters + string.digits  # Letras y números
    # Genera una contraseña de 8 caracteres
    contraseña = ''.join(random.choices(caracteres, k=8))
    # Envía el mensaje con la contraseña generada
    await ctx.send(f"🔐 Tu contraseña generada es: `{contraseña}`")

@bot.command()
async def chiste1(ctx):
    await ctx.send("¿Qué le dice una taza a otra? - ¿Qué taza ciendo?")

@bot.command()
async def chiste2(ctx):
    await ctx.send("¿Como se dice 99 en chino? - Cachi cien")

@bot.command()
async def chiste3(ctx):
    await ctx.send("Las ovejas al jugar futbol. Una de ellas lanza muy lejos el balón. Y le dice a otra oveja: Veeeeeeeee!!!! y la otra le dice no, Veeeeeeeeeee tu")

@bot.command()
async def chiste4(ctx):
    await ctx.send("¿Como se dice repollo en ingles? Rechiken")

@bot.command()
async def chiste5(ctx):
    await ctx.send("¿Qué le dice una taza a otra? - ¿Qué taza ciendo?")

@bot.command()
async def gato(ctx):
    await ctx.send(file=discord.File("gato.jpeg"))  # Pon el nombre del archivo de la imagen

@bot.command()
async def juego(ctx):
    numero = random.randint(1, 10)
    await ctx.send("Adivina un número entre 1 y 10.")

    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit()

    try:
        mensaje = await bot.wait_for('message', check=check, timeout=30.0)
        if int(mensaje.content) == numero:
            await ctx.send(f"¡Correcto! El número era {numero}.")
        else:
            await ctx.send(f"¡Incorrecto! El número era {numero}.")
    except asyncio.TimeoutError:
        await ctx.send("¡Se agotó el tiempo para adivinar!")
 
@bot.command()
async def fecha(ctx):
    ahora = datetime.now()  # Obtiene la fecha y hora actual
    fecha = ahora.strftime("%d/%m/%Y")  # Formato: Día/Mes/Año
    hora = ahora.strftime("%H:%M:%S")  # Formato: Horas:Minutos:Segundos
    
    await ctx.send(f"📅 Fecha actual: {fecha}\n⏰ Hora actual: {hora}")

@bot.command()
async def repetir(ctx, *, mensaje: str):
    await ctx.send(mensaje)

# Inicia el bot (coloca tu token aquí)
bot.run("Escribe aqui tu token")
