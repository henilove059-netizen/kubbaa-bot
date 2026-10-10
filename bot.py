from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8306704439:AAFmybUJD3wMbeHQn1LmxMPRmxGz2-jNOn4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Akkam jirtu! ⚽\n"
        "Baga gara Kubbaa Bot Afaan Oromoo dhuftan!\n"
        "Oduu kubbaa miilaa argachuuf nu hordofaa."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Kubbaa Bot jalqabe!")
app.run_polling()