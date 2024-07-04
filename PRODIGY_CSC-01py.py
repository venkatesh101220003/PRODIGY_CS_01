def caesar_cipher(text, shift, mode):
    if mode == "decrypt":
        shift = 26 - shift
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

if __name__ == "__main__":
    print("Caesar Cipher")
    while True:
        mode = input("\nChoose mode (encrypt/decrypt): ").lower()
        if mode in ["encrypt", "decrypt"]:
            break
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    output = caesar_cipher(message, shift, mode)

    if mode == "encrypt":
        print(f"Encrypted message: {output}")
    else:
        print(f"Decrypted message: {output}")