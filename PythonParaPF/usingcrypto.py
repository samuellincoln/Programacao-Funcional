from crypto.Cipher import AES
from crypto.Random import get_random_bytes
from crypto.Util.Padding import pad
# Set up the encryption key and initialization vector
key = get_random_bytes(16)
iv = get_random_bytes(16)
# Create the AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)
# Encrypt the plaintext
plaintext = pad (b'This is a secret message.', 16)
#pad preenche o texto sem formatacao para o tamanho do bloco AES de 16 bytes
print ("Message :: " + str (plaintext))
#The b' indicates that it is a bytes object in Python
ciphertext = cipher.encrypt(plaintext)
# Print the ciphertext
print("Encrypted text :: " + ciphertext.hex())
# Create a new AES cipher object for decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
# Decrypt the ciphertext
decrypted_plaintext = decipher.decrypt(ciphertext)
# Print the decrypted plaintext
print("Decrypted text :: " + decrypted_plaintext.decode())
