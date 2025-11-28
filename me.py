import socket
import base64


# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                 # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    return decipher

def to_send(todecode, s):
    for c in todecode:
            if c == '.':
                todecode = todecode.replace("/"," ")
                val = decrypt(todecode)
                print (val)
                print("to send")
                s.send(f"{val.lower()}\n".encode())
                print("morse")
                return True
    return False


# Hard-coded driver function to run the program
message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
result = decrypt(message)
print (result)


HOST = "challenge01.root-me.org"  # The server's hostname or IP address
PORT = 52017      # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    
    i = 0
    while i < 100:
        data = s.recv(1024)
        print(data.decode())
        var = data.decode()
        index = var.find(":")
        todecode = var[index+3:-5:]

        print("presentation :" + todecode + ".")
        if to_send(todecode,s):
            i += 1
            continue
        try :
            val = bytes.fromhex(todecode).decode('utf-8')
            print("to send")
            s.send(f"{val}\n".encode())
            print("ASCII")
            i += 1
            continue
        except:
            print("next")
        try :
            val = base64.b64decode(todecode.encode())
            print(val.decode())
            print("to send")
            s.send(f"{val.decode()}\n".encode())
            print("b64")
            i += 1
            continue
            for c in val :
                if c.islower():
                    print("to send")
                    s.send(f"{val}\n".encode())
                    print("b64")    
                    i = i + 1
            if i != 0 :
                break
                    
        except :
            print("next")
        try :
            val = base64.b32decode(todecode[::].encode())
            print(val.decode())
            print("b32")
            print("to send")
            s.send(f"{val.decode()}\n".encode())
            i += 1
            continue
            
        except:
            print("next")
        try :
            val = base64.b85decode(todecode.encode())
            print(val.decode())
            print("b85")
            print("to send")
            s.send(f"{val.decode()}\n".encode())
            i += 1
            continue
        except:
            print("b85 next")
    data = s.recv(1024)
    print(data.decode())
   
# base64 ok
# morse
# base32 ok
# ascii = utf 8
# base64.b85decode base85 ok