#import os é apenas se você for uasr o .env para receber o token, como não estamos
#utilizando dessa forma, não é necessário.
import os

#import discord para utilizarmos a biblioteca DISCORD
import discord

#Em alguns casos pode ocorrer erro sem esse Import, por isso foi utilizado.
from discord.ext import commands
intents = discord.Intents(messages=True)


#Criamos uma instância de um Client. Esta é a conexão com o Discord.
client = commands.Bot(command_prefix ='+', intents=intents)

#@client.event() é usado para registrar um evento
@client.event

#evento on_ready() é chamado quando o bot está pronto para começar a ser usado.
async def on_ready():
    print('Nós estamos logados como {0.user}'.format(client))

@client.event
#Quando o bot recebe uma mensagem, o evento on_message() é chamado.

async def on_message(message):
    if message.author == client.user:
        return

#verificamos se o Message.content começa com '$hello'.
# Se começar, o bot responde com um 'Hello!' para o canal em que foi usado.

    if message.content.startswith('+Start'):
        await message.channel.send('O Bot está ATIVO!!')

#Voce substitui pelo TOKEN do seu BOT
client.run('TOKEN')
