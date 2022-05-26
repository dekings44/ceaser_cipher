

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, Type decode to decrypt\n")

text = input('Type your message:\n').lower()

shift = int(input("Type the number of place your want to shift your text:\n"))


# def encrypt(word, shift_number):
#     cipher_text = ''
#     for letter in word:
#         position = letters.index(letter)
#         new_position = position + shift_number
#         new_letter = letters[new_position]
#         cipher_text += new_letter
        
#     print(f"The encode text is {cipher_text}")



# def decrypt(cipher_text, shift_number):
#     plain_text = ""
#     for letter in cipher_text:
#         position = letters.index(letter)
#         new_position = position - shift_number
#         plain_text += letters[new_position]

#     print(f"The decoded text is {plain_text}")



# if direction == "encode":
#     encrypt(word=text, shift_number=shift)
# elif direction == "decode":
#     decrypt(cipher_text = text, shift_number = shift)


def caeser(start_text, shift_number, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
            shift_number *= -1
    for letter in start_text:
        position = letters.index(letter)
        new_position = position + shift_number
        end_text += letters[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

caeser(start_text = text, shift_number = shift, cipher_direction = direction)
