alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        # print(f"Alphabet length: {len(alphabet)}\n")
        # print(f"New position: {new_position}\n")

        if new_position >= len(alphabet):
            new_position = new_position - len(alphabet)
        encrypted += alphabet[new_position]

    print(f"The encoded text is {encrypted}")

def decrypt(text, shift):
    decrypted = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        # print(f"Alphabet length: {len(alphabet)}\n")
        # print(f"New position: {new_position}\n")

        decrypted += alphabet[new_position]

    print(f"The decoded text is: {decrypted}")

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)