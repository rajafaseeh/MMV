from flask import Flask , render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sendEmail')
def sendEmail():

    msg = MIMEMultipart()
    msg['Subject'] = 'Team name,,Group#123'

    body = 'Test email sent from phython and flask'
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()

    email="rajafaseeh204@gmail.com"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("rajafaseehuzz@gmail.com","ykkxpkkoftsvgifp")
    response = server.sendmail("rajafaseehuzz@gmail.com",email,text)
    return "Email sent successfully!!!!"