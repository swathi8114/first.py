import random
import string 

# Function to generate password 
def generate_password(length, complexity):
    characters = string.ascii_lowercase

    if complexity >= 2:
        characters += string.ascii_uppercase
    if complexity >= 3:
        characters += string.digits
    if complexity == 4:
        characters += string.punctuation 

    # Generate password with the specified length and character set 
    password = ''.join(random.choice(characters) for _ in range(length))

    return password 

# Main function to take input from the user 
def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter Password length (minimum 6 characters): "))
            if length < 6:
                print("Password length must be at least 6.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for password length.")

    print("\nChoose password complexity level:")
    print("1 = Lowercase letters only")
    print("2 = Lowercase + Uppercase letters")
    print("3 = Lowercase + Uppercase letters + Digits")
    print("4 = Lowercase + Uppercase + Digits + Special characters ")

    while True:
        try:
            complexity = int(input("Enter complexity level (1-4): "))
            if complexity < 1 or complexity > 4:
                print("Please choose a complexity level between 1 and 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for complexity level.")

    # Generate and display the password 
    password = generate_password(length, complexity)
    print("\nGenerated password: ", password)

# Run the application 
if __name__ == "__main__":
    main()