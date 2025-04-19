import random
import string

def generate_password(length):
    """Generate a secure password of given length."""
    if length < 4:
        return "⚠️ Password length should be at least 4 characters."

    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    # Ensure password contains at least one character from each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)  # Shuffle to randomize character positions

    return ''.join(password)

def main():
    print("\n🔐 Secure Password Generator 🔐")

    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("⚠️ Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
