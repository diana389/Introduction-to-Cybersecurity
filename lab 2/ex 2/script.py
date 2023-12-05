import gmpy2
from gmpy2 import mpz

c = mpz(28822365203577929536184039125870638440692316100772583657817939349051546473185)
n = mpz(70736025239265239976315088690174594021646654881626421461009089480870633400973)
e = 3

# FactorDB 
p = mpz(238324208831434331628131715304428889871)  
q = mpz(296805874594538235115008173244022912163)   

phi = (p - 1) * (q - 1)

# Calculate d using the modular inverse of e and phi
d = gmpy2.invert(e, phi)

# Decrypt the ciphertext
plaintext = gmpy2.powmod(c, d, n)

# Convert the result to ASCII text
decrypted_message = bytearray.fromhex(hex(plaintext)[2:]).decode("utf-8")

print("Decrypted Message:", decrypted_message)
