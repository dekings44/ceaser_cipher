

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, Type decode to decrypt\n")

text = input('Type your message:\n').lower()

shift = int(input("Type the number of place your want to shift your text:\n"))


def encrypt(word, shift_number):
    cipher_text = ''
    for letter in word:
        position = letters.index(letter)
        new_position = position + shift_number
        new_letter = letters[new_position]
        cipher_text += new_letter
        
    print(f"The encode text is {cipher_text}")

encrypt(word=text, shift_number=shift)