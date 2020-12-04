import smtplib

smtpObject = smtplib.SMTP('smtp.gmail.com', 587)
smtpObject.starttls()

from_some = str(input("Cuenta: "))
password = input("Password: ")
smtpObject.login(from_some,password)

to_some = str(input("Para: "))
subject = str(input("asunto: "))
body = str(input("Mensaje: "))


smtpObject.sendmail(from_some,to_some,body)
smtpObject.quit()

     