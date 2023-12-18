alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    end_text = ""
    if direction == 'decode':
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        # print(f"Alphabet length: {len(alphabet)}\n")
        # print(f"New position: {new_position}\n")

        if new_position >= len(alphabet):
            new_position = new_position - len(alphabet)
        end_text += alphabet[new_position]

    end_text = f"The {direction}d text is {end_text}"
    print(end_text)

caesar(text=text, shift=shift, direction=direction)
