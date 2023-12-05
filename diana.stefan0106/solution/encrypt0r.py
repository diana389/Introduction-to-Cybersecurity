#!/usr/bin/env python3

import base64
import json
import gmpy2


def str_to_number(text):
    """ Encodes a text to a long number representation (big endian). """
    return int.from_bytes(text.encode("ASCII"), 'big')

def number_to_str(num):
    """ Decodes a text to a long number representation (big endian). """
    num = int(num)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode('ASCII')

def encrypt(pub_k, msg_num):
    """ We only managed to steal this function... """
    cipher_num = gmpy2.powmod(msg_num, pub_k["e"], pub_k["n"])
    # note: gmpy's to_binary uses a custom format (little endian + special GMPY header)!
    cipher_b64 = base64.b64encode(gmpy2.to_binary(cipher_num))
    return cipher_b64

def decrypt(priv_k, cipher):
    """ We don't have the privary key, anyway :( """
    # you'll never get it!
    pass

if __name__ == "__main__":
    # example public key
    pub_k = {"e": 17, "n": 1221540932698357538969048008476734604937734436157953593060163}
    # generate a message
    message = "Test Message 1234"
    # note: encrypt requires a number
    msg_num = str_to_number(message)
    # test the reverse
    print("Message:", number_to_str(msg_num))
    # encrypt the message
    cipher = encrypt(pub_k, msg_num)
    print("Ciphertext:", cipher)
    # encode the message to the server's format
    # todo...

    file_path = "message.txt"

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        file_content = file.read()

    # Print or use the content as needed
    print("file_content:", file_content)

    file_content = base64.b64decode(file_content)

    print("file_content:", file_content)

    data_dict = json.loads(file_content)

    # Extract values
    n_value = data_dict["n"]
    e_value = data_dict["e"]
    flag_value = data_dict["flag"]

    print("n:", n_value)
    print("e:", e_value)
    print("flag:", flag_value)

    # string = "SpeishFlag{diana}"
    # string = encrypt(data_dict, str_to_number(string))
                     
    # print("string:", string)

    # regular_string = string.decode('utf-8')
    # print("regular_string:", regular_string)

    data = {"flag": flag_value}
    data = json.dumps(data)
    data = base64.b64encode(data.encode("ASCII"))

    print("data:", data)

    C = gmpy2.from_binary(base64.b64decode(flag_value))
    print("C:", C)

    Ca = gmpy2.powmod(5, e_value, n_value)
    print("Ca:", Ca)

    Cb = C * Ca
    Cb = base64.b64encode(gmpy2.to_binary(Cb))
    print("Cb:", Cb)

    regular_Cb = Cb.decode('utf-8') 
    
    data = {"flag": regular_Cb}
    data = json.dumps(data)
    data = base64.b64encode(data.encode("ASCII"))

    print("data:", data)

    string_returned_by_server = b'\x01\xa11\xfb\x0fA\t`\x1d\xe7\x05iK\x1d\xa5\x19\xeb\xbe\x9c\x14\x04\x0b7\n;\x0f\xaa\xa5j!\xf2\x1d\xe6\x1a\'[\r\xf2Y\x00\xef\xfc"\x97q'

    string_returned_by_server = int.from_bytes(string_returned_by_server, 'big')
    print("string_returned_by_server:", string_returned_by_server)

    string_returned_by_server = string_returned_by_server // 5

    print("string_returned_by_server:", string_returned_by_server)

    string_returned_by_server = number_to_str(string_returned_by_server)
    
    print("string_returned_by_server:", string_returned_by_server)