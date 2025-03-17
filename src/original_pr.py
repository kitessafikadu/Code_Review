import re

def is_valid_email(email: str) -> bool:
    """
    Validates an email address using a stricter regular expression.
    
    - Ensures the email follows a proper structure.
    - Uses re.match() to enforce full-string validation.
    - Prevents multiple consecutive dots and trailing dots.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not email:
        return False  # Handle None or empty input

    pattern = r'^[a-zA-Z0-9]+([._+-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
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
