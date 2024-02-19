ciphertext = "wAyk{mmAwjAuwpzAwmAqjn"

for key in range(256):
    decrypted_text = ''.join([chr(ord(c) ^ key) for c in ciphertext])
    print(f"Key {key}: {decrypted_text}")