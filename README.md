## Universidad Politecnica Salesiana
## Ingeniería en Ciencias de la Computación


<img src="assets/ups-icc.png" alt="Logo Carrera" style="height:75px;"/>

#
###
###
# Crear un Bot de Telegram con Python

<img src="assets/logo-Python.png" alt="Logo Carrera" style="height:50px;"/>
<img src="assets/logo-Telegram.png" alt="Logo Carrera" style="height:50px;"/>

En este taller te guiaremos paso a paso para crear un bot de Telegram utilizando la biblioteca `TeleBot`. Incluye instrucciones para obtener el token de acceso, ejecutar el bot y agregar comandos personalizados.

---

## **Paso 1: Crear el Bot en Telegram**

1. Abre la aplicación de Telegram en tu teléfono o en la versión de escritorio.
2. Busca el usuario `BotFather` en Telegram.
3. Inicia una conversación con `BotFather` y usa el comando:
   ```
   /newbot
   ```
4. Sigue las instrucciones:
   - Asigna un nombre a tu bot (por ejemplo, `MiPrimerBot`).
   - Asigna un nombre de usuario único que termine en `bot` (por ejemplo, `MiPrimerBot` o `MiBot123_bot`).
5. Una vez creado, BotFather te proporcionará un **token de acceso**. Este token es esencial para interactuar con la API de Telegram.
   - Ejemplo de token: `123456789:ABCDefGhIjKLmnOpQrStuVWxyZ12345678`

   **¡Importante!** Guarda este token de forma segura.

---

## **Paso 2: Configurar el Entorno de Desarrollo**

1. Asegúrate de tener Python instalado en tu sistema.
   - Para verificarlo, ejecuta:
     ```bash
     python --version
     ```

2. Instala la biblioteca `TeleBot`:
   ```bash
   pip install pyTelegramBotAPI
   ```

---

## **Paso 3: Crear el Bot Básico**

Crea un archivo llamado `bot.py` y copia el siguiente código:

```python
import telebot

# Reemplaza "TU_TOKEN_AQUI" con el token que te dio BotFather
TOKEN = "TU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy tu bot creado en taller de la Universidad Politécnia Salesiana. Escribe algo y te responderé.")

# Manejo de mensajes de texto
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Me dijiste: {message.text}")

# Iniciar el bot
print("El bot está funcionando :) ...")
bot.polling()
```

---

## **Paso 4: Ejecutar el Bot**

1. En la terminal, navega hasta la ubicación del archivo `bot.py`.
2. Ejecuta el bot:
   ```bash
   python bot.py
   ```
3. Si todo está configurado correctamente, deberías ver el mensaje:
   ```
   El bot está funcionando...
   ```

4. Abre Telegram, busca tu bot por el nombre de usuario que configuraste y haz clic en **Iniciar** para interactuar con él.

---

## **Paso 5: Agregar Comandos Personalizados**

### **Comando /ayuda**
Agrega un comando que muestre información útil sobre el bot.

```python
@bot.message_handler(commands=['ayuda'])
def send_help(message):
    bot.reply_to(message, "Comandos disponibles:\n/start - Inicia el bot\n/ayuda - Muestra esta ayuda")
```

### **Comando /edad**
Crea un comando que calcule los días que alguien ha vivido basado en su edad:

```python
@bot.message_handler(commands=['edad'])
def calculate_age(message):
    try:
        # Extraer la edad de los argumentos del comando
        edad = int(message.text.split()[1])
        dias_vividos = edad * 365
        bot.reply_to(message, f"Has vivido aproximadamente {dias_vividos} días.")
    except (IndexError, ValueError):
        bot.reply_to(message, "Por favor, usa el comando así: /edad <tu edad>")
```

---

## **Paso 6: Personalizar el Bot**

1. Cambia el mensaje de bienvenida en `/start`.
2. Agrega más comandos como `/motivacion` que envíe frases aleatorias:
   ```python
   import random

   @bot.message_handler(commands=['motivacion'])
   def motivacion(message):
       frases = [
           "¡Sigue adelante, lo estás haciendo genial!",
           "Recuerda, cada día es una nueva oportunidad.",
           "Nunca dejes de aprender y crecer.",
       ]
       bot.reply_to(message, random.choice(frases))
   ```

---

## **Paso 7: Probar y Mejorar**

- Ejecuta el bot nuevamente y prueba los nuevos comandos.
- Pide a los estudiantes que modifiquen o agreguen más funcionalidades.

---

## **Recursos Adicionales**
- [Documentación oficial de TeleBot](https://github.com/eternnoir/pyTelegramBotAPI)
- [Guía de Telegram Bots](https://core.telegram.org/bots)

