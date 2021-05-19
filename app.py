from flask import Flask, app,render_template,request
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='rajafaseehuzz@gmail.com'
app.config['MAIL_PASSWORD']='ykkxpkkoftsvgifp'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail =Mail(app)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/send_mail',methods=['GET','POST'])
def send_mail():
    if request.method== 'POST':
        email = request.form['eml']
        subject = request.form['sub']
        email_body = request.form['msg']
        message_to_be_sent = Message(subject,sender="rajafaseehuzz@gmail.com",recipients=[email])
        message_to_be_sent.body = email_body
        mail.send(message_to_be_sent)

        # success message '
        return render_template('success.html',email=email,subject=subject,message=email_body)

