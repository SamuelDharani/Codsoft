import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the requiredlength of the password: "))
        if length <= 0:
            raise ValueError("Only Positive Numbers Are Accepted")
        
        password = generate_password(length)
        print("Generated Password:", password)
    
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

