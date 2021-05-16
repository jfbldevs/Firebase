import pyrebase

firebaseConfig = {
    'apiKey': "",
    'authDomain': "",
    'projectId': "",
    'storageBucket': "",
    'messagingSenderId': "",
    'appId': "",
    'measurementId': "",
    'databaseURL':""
  }

firebase = pyrebase.initialize_app(firebaseConfig)

#Autenticación
#Login y contraseña
auth = firebase.auth()

"""email = input("Entra tu email: ")
password = input("Entra tu password: ")

try:
    auth.sign_in_with_email_and_password(email, password)
    print("Bienvenido!")
except:
    print("Correo ó contraseña incorrectos")"""

#Creación de cuentas de usuarios
"""email = input("Entra tu email: ")
password = input("Entra tu password: ")
confirmpass = input("Confirma tu password: ")

if password == confirmpass:
    try:
        auth.create_user_with_email_and_password(email, password)
    except:
        print("El email ya existe")"""
#Verificación de correo
"""email = input("Entra tu email: ")
password = input("Entra tu password: ")
login = auth.sign_in_with_email_and_password(email, password)
auth.send_email_verification(login['idToken'])
print("Verificación en camino")"""
#Recuperación de contraseña
"""email = input("Entra tu email: ")
auth.send_password_reset_email(email)
print("Verificación en camino")"""