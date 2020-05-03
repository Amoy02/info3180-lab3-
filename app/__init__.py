from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ilikethiscourse'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'b701d163802299'
app.config['MAIL_PASSWORD'] = '3bee5515812b7c'
mail = Mail(app) 

from app import views