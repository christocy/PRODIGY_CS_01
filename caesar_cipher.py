def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Encryption/Decryption")
    mode_choice = input("Choose 'encrypt(e)' or 'decrypt(d)': ").lower()

    if mode_choice == 'e':
        mode = 'encrypt'
    elif mode_choice == 'd':
        mode = 'decrypt'
    else:
        print("Invalid choice!")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (positive integer): "))
    shift = shift % 26  # Ensures the shift value wraps around

    result = caesar_cipher(message, shift, mode)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
