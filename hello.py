def encode(password):
    passNum = str(password)
    encoded = ""
    for c in passNum:
        extraVar = int(c)+3
        xxVar = str(extraVar)
        encoded += xxVar
    return encoded


def decode(encodedPassword):
    result = ""
    for i in encodedPassword:
        i = int(i)
        if i >= 3:
            i -= 3
            result += str(i)
        else:
            if i == 2:
                result += '9'
            elif i == 1:
                result += '8'
            elif i == 0:
                    result += '7'
        return result



def main():
    
    encoded = None
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\n")
        menu_selection= int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print(encoded)
        
        elif menu_selection == 2:
            decoded = decode(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".")
            
        elif menu_selection == 3 :
            break
        
if __name__ == "__main__":
    main()