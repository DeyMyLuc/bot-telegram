from dotenv import load_dotenv
import os
import random
import threading
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN não encontrado! Configure a variável de ambiente.")

bot = telebot.TeleBot(TOKEN)

usuarios = set()
compradores = set()

# ── Helper de botões ──────────────────────────────────
def make_markup(*botoes):
    markup = InlineKeyboardMarkup()
    for texto, url in botoes:
        markup.add(InlineKeyboardButton(texto, url=url))
    return markup

# ── Upsell 1: desconto (10 min após /start) ───────────
def upsell_desconto(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("🔥 Garantir com desconto agora", "https://seu-link-desconto.com"),
    )
    texto = (
        "Ei... vi que você ainda não garantiu seu acesso. 👀\n\n"
        "Vou ser honesta: separei um desconto especial só para você.\n\n"
        "💎 Mesmo acesso VIP completo por um valor menor.\n\n"
        "⏳ Mas essa condição some em breve!"
    )
    bot.send_message(chat_id, texto, reply_markup=markup)
    threading.Timer(900, oferta_relampago, args=[chat_id]).start()

# ── Upsell 2: oferta relâmpago (15 min depois) ────────
def oferta_relampago(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("🔥 RESGATAR MINHA OFERTA 🔥", "https://seu-link-final.com"),
    )
    texto = (
        "🚨🔥 OFERTA RELÂMPAGO LIBERADA 🔥🚨\n\n"
        "Espere... antes de ir embora, preciso te mostrar uma coisa. 👀\n\n"
        "Consegui liberar uma condição especial por tempo limitado. 🎁\n\n"
        "✅ Mesmo acesso completo\n"
        "✅ Mesmos benefícios\n"
        "✅ Liberação imediata\n\n"
        "⚠️ Esta oferta não ficará disponível para sempre.\n\n"
        "👇 Aproveite agora:"
    )
    bot.send_message(chat_id, texto, reply_markup=markup)

# ── /start: pitch de vendas ───────────────────────────
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    usuarios.add(message.from_user.id)

    markup = make_markup(
        ("Plano Premium 😈 por R$ 14,99", "https://seu-link-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 21,99", "https://seu-link-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 29,99", "https://seu-link-plano3.com"),
    )
    texto = (
        "💋 Se você chegou até aqui, é porque quer me conhecer muito além do Instagram...\n"
        "E eu confesso que adoro surpreender quem entra no meu VIP. 😈\n\n"
        "Você chegou até aqui porque algo em mim chamou sua atenção... 😉\n\n"
        "Agora imagine ter acesso ao meu conteúdo mais exclusivo em um lugar privado, "
        "longe das limitações das redes sociais. 🔥\n\n"
        "💋 Conteúdos exclusivos\n"
        "📸 Atualizações frequentes\n"
        "🎁 Bônus especiais para membros\n"
        "🔒 Acesso privado\n"
        "❤️ Experiência mais próxima\n\n"
        "Milhares de pessoas visitam meu perfil, mas apenas uma parte tem acesso ao meu VIP. ✨\n\n"
        "Hoje você pode fazer parte desse grupo.\n\n"
        "👇 Escolha seu plano e entre agora."
    )
    bot.send_message(chat_id, texto, reply_markup=markup)
    threading.Timer(600, upsell_desconto, args=[chat_id]).start()

# ── /ajuda ────────────────────────────────────────────
@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.reply_to(message,
        "Comandos Disponíveis:\n"
        "/start - Ver planos VIP\n"
        "/ajuda - Ver comandos\n"
        "/piada - Receber piada\n"
    )

# ── /piada ────────────────────────────────────────────
@bot.message_handler(commands=['piada'])
def piada(message):
    bot.reply_to(message,
        "Por que o programador usa óculos?\n"
        "Porque não consegue C# (sharp = nítido)! 😂"
    )

# ── /avisar: envia mensagem para todos os usuários ────
@bot.message_handler(commands=['avisar'])
def avisar(message):
    for usuario_id in usuarios:
        bot.send_message(usuario_id, "Bom dia! Sinta-se orgulhoso por estar na minha presença, seu humano!")
    bot.reply_to(message, f"Enviado para {len(usuarios)} usuários!")

# ── Responder mensagens genéricas ─────────────────────
@bot.message_handler(func=lambda message: True)
def responder(message):
    usuarios.add(message.from_user.id)
    bot.reply_to(message,
        "Oi! Tudo bem? 😊\n"
        "Use /start para ver o que sei fazer!"
    )

print("Bot rodando!")
bot.infinity_polling()
