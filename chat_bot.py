TOKEN = "8145703136:AAHp1JSimU62L8GUSPAy5JEjWWqM24yLU2Y"

import os
import random

import telebot
from telebot.types import BotCommand

from pydub import AudioSegment
import speech_recognition as sr

from gtts import gTTS

# TOKEN = "TU_TOKEN_AQUÍ"
bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Holaaaaaaa! Soy tu bot de TeleBot. Usa /ayuda para ver lo que puedo hacer.")

# Comando /ayuda
@bot.message_handler(commands=['ayuda'])
def send_help(message):
    bot.reply_to(message, "Comandos disponibles:\n/start - Inicia el bot\n/ayuda - Muestra esta ayuda\n/edad <tu edad> - Calcula cuántos días has vivido")


@bot.message_handler(commands=['motivacion'])
def motivacion(message):
    frases = [
        "¡Sigue adelante, lo estás haciendo genial!",
        "Recuerda, cada día es una nueva oportunidad.",
        "Nunca dejes de aprender y crecer.",
    ]
    bot.reply_to(message, random.choice(frases))

# Comando /edad
@bot.message_handler(commands=['edad'])
def calculate_age(message):
    try:
        # Extraer la edad de los argumentos del comando
        edad = int(message.text.split()[1])
        dias_vividos = edad * 365
        bot.reply_to(message, f"Has vivido aproximadamente {dias_vividos} días.")
    except (IndexError, ValueError):
        bot.reply_to(message, "Por favor, usa el comando así: /edad <tu edad>")

@bot.message_handler(commands=['audio'])
def text_to_audio(message):
    try:
        # Extraer el texto después del comando
        text = message.text[len('/audio '):].strip()
        if not text:
            bot.reply_to(message, "Por favor, envíame un texto para convertir a audio. Ejemplo: /audio Hola, ¿cómo estás?")
            return

        # Convertir texto a audio
        tts = gTTS(text, lang='es')
        audio_file = "response.mp3"
        tts.save(audio_file)

        # Enviar el audio al usuario
        with open(audio_file, 'rb') as audio:
            bot.send_voice(message.chat.id, audio)

        # Limpiar archivo temporal
        os.remove(audio_file)

    except Exception as e:
        bot.reply_to(message, f"No pude generar el audio: {str(e)}")


# Manejo de mensajes de texto
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Me dijiste: {message.text}")


def set_commands():
    commands = [
        BotCommand("start", "Inicia el bot"),
        BotCommand("ayuda", "Muestra la ayuda"),
        BotCommand("edad", "Calcula los días vividos"),
        BotCommand("motivacion", "Envía una frase motivadora"),
        BotCommand("audio", "Convierte texto a audio"), 
    ]
    bot.set_my_commands(commands)


# Manejar mensajes de audio
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        # Descargar el archivo de audio
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        audio_file = "voice.ogg"

        with open(audio_file, 'wb') as f:
            f.write(downloaded_file)

        # Convertir el archivo OGG a WAV
        sound = AudioSegment.from_file(audio_file, format="ogg")
        wav_file = "voice.wav"
        sound.export(wav_file, format="wav")

        # Reconocer el texto del audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="es-ES")

        bot.reply_to(message, f"Texto reconocido: {text}")

        # Limpiar archivos temporales
        os.remove(audio_file)
        os.remove(wav_file)

    except Exception as e:
        bot.reply_to(message, f"No pude procesar el audio: {str(e)}")



# Configurar los comandos al iniciar el bot
set_commands()

# Iniciar el bot
print("El bot está funcionando...")
bot.polling()
