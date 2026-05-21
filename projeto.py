from dotenv import load_dotenv
import os
import random
import telebot

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Comando /start - mensagem de boas-vindas
@bot.message_handler(commands=['perguntar'])
def perguntar(message):
    nome = message.from_user.first_name
    bot.reply_to(message,f'Olá, {nome}! 👋\nSou seu bot Python. Como posso ajudar?',)

# Comando /ajuda - lista de comandos
@bot.message_handler(commands=['start'])
def ajuda(message):
            bot.reply_to(message,"Comandos Disponiveis\n"
            "/perguntar - Iniciar o bot \n"
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
        "Use /start para ver o que sei fazer!"
    )
# Permitir o bot funcionar em grupos
@bot.message_handler(commands=['grupos'])
def grupos(message): # Já roda automaticamente  em grupos
     usuarios = [] #Lista de IDs
@bot.message_handler(commands=['avisar'])
def avisar (message):
    for usuarios_id in usuarios:
    if message.chat.id not in usuarios:
        usuarios.append(message.chat.id)
    bot.send_message(usuario_id, "Bom dia! sentia-se orgulhoso por estar na minhas preseça seu humano!")

usuarios = set() #Relatorio de usuarios
@bot.message_handler(func=lambda m: true)
def responder(message):
    usuarios.add(message.from_user.id)
    print(f"total de usuarios: {len(usuarios)}")

print ("bot rodando!")
bot.infinity_polling()
