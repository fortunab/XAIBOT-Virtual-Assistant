from flask import Flask, render_template, request

import functii
import manipulareYaml

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/corpus")
def corpusul():
    return "AB"

@app.route("/detectare")
def detect_referinte():
    userText = request.args.get('msg')
    if userText.lower() == "q":
        return 'Well, you just saw how things are going. ' \
               'I detected references. It was a strange conversation, between a human and me. I am glad that I met you. ' \
               'Now, I have to work on my abilities. See you soon. ' \
               'If you have more questions or doubts, please comeback to the application. ' \
               'Bye!'
    return functii.referinte(userText)

@app.route("/name", methods=["GET"])
def name():
    userText = request.args.get('msg')
    return functii.nume(userText)
#render_template('nimic.html', userText=userText)

@app.route("/discut")
def dialog():
    userText = request.args.get('msg')
    return functii.convorbireIT(userText)

@app.route("/discut_modif")
def dialogRef():
    userText = request.args.get('msg')
    return functii.convorbireREF(userText)

@app.route("/ceva", methods=["GET"])
def ceva():
    cv = request.args.get('msg')
    return render_template("index.html", cv=cv)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText.lower() == "exit":
        return 'Well, you just saw how things are going. ' \
               'I just talked with you about XAI and my reason. ' \
               'It was a strange conversation, between a human and me. I am glad that I met you. ' \
               'Now, I have to work on my abilities. See you soon. ' \
               'If you have more questions or doubts, please comeback to the application. ' \
               'Bye!'
    return manipulareYaml.convorbireXAI(userText)

if __name__ == "__main__":
    app.run()