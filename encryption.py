from cryptography.fernet import Fernet
from rich.text import Text
from rich.console import Console
from rich import print
from rich.panel import Panel

console = Console()
text = Text("CRYPT", justify = 'center')
text.stylize("bold red")
console.print(text)

while True:
    choixPrint = Text("1.Crypter un fichier    |    2.Decrypter un fichier    |   3.Quitter le programme", justify = 'center')
    choixPrint.stylize("bold white")
    choix = input(console.print(choixPrint)).lower()

    if choix == "1":
        nomFichier = input("Quelle est le nom de votre fichier")
        def makeKey():
            key = Fernet.generate_key()
            with open("key.key", "wb") as keyFile:
                keyFile.write(key)

        def readKey():
            return open("key.key", "rb").read()

        makeKey()
        key = readKey()

        f = Fernet(key)

        with open(nomFichier, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(nomFichier, 'wb') as encrypted_files:
            encrypted_files.write(encrypted)

    if choix == "2":
        nomFichier = input("Quelle est le nom de votre fichier")
        def readKey():
            return open("key.key", "rb").read()
        key = readKey()
        f = Fernet(key)

        with open(nomFichier, 'rb') as encrypted_files:
            encrypted = encrypted_files.read()

        decrypted = f.decrypt(encrypted)

        with open(nomFichier, 'wb') as dec_file:
            dec_file.write(decrypted)

    if choix == "3":
        quit()
