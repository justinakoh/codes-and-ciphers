from string import ascii_uppercase as l

def main():
    start_message = input(
        "This is an encoder/decoder which uses the Affine Cipher. Do you wish to continue? "
    )
    if start_message == "" or start_message == "y" or start_message == "Y":
        plaintext = input("Please enter your plaintext: ").lower()
        a = input ("Please input a random number: ")
        if a.is_integer():
            b = input ("Please input a random number that is coprime to the first number: ")
                if b.is_integer():
                if checkIfPrime():
                    print("Is prime")
                    #Setting the variables
                    m = 26 #num of letters in the alphabet

                    #Do the equation
                    for i in plaintext:
                        encoded_letter = (ax + b) % m

                        print("Letter: ", i " encoded: ", encoded_letter)
                    else:
                        print("This number is not coprime")
        else:
            print("Please enter an integer value")

        print("Plaintext: ", plaintext, " a: ", a, " b: ", b)

def checkIfPrime():
    print("Checking")

if __name__ == "__main__":
    main()
