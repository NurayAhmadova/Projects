from mailer import Mailer

mail = Mailer(email='someone@gmail.com', password='your_password')
mail.send(receiver='someone@example.com', subject='TEST', message='From Python!')