from string import ascii_uppercase as l


def main():
    start_message = input(
        "This is an encoder/decoder which uses the Vigenere Cipher. Do you wish to continue? "
    )
    if start_message == "" or start_message == "y" or start_message == "Y":
        # Make the table
        table = createTable()
        plaintext = input("Please enter your plaintext here ")
        keyword = input("Please enter your chosen keyword ")
        keyword_letter = 0
        final_string = ""
        # Loop through plaintext
        for i in plaintext:
            # Allows us to loop through keyword
            if keyword_letter >= len(keyword):
                keyword_letter = 0

            # Checks that plaintext char is a letter
            if i.isalpha():
                final_string += table[ord(i) - 97][ord(keyword[keyword_letter]) - 97]

            elif i.isnumeric():
                final_string += i

            elif i == " ":
                keyword_letter -= 1  # decrement so when we increment later it doesn't skip parts of the keyword

            # Increment to make sure we loop through keyword
            keyword_letter += 1


# Creates the 2D table used by the Vigenere cipher
def createTable():
    table = [l[i:] + l[:i] for i in range(len(l))]
    return table


if __name__ == "__main__":
    main()
