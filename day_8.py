from ascii_art import caesar_logo

def user_interface():
    print(caesar_logo)
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction.lower() == "encode" or direction.lower() == 'decode':
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            caesar(original_text=text, shift_amount=shift, cipher_direction=direction)
        else:
            print("Invalid Input")

        end_program = input("Type 'Yes' if you want to go again, otherwise, type 'No'.")
        if end_program.lower() == 'yes':
            continue
        elif end_program.lower() == 'no':
            print("Ending Program...")
            break
        else:
            print("Invalid Input!")
            print("Ending Program...")
            break


def caesar(original_text: str, shift_amount: int, cipher_direction: str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    result = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in original_text:
        if char in alphabet:
            shift_index = alphabet.index(char) + shift_amount
            if abs(shift_index) >= len(alphabet):
                shift_index = shift_index % len(alphabet)
            result += alphabet[shift_index]
        else:
            result += char

    print(f"The {cipher_direction}d text is: {result}")

user_interface()