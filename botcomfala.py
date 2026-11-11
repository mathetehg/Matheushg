import discord  #discord
from discord.ext import commands  
import requests  
import pyttsx3  #sintese de fala

#inicializando o bot
intents = discord.Intents.default()
intents.message_content = True  # Para ler mensagens
bot = commands.Bot(command_prefix="!", intents=intents)

#inicializando o motor de sintese de fala (pyttsx3)
engine = pyttsx3.init()
language = 'pt'

def speak(text: str):
    #função para converter texto em fala
    engine.say(text)
    engine.runAndWait()

#função para buscar um fato interessante na API
def get_fact() -> str:
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    
    
    print(response.json())

    if response.status_code == 200:
        data = response.json()
        return data.get("text", "Não foi possível encontrar um fato.")
    else:
        return f"Erro ao buscar a curiosidade. Código de status: {response.status_code}"

# Função de clima (já presente no seu código)
def get_weather(city: str) -> str:
    base_url = f"https://wttr.in/{city}?format=%C+%t" 
    response = requests.get(base_url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Não foi possível obter a previsão do tempo."

# Etapa 1: Manipulador de comandos !start atualizado
@bot.command()
async def start(ctx):
    await ctx.send("Olá! Sou seu assistente em Python. Use `!fact` para ver um fato interessante ou `!weather <cidade>` para a previsão do tempo!")

# Comando !fact com síntese de fala
@bot.command()
async def fact(ctx):
    fact_text = get_fact()
    await ctx.send(f"💡 Fato interessante: {fact_text}")
    
    # Lê o fato em voz alta no momento em que o bot envia a mensagem
    speak(fact_text)

@bot.command()
async def weather(ctx, *, city: str):
    weather_info = get_weather(city)
    await ctx.send(f"Previsão do tempo para {city}: {weather_info}")

# Executando o bot (substitua pelo seu token se for usar :] )
bot.run("token")

