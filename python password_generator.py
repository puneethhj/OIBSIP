import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on the given criteria."""
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character set (letters, numbers, symbols) must be selected.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    print("Welcome to the Password Generator")

    try:
        length = int(input("Please enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as ve:
        print(ve)
        return

    use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
