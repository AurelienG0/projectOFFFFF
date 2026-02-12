import pyAesCrypt
import os

#inr

password = "hgTsCsIajPpMeNNUUmorVrrll"

action = input("ecris e pour encrypt ou d pour decrypt:   \n")


if action == "e":
    files_files_first = os.listdir("files_first")
    print("Voici tous les fichiers disponibles")
    for f in enumerate(files_files_first, start=1):
        print(f"{f}")
    choice = int(input("choisis un fichier :  \n"))
    filechoose_encrypted = files_files_first[choice - 1]
    pyAesCrypt.encryptFile(f"files_first/{filechoose_encrypted}",f"encrypted_files/{filechoose_encrypted}.aes", password)

elif action == "d":
    files_encrypted_files = os.listdir("encrypted_files")
    print("Voici tous les fichiers disponibles")
    for f in enumerate(files_encrypted_files, start=1):
        print(f"{f}")
    choice = int(input("choisis un fichier :  \n"))
    filechoose_decrypted = files_encrypted_files[choice - 1]
    pyAesCrypt.encryptFile(f"encrypted_files/{filechoose_decrypted}",f"decrypted_files/{filechoose_decrypted.replace('.aes', '')}", password)

