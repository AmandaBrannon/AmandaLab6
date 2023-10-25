
def encode(password):
    passNum = str(password)
    encoded = ""
    for c in passNum:
        extraVar = int(c)+3
        xxVar = str(extraVar)
        encoded += xxVar
    return encoded




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