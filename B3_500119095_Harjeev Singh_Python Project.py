import base64

def encode_base64(input_str):
    """
    Encodes the given input string to base64 format.
    """
    encoded_bytes = base64.b64encode(input_str.encode())
    encoded_str = encoded_bytes.decode()
    return encoded_str

def decode_base64(input_str):
    """
    Decodes the given input string from base64 format.
    """
    try:
        decoded_bytes = base64.b64decode(input_str.encode())
        decoded_str = decoded_bytes.decode()
        return decoded_str
    except base64.binascii.Error as e:
        return f"An error occurred during decoding: {str(e)}"

def caesar_cipher(text, shift, mode='encode'):
    """
    Encodes or decodes the given text using Caesar cipher with the specified shift.
    """
    result = ""
    for char in text:
        if char.isalpha():
            if mode == 'encode':
                shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            else:  # mode == 'decode'
                shifted_char = chr(((ord(char.lower()) - 97 - shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

def main():
    """
    The main function that takes user input and performs encoding/decoding.
    """
    print("Encoder/Decoder")
    while True:
        print("\nOptions:")
        print("1. Encode/Decode with Base64")
        print("2. Encode/Decode with Caesar Cipher")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")
        
        if choice == '1':
            sub_choice = input("Choose 'encode' or 'decode': ")
            if sub_choice.lower() == 'encode':
                plain_text = input("Enter text to encode: ")
                print("Encoded Text:", encode_base64(plain_text))
            elif sub_choice.lower() == 'decode':
                encoded_text = input("Enter base64 text to decode: ")
                print("Decoded Text:", decode_base64(encoded_text))
            else:
                print("Invalid sub-option. Please choose 'encode' or 'decode'.")
        elif choice == '2':
            sub_choice = input("Choose 'encode' or 'decode': ")
            if sub_choice.lower() == 'encode':
                plain_text = input("Enter text to encode: ")
                shift = int(input("Enter the shift value (1-25): "))
                print("Encoded Text:", caesar_cipher(plain_text, shift))
            elif sub_choice.lower() == 'decode':
                encoded_text = input("Enter text to decode: ")
                shift = int(input("Enter the shift value (1-25): "))
                print("Decoded Text:", caesar_cipher(encoded_text, shift, mode='decode'))
            else:
                print("Invalid sub-option. Please choose 'encode' or 'decode'.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
