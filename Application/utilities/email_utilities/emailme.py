import os,imaplib
import traceback
from imbox import Imbox
from datetime import datetime,timedelta,date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import utilities
from email.utils import parsedate_to_datetime
def emailing(option,candida):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "shahriyarbabaki@gmail.com"
    smtp_password = "eqncfacmxqwxkgrz"
    from_email = "shahriyarbabaki@gmail.com"
    to_email = candida
    if str(option)=="sending":
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            for email_one in to_email:
                msg = MIMEMultipart()
                msg['Subject'] = 'Congratulation'
                msg['From'] = from_email
                msg['To'] = email_one
                name = email_one.split('@')[0]
                message = MIMEText(utilities.body_name(name,"first"), 'html')
                msg.attach(message)
                attachment_path ="question.py"
                # Create file attachment
                with open(attachment_path, 'rb') as attachment:
                    attachment_mime = MIMEApplication(attachment.read(), _subtype=os.path.splitext(attachment_path)[1][1:])
                    attachment_mime.add_header('Content-Disposition', 'attachment', filename=f"{name}.py")
                    msg.attach(attachment_mime)
                server.sendmail(from_email,email_one, msg.as_string())
                msg.set_payload([])
                sent_time = datetime.now()
                mongo_data={"recipient":email_one,"sent_time":sent_time,"receive_time":[]}
                utilities.mongoimportinsert(mongo_data,"hushHush","Email")
                del msg['To']
                del msg['From']
                del msg['Subject']
    elif str(option)=="searching":
         searching(to_email,smtp_username,smtp_password)
def searching(emails,smtp_username,smtp_password):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(smtp_username, smtp_password)
    imap.select("INBOX")
    download_folder = "downloaded_answer"
    today = date.today()
    minute_ago = today - timedelta(minutes=2)
    if not os.path.isdir(download_folder):
        os.makedirs(download_folder, exist_ok=True)
    mail_through = Imbox("imap.gmail.com", username=smtp_username, password=smtp_password, ssl=True, ssl_context=None, starttls=False)
    #messages = mail_through.messages(date__gt=minute_ago)
    for each_email in emails:
        messages = mail_through.messages(unread=True,sent_from=each_email,date__gt=minute_ago)
        name=each_email.split('@')[0]
        try:
            for (uid, message) in messages:
                mail_through.mark_seen(uid) # optional, mark message as read
                for idx, attachment in enumerate(message.attachments):
                    try:
                        att_fn = attachment.get('filename')
                        try:
                            file_name=att_fn.split('.py')[0]
                            if file_name==name:
                                download_path = f"{download_folder}/{att_fn}"
                                with open(download_path, "wb") as fp:
                                    fp.write(attachment.get('content').read())
                                received_header = message.date
                                received_time=parsedate_to_datetime(received_header)
                                #print(each_email)
                                mongo_data={"recipient":each_email,"receive_time":received_time}
                                filtering={"recipient":each_email}
                                utilities.mongoimportupdate(mongo_data,filtering,"hushHush","Email")
                                client=utilities.mongo_local()
                                db=client.hushHush
                                collection = db.Email
                                emails_find= collection.find({
                                "recipient":each_email
                                })
                                for email in emails_find:
                                    #print(email)
                                    time_diff = email["receive_time"] - email["sent_time"]
                                    if time_diff < timedelta(days=14):
                                        mongo_data={"recipient":each_email,"In_time":True}
                                        filtering={"recipient":each_email}
                                        utilities.mongoimportupdate(mongo_data,filtering,"hushHush","Email")
                                    else:
                                        mongo_data={"recipient":each_email,"In_time":False}
                                        filtering={"recipient":each_email}
                                        utilities.mongoimportupdate(mongo_data,filtering,"hushHush","Email")
                        except:
                            None
                    except:
                        print(traceback.print_exc())
        except:
            None
    mail_through.logout()
#emails=["shahriyarbabaki@gmail.com"]
#emails=["mohamadreza.yazdankhah@gmail.com","mmorbajgiran@gmail.com","dnlbabaki@gmail.com"]
#emailing("searching",emails)
#utilities.emailing_final(emails[0],"failed")
