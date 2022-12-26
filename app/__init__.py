from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = '3e7bf39c2f9a3470ee4d10cc96685b36'

from app import routes