from flask import Flask,request
from telegram import Bot
from app import start
from settings import TOKEN

app=Flask(__name__)

@app.route("/",methods=["POST"])
def home():
    if request.method=="POST":
        data=request.get_json()
        text=data["message"]["text"]
        chat_id=data["message"]["chat"]["id"]
        if text=="/start":
            start(chat_id,data["message"]["first_name"])
        return "Ok"

if __name__=="__main__":
    app.run(debug=True)