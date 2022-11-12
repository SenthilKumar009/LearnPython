# go over to your gmail and enable two factor authentication
# generate app password
# create a function to send an email

from email.message import EmailMessage
from pwd import password
import ssl
import smtplib

email_sender = 'senthilkumark.nitt@gmail.com'
email_password = password

email_receiver = 'kabil.vasu@gmail.com'
email_subject = "Test Mail"
email_body = "This is a Test mail"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

