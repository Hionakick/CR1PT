from cryptography.fernet import Fernet
from pyfiglet import Figlet

f = Figlet(font="puffy")
print (f.renderText("CR1PT"))

while True:
    choix = input("1.Crypter un fichier    |       2.Decrypter un fichier").lower()

    if choix == "1":
        def makeKey():
            key = Fernet.generate_key()
            with open("key.key", "wb") as keyFile:
                keyFile.write(key)

        def readKey():
            return open("key.key", "rb").read()

        makeKey()
        key = readKey()

        f = Fernet(key)

        with open('passwd', 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open('passwd', 'wb') as encrypted_files:
            encrypted_files.write(encrypted)

    if choix == "2":
        f = Fernet(key)

        with open('passwd', 'rb') as encrypted_files:
            encrypted = encrypted_files.read()

        decrypted = f.decrypt(encrypted)

        with open('passwd', 'wb') as dec_file:
            dec_file.write(decrypted)
