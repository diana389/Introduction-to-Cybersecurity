from Crypto.Cipher import AES
import os

BLOCK_SIZE = 32
PADDING = b'#'
iv = b"\x00" * 16

def unpad(s):
    return s.rstrip(PADDING)

def decrypt(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = aes.decrypt(data)
    return unpad(decrypted_data)

with open('isc-lab02-secret.enc', 'rb') as f:
    key = f.read(BLOCK_SIZE)  # Use your actual key here
    enc = f.read()

dec = decrypt(key, iv, enc)

with open('decrypted.jpg', 'wb') as f_out:
    f_out.write(dec)
