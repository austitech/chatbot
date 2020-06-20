
from flask import Flask, render_template, request

from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer


# create flask app object
app = Flask(__name__)

# create chatbot
bot = ChatBot("HNGi7-Bot")

# configure chatbot
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


# create flask routes
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg")
    return str(bot.get_response(user_text))


if __name__ == "__main__":
    app.run()
