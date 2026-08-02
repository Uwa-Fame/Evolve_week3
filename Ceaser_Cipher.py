def  shift_letter(letter, shift):
    """
    A function that Shift a lowercase letter forward by a given number of positions.

    Args:
        letter (str): A single lowercase letter.
        shift (int): Number of positions to shift.

    Returns:
        str: The shifted letter.
    """
      
    first_letter = "a" # this is a constant
    _first_chr_value = ord("a")  # converting the first letter/character of an ALPHABET to its ordinary value to determine its position.

    letter_position = ord(letter) - _first_chr_value # To determine a letter position by subtratct the first character value from the "entered/provided character value.
    new_position = (letter_position + shift) % 26
    return chr(_first_chr_value + new_position)
    
    # QWESTION QUESTION QUESTION: ALTERNATIVE ONE LINE CODE BELOW 
    # new_position = (ord(letter) - ord("a") + shift ) % 25 + ord('a')
    # return chr(new_position)

# TESTING shift_letter() fUNCTION 
# print(shift_letter('z', 4))



def encode(text, shift):
    
    """
Encode text using a Caesar cipher.

Args:
    text (str): Text to encode.
    shift (int): Number of positions to shift.

Returns:
    str: Encoded text.
"""
    encoded_texts = ""

    for character in text:
        if character.islower():
            encoded_texts += shift_letter(character, shift) # checks current letter position, add the requested number of shifts and returns the corresponding letter of the new possition.
        else:
            encoded_texts += character
    return encoded_texts
        
# TESTING the shift_letter() function and the "encode()" function    
# print(shift_letter("m", 6))
# data = print(encode("message me now", 6))



def decode(encoded_text, shift):
    """returns and encoded text"""
    return encode(encoded_text, -shift )

# TESTING the decode() function 
message1 = "i finally did it"


encrypted = encode(message1, 5) #calling the function to encrypt a message 
decrypted = decode(encrypted, 5) # I innitialy made a mistake of "decode(message,5) INSTEAD OF decode(encrypted, 5)

print("--------------------TEST 1-----------------")
print (encrypted)
print(decrypted)

print("--------------------TEST 2-----------------")
message_2 = "This is an encrypted message by Ebuwa Famous"
encrypted2 = encode(message_2, 8)
decrypted2 = decode(encrypted2, 3)
print("Encrpyted:", encrypted2)
print("Decrypted:", decrypted2)