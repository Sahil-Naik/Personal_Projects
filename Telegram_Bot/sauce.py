from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Get Bot Setup from BotFather on Telegram

Token: Final = # Your Bot API

Bot_USERNAME: Final = # Your Bot Name

#--------------- Commands ----------------

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text("Hello! Thanks for choosing me. I'm Bot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text("How can I help you?")

#--------------- Responses ----------------

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello there!'

    elif 'how are you' in processed:
        return 'I am Good!'

    else:
        return 'Sorry I do not understand what you wrote.'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if Bot_USERNAME in text:
            new_text: str = text.replace(Bot_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:',response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Staring Bot...")
    app = Application.builder().token(Token).build()

    # Commands
    app.add_handler(CommandHandler('Start', start_command))
    app.add_handler(CommandHandler('Help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)
