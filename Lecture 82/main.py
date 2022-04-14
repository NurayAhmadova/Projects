from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
import random

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get('EMAIL_USER'),
    "MAIL_PASSWORD": os.environ.get('EMAIL_PASSWORD'),
}

app.config.update(mail_settings)
mail = Mail(app)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


def send_contact_form(results):
    msg = Message("Contact Form from Website",
                  sender="python.test.n.a@gmail.com",
                  recipients=["python.test.n.a@gmail.com", "nuray.akhmedova@gmail.com"])

    msg.body = """
    Hello,
    
    You have just received a contact form.
    
    Name: {}
    Email: {}
    Message: {}
    
    Regards,
    
    """.format(results['name'], results['email'], results['message'])
    mail.send(msg)


@app.route('/')
def home():
    random_var = random.randint(10000, 100000)
    print(random_var)
    return render_template("index.html", random_var=random_var)


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        results = {
            "name": request.form['name'],
            "email": request.form['email'].replace(' ', '').lower(),
            "message": request.form['message'],
        }
        send_contact_form(results)
        flash("Message submitted successfully!")
        return render_template("contact.html")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
