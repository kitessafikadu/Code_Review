import re

def is_valid_email(email):
    """Checks if an email is valid using regular expression."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email)) 

def main():
    """Handles user input and prints validation results."""
    email = input("Enter an email address: ").strip()  # Strip leading/trailing spaces
    if is_valid_email(email):
        print(f"✅ {email} is a valid email address.")
    else:
        print(f"❌ {email} is not a valid email address.")

if __name__ == "__main__":
    main()
