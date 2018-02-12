import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
email_user = "cdtrasnport@gmail.com"
email_send = "cdtrasnport@gmail.com"
subject = "Checador de Transporte"
msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = email_send
msg["Subject"] = subject
body = "hi i am a test"
msg.attach(MIMEText(body,"plain"))

filename = "Lista_usuarios.csv"
attachment = open(filename, "rb")
part = MIMEBase("application", "aoctet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("content-disposition", "attachment; filename = " + filename)
msg.attach(part)


text = msg.as_string()

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(email_user,"novalinkmx")

server.sendmail(email_user, email_send, text)
server.quit()
