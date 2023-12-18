from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    end_text = ""
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            # print(f"Alphabet length: {len(alphabet)}\n")
            # print(f"New position: {new_position}\n")

            if new_position >= len(alphabet):
                new_position = new_position - len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {direction}d text is {end_text}\n")

print(logo)


should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= len(alphabet) #alter case when shift is higher that alphabet length
    caesar(text=text, shift=shift, direction=direction)

    option = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    if option == 'no':
        should_continue = False
        print("Goodbye")