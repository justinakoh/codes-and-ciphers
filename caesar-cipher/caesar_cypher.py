# This is a script to translate into and out of the caesar cypher.
# This is a simple subsitution cypher which involves substituting each letter
# in the message you want to be encoded, by substituting each letter by a
# specific number across

def main():
    start_message = input(
        "This is a caesar cipher encoder/decoder. Do you wish to continue? Y/n"
    )
    if start_message == "" or start_message == "y" or start_message == "Y":
        plaintext_letter = input("Please enter a letter you'd like to replace: ")
        encoded_letter = input(
            "Now please enter the letter you'd like to replace it with: "
        )
        number_of_shifts = calc_spaces_to_shift_by(
            plaintext_letter, encoded_letter
        )
        print("space", number_of_shifts)
        plaintext = input(
            "Please enter the text that you want to encode/decode: "
        )
        print("Past the plaintext input", plaintext)
        #Converting plaintext to all lowercase letters
        encoded_text = encode_text(plaintext.lower(), number_of_shifts)
        print(text)
    else:
        exit()


def encode_text(plaintext, number_of_shifts):
    print("First section")
    encoded_text = ""
    print("Encoded text", encoded_text)
    for letter in plaintext:
        print("Inside for loop", letter, "number of shifts ", number_of_shifts)
        encoded_text += output_letter(letter, number_of_shifts)
        print("After encoded", encoded_text)
    return encoded_text


# This calculates the spaces to shift the alphabet by
def calc_spaces_to_shift_by(plaintext_letter, encoded_letter):
    if plaintext_letter == " ":
        return 0
    elif ord(plaintext_letter) <= ord(encoded_letter):
        return abs(ord(plaintext_letter) - ord(encoded_letter))
    else:
        return (ord("z") - ord(plaintext_letter)) + (ord(encoded_letter) - ord("a") + 1)

# This will output the actual letter
def output_letter(original_letter, number_of_shifts):
    if original_letter == " ":
        return " "
    # elif plaintext_letter.isdigit():
    #     if  number_of_shifts + ord(original_letter) >
    else:
        return chr((ord(original_letter) + number_of_shifts) % 122)
    # number = ord(original_letter) + number_of_shifts
    # if number <= 122:
    #     return chr(number)
    # else:
    #     return chr(ord("a") + (number - ord("z") - 1))


if __name__ == "__main__":
    main()
