from dotenv import load_dotenv
import os
import threading
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

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

def make_callback_markup(*botoes):
    markup = InlineKeyboardMarkup()
    for texto, callback in botoes:
        markup.add(InlineKeyboardButton(texto, callback_data=callback))
    return markup

# ── /start: texto + botão VIP ─────────────────────────
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    usuarios.add(message.from_user.id)

    markup = make_callback_markup(
        ("🔥 QUERO ACESSAR O VIP 🔥", "ver_oferta"),
    )

    bot.send_message(
        chat_id,
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
        "Milhares de pessoas visitam meu perfil, mas apenas uma parte delas tem acesso ao meu VIP. ✨\n\n"
        "Hoje você pode fazer parte desse grupo.\n\n"
        "👇 Escolha seu plano e entre agora.",
        reply_markup=markup
    )

# ── Callback: clicou em QUERO ACESSAR O VIP ───────────
@bot.callback_query_handler(func=lambda call: call.data == "ver_oferta")
def ver_oferta(call):
    chat_id = call.message.chat.id
    bot.answer_callback_query(call.id)

    markup = make_markup(
        ("Plano Premium 😈 por R$ 14,49", "https://seu-link-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 19,90", "https://seu-link-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 27,49", "https://seu-link-plano3.com"),
    )

    with open("Imagem1.jpg", "rb") as foto:
        bot.send_photo(
            chat_id,
            photo=foto,
            caption=(
                "🔥 Aqui está sua oferta exclusiva!\n\n"
                "Escolha o plano ideal para você e garanta seu acesso agora. 👇"
            ),
            reply_markup=markup
        )

    with open("video.mp4", "rb") as vid:
        bot.send_video(
            chat_id,
            video=vid,
            caption="🔥 Prévia exclusiva do que te espera dentro do VIP..."
        )

    threading.Timer(600, upsell_1, args=[chat_id]).start()

# ── Upsell 1 (10min) — 5% de desconto ────────────────
def upsell_1(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("Plano Premium 😈 por R$ 13,77", "https://seu-link-u1-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 18,91", "https://seu-link-u1-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 26,12", "https://seu-link-u1-plano3.com"),
    )
    medias = [
        InputMediaPhoto(open("Imagem2.jpg", "rb"), caption=(
            "Ei... vi que você ainda não garantiu seu acesso. 👀\n\n"
            "Separei um desconto especial só para você! 🎁\n\n"
            "🔥 5% OFF por tempo limitado:\n"
            "😈 Premium: de R$ 14,49 por R$ 13,77\n"
            "😘 Premium + Vídeo: de R$ 19,90 por R$ 18,91\n"
            "🔥 Completo + Bônus: de R$ 27,49 por R$ 26,12\n\n"
            "⏳ Essa condição some em breve!"
        )),
        InputMediaPhoto(open("Imagem3.jpg", "rb")),
    ]
    bot.send_media_group(chat_id, medias)
    bot.send_message(chat_id, "👇 Garanta agora antes que acabe!", reply_markup=markup)

    threading.Timer(900, upsell_2, args=[chat_id]).start()

# ── Upsell 2 (15min) — 13% de desconto ───────────────
def upsell_2(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("Plano Premium 😈 por R$ 12,61", "https://seu-link-u2-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 17,31", "https://seu-link-u2-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 23,92", "https://seu-link-u2-plano3.com"),
    )
    medias = [
        InputMediaPhoto(open("Imagem4.jpg", "rb"), caption=(
            "✨ Olha o que você ainda está perdendo...\n\n"
            "Aumentei o desconto só para você! 💎\n\n"
            "🔥 13% OFF:\n"
            "😈 Premium: de R$ 14,49 por R$ 12,61\n"
            "😘 Premium + Vídeo: de R$ 19,90 por R$ 17,31\n"
            "🔥 Completo + Bônus: de R$ 27,49 por R$ 23,92\n\n"
            "⚠️ Aproveite antes que essa oferta acabe!"
        )),
        InputMediaPhoto(open("Imagem5.jpg", "rb")),
    ]
    bot.send_media_group(chat_id, medias)
    bot.send_message(chat_id, "👇 Não deixa essa oportunidade passar!", reply_markup=markup)

    threading.Timer(900, upsell_3, args=[chat_id]).start()

# ── Upsell 3 (15min) — 21% de desconto ───────────────
def upsell_3(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("Plano Premium 😈 por R$ 11,45", "https://seu-link-u3-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 15,72", "https://seu-link-u3-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 21,72", "https://seu-link-u3-plano3.com"),
    )
    medias = [
        InputMediaPhoto(open("Imagem6.jpg", "rb"), caption=(
            "👀 Mais uma prévia do que te espera...\n\n"
            "Esse desconto não vai durar muito! 🚨\n\n"
            "🔥 21% OFF:\n"
            "😈 Premium: de R$ 14,49 por R$ 11,45\n"
            "😘 Premium + Vídeo: de R$ 19,90 por R$ 15,72\n"
            "🔥 Completo + Bônus: de R$ 27,49 por R$ 21,72\n\n"
            "⏳ Depois disso o valor volta ao normal!"
        )),
        InputMediaPhoto(open("Imagem7.jpg", "rb")),
    ]
    bot.send_media_group(chat_id, medias)
    bot.send_message(chat_id, "👇 Garanta agora com 21% OFF!", reply_markup=markup)

    threading.Timer(900, upsell_4, args=[chat_id]).start()

# ── Upsell 4 (15min) — 29% de desconto ───────────────
def upsell_4(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("Plano Premium 😈 por R$ 10,99", "https://seu-link-u4-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 14,13", "https://seu-link-u4-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 19,52", "https://seu-link-u4-plano3.com"),
    )
    medias = [
        InputMediaPhoto(open("Imagem8.jpg", "rb"), caption=(
            "💋 Ei... ainda estou aqui te esperando. 😈\n\n"
            "Liberando mais desconto para você entrar agora!\n\n"
            "🔥 29% OFF:\n"
            "😈 Premium: de R$ 14,49 por R$ 10,99\n"
            "😘 Premium + Vídeo: de R$ 19,90 por R$ 14,13\n"
            "🔥 Completo + Bônus: de R$ 27,49 por R$ 19,52\n\n"
            "⚠️ Essa é uma oportunidade que poucas pessoas têm!"
        )),
        InputMediaPhoto(open("Imagem2.jpg", "rb")),
    ]
    bot.send_media_group(chat_id, medias)
    bot.send_message(chat_id, "👇 Entre agora antes que seja tarde!", reply_markup=markup)

    threading.Timer(900, upsell_5, args=[chat_id]).start()

# ── Upsell 5 (15min) — Imagem1 + vídeo (37% OFF) ─────
def upsell_5(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("Plano Premium 😈 por R$ 10,99", "https://seu-link-u5-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 12,54", "https://seu-link-u5-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 17,32", "https://seu-link-u5-plano3.com"),
    )

    with open("Imagem1.jpg", "rb") as foto:
        bot.send_photo(
            chat_id,
            photo=foto,
            caption=(
                "💋 Não quero que você vá embora sem ver isso mais uma vez...\n\n"
                "Liberei o maior desconto até agora! 🎁\n\n"
                "🔥 37% OFF:\n"
                "😈 Premium: de R$ 14,49 por R$ 10,99\n"
                "😘 Premium + Vídeo: de R$ 19,90 por R$ 12,54\n"
                "🔥 Completo + Bônus: de R$ 27,49 por R$ 17,32\n\n"
                "👇 Escolha seu plano agora."
            ),
            reply_markup=markup
        )

    with open("video.mp4", "rb") as vid:
        bot.send_video(
            chat_id,
            video=vid,
            caption="🔥 Lembra dessa prévia? É só o começo do que te espera..."
        )

    threading.Timer(900, upsell_6, args=[chat_id]).start()

# ── Upsell 6 (15min) — RELÂMPAGO FINAL 40% OFF ───────
def upsell_6(chat_id):
    if chat_id in compradores:
        return

    markup = make_markup(
        ("Plano Premium 😈 por R$ 10,99", "https://seu-link-u6-plano1.com"),
        ("Premium + Vídeo 😘 por R$ 11,94", "https://seu-link-u6-plano2.com"),
        ("Completo + Bônus 🔥 por R$ 16,49", "https://seu-link-u6-plano3.com"),
    )
    medias = [
        InputMediaPhoto(open("Imagem3.jpg", "rb"), caption=(
            "🚨🔥 OFERTA RELÂMPAGO — ÚLTIMO DESCONTO! 🔥🚨\n\n"
            "Essa é a minha oferta final para você. 👀\n\n"
            "🔥 40% OFF — maior desconto possível:\n"
            "😈 Premium: de R$ 14,49 por R$ 10,99\n"
            "😘 Premium + Vídeo: de R$ 19,90 por R$ 11,94\n"
            "🔥 Completo + Bônus: de R$ 27,49 por R$ 16,49\n\n"
            "✅ Mesmo acesso completo\n"
            "✅ Liberação imediata\n\n"
            "⚠️ Esta oferta some em instantes. Não perca!"
        )),
        InputMediaPhoto(open("Imagem4.jpg", "rb")),
    ]
    bot.send_media_group(chat_id, medias)
    bot.send_message(chat_id, "👇 Aproveite agora enquanto sua oferta continua ativa:", reply_markup=markup)

# ── /ajuda ────────────────────────────────────────────
@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    bot.reply_to(message,
        "Comandos Disponíveis:\n"
        "/start - Iniciar o bot\n"
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

# ── /avisar ───────────────────────────────────────────
@bot.message_handler(commands=['avisar'])
def avisar(message):
    for usuario_id in usuarios:
        bot.send_message(usuario_id, "📢 Nova mensagem para todos os membros!")
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
