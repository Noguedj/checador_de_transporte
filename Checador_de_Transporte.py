#Probador de conexion
#!/usr/bin
import subprocess, time
hosts = ("8.8.8.8", "yahoo.com")
def ping(host):
    ret = subprocess.call(["ping", "-c", "3", "-w", "5", host],
        stdout = open("/dev/null", "w"),
        stderr = open("/dev/null", "w"))
    return ret == 0
print ("checando red")
xstatus = 1
if ping("8.8.8.8"):
    q = "true"
    xstatus = 0
if xstatus:
    q = "false" 
if q == "true":
#Fin de la prueba
#enviar correo
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
    body = "Lista de usuarios"
    msg.attach(MIMEText(body,"plain"))
    filename = "/home/pi/pitando/Lista_usuarios.csv"
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
#fin del envio
    while 1 == 1:    
        prueba = open("/home/pi/pitando/Lista_usuarios.csv","a")
        print("Introduce el numero de empleado\n")
        Num = str(input())
        import time
        hora = time.strftime("%H:%M:%S")
        fecha = time.strftime("%d/%m/%y")
        prueba.write(Num)
        prueba.write(",")
        prueba.write(hora)
        prueba.write(",")
        prueba.write(fecha)
        prueba.write("\n")
        prueba.close()
else:
     while 1 == 1:    
        prueba = open("/home/pi/pitando/Lista_usuarios.csv","a")
        print("Introduce el numero de empleado1\n")
        Num = str(input())
        import time
        hora = time.strftime("%H:%M:%S")
        fecha = time.strftime("%d/%m/%y")
        prueba.write(Num)
        prueba.write(",")
        prueba.write(hora)
        prueba.write(",")
        prueba.write(fecha)
        prueba.write("\n")
        prueba.close()
        
        
        
            
            
            
    
