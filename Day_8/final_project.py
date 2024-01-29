from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(mode, message, shift):
    result = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            if mode == 'encode':
                result += alphabet[index+shift]
            elif mode == 'decode':
                result += alphabet[index-shift]
        else:
            result += letter
    return result


#menu
print(logo)
choice = "yes"
while choice == "yes":
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(f"Here's the encoded result: {cipher(mode, message, shift)}")
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")