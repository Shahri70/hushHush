import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import utilities
def emailing_final(email_address,kind):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    subject=None
    if kind=="confirmed":
        subject="GREAT NEWS"
    else:
        subject="TheResult"
    smtp_username = "shahriyarbabaki@gmail.com"
    smtp_password = "eqncfacmxqwxkgrz"
    from_email = "shahriyarbabaki@gmail.com"
    to_email = email_address
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        name = email_address.split('@')[0]
        message = MIMEText(utilities.body_name(name,kind), 'html')
        msg.attach(message)
        server.sendmail(from_email,to_email, msg.as_string())
        msg.set_payload([])
        del msg['To']
        del msg['From']
        del msg['Subject']
