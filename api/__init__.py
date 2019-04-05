from flask import Flask, redirect
from .views.user_views import user
from .views.message_views import message


app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(message)