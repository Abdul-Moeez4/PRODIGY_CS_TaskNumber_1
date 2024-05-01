def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text


def main():
    message = input("Enter a message: ")
    shift = int(input("Enter a shift value: "))

    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()