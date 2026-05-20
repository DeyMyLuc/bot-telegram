from dotenv import load_dotenv
import os
import random
import telebot

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Comando /start - mensagem de boas-vindas
@bot.message_handler(commands=['start'])
def start(message):
    nome = message.from_user.first_name
    bot.reply_to(message,f'Olá, {nome}! 👋\nSou seu bot Python. Como posso ajudar?',)

# Comando /ajuda - lista de comandos
@bot.message_handler(commands=['ajuda'])
def ajuda(message):
            bot.reply_to(message,"Comandos Disponiveis\n"
            "/start - Iniciar o bot \n"
            "/ajuda - Ver comandos\n"
            "/piada - Receber piada\n")
# Comenado /piada - conta uma piada
@bot.message_handler(commands=['piada'])
def piada(message):
        bot.reply_to(message, "Por que o programador usa óculos? \n"
        "Porque não consegue C# (sharp=nítido)!"
    )
#Responder mensagens simples
@bot.message_handler(func=lambda message: True)
def responder(message):
    bot.reply_to(message,f'Oi! Tudo bem? 😊'
        "Use /ajuda para ver o que sei fazer!"
    )
print ("bot rodando!")
bot.infinity_polling()
