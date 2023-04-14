from Crypto.Cipher import AES

# Entrez le nom du fichier à chiffrer
file_name = input("Entrez le nom du fichier à chiffrer : ")
# Entrez la clé de chiffrement (16, 24 ou 32 caractères)
key = input("Entrez la clé de chiffrement (16, 24 ou 32 caractères) : ")

# Fonction pour chiffrer le fichier
def encrypt_file(file_name, key):
    # Ajouter des octets de remplissage pour que la taille du fichier soit un multiple de 16
    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    # Ouverture du fichier en mode binaire
    with open(file_name, "rb") as f:
        data = f.read()
    # Chiffrement des données
    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data))
    # Écriture des données chiffrées dans un nouveau fichier
    with open(file_name + ".enc", "wb") as f:
        f.write(encrypted_data)

# Appel de la fonction pour chiffrer le fichier
encrypt_file(file_name, key)
