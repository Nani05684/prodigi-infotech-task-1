'''The caesar cipher algorithm is a traditional way to encrypt or decrypt data in cyrptography,

 it have a plaintext and a key/shift value to encrypt/decrypt the data'''

#main logic of the caeser cipher algorithm 
def caesar_cipher(text, key, direction):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + direction * key) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result


#Reading the inputs from the user wheather its a plain text or Cipherd text 
def main():
    text = input("Enter the text: ")
    key = int(input("Enter the key value: "))

#Reading the inpt from the user to encrypt or decrypt the data 
    mode = input("Choose mode - Encrypt (E) or Decrypt (D): ")

    if mode.lower() == 'e':
        print("Encrypted text: ", caesar_cipher(text, key, 1))
    elif mode.lower() == 'd':
        print("Decrypted text: ", caesar_cipher(text, key, -1))
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()
