import pyrebase

firebaseConfig = {
    'apiKey': "",
    'authDomain': "",
    'projectId': "",
    'storageBucket': "",
    'messagingSenderId': "",
    'appId': "",
    'measurementId': "",
    'databaseURL': ''
  }


firebase = pyrebase.initialize_app(firebaseConfig)

#Storage
#Establecer reglas:
""""rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if true;
    }
  }
}"""

#Uploading
storage = firebase.storage()
#Nombre de la carpeta a subir
#filename = input("Enter the name of the file you want to upload: ")
#Nombre que quieres que tenga la carpeta en la nube
#cloudfilename = input("Enter the name of the file on the cloud: ")
#Sube el archivo del directorio hacia la nube
"""storage.child(cloudfilename).put(filename)
#Nota: a)contendor/archivo/file_01.txt, crea las carpetas y luego copia el archivo indicado
#Nota: b) Si ponemos sólo el nombre del archivo, los copiaremos en la raíz principal "contenidocopiado02.txt"
print(storage.child(cloudfilename).get_url(None)) #Genera una url en la consola de acceso a los datos en la nube"""
#Downloading data
"""cloudfilename = input("Enter the name of the file you want to download: ")
storage.child(cloudfilename).download("", "archivo.txt") #Si está en el root se pone nombre y extención, de lo contrario indicar la ruta del archivo
storage.child("file_01.txt").download("", "donwloaded.txt") #Otra alternativa de descarga"""
