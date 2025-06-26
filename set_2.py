alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def shift_letter(letter, shift):
    alphabet_var = alphabet.find(letter)

    shift_process = shift + alphabet_var - 26*int((shift+alphabet_var)/26)

    if letter.isalpha() == False:
        final = " "
    else:
        final = alphabet[shift_process]
    return final

def caesar_cipher(message, shift):
    shiftee = ""
    for i in range(len(message)):
        letter = message[i]
        shiftee += shift_letter(letter, shift)
    return shiftee

def shift_by_letter(letter, letter_shift):
    shifted_letter =alphabet.find(letter_shift)
    return(shift_letter(letter, shifted_letter))

def vigenere_cipher(message, key):
    shift_message = ""
    for i in range(len(message)):
        letter_var = message[i]
        key_letter = key[i % len(key)]
        shifted_letter = shift_by_letter(letter_var, key_letter)
        shift_message += shifted_letter
    return shift_message


def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    characters = len(message) // shift
    cipher_text = ""
    for i in range(characters):
        for x in range(shift):
            cipher_text += message[x * characters + i]
    return cipher_text


def scytale_decipher(message, shift):
    message2 = ""
    for i in range(0, len(message)):
        end = shift*i
        if end >= len(message):
            end = end % len(message) + int(end/len(message))
        message2 = message2 + message[end]
    return message2