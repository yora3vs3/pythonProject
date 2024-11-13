import getpass  # For masked input, such as password
import re  # For regular expressions in input validation


def get_integer_input(prompt):
    """Function to get integer input with validation."""
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input! Please enter an integer.")


def get_float_input(prompt):
    """Function to get float input with validation."""
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a decimal number.")


def get_choice_input(prompt, choices):
    """Function to get input that must be one of the specified choices."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in choices:
            return user_input
        print(f"Invalid choice! Choose one of: {', '.join(choices)}.")


def get_email_input(prompt):
    """Function to validate an email address input using regex."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input(prompt).strip()
        if re.match(email_regex, email):
            return email
        print("Invalid email format. Please try again.")


def collect_user_information():
    """Collect and display comprehensive user information."""

    # Basic inputs with type conversions
    print("\nPlease enter your basic information.")
    name = input("Enter your full name: ").strip()
    age = get_integer_input("Enter your age: ")
    height = get_float_input("Enter your height (in meters): ")

    # Multiple choice input
    gender = get_choice_input("Enter your gender (male/female/other): ", ["male", "female", "other"])

    # Masked input for sensitive data
    password = getpass.getpass("Enter a secure password: ")

    # Email with validation
    email = get_email_input("Enter your email address: ")

    # Handling multiple inputs at once
    favorite_numbers = input("Enter your three favorite numbers, separated by spaces: ").split()
    favorite_numbers = [int(num) for num in favorite_numbers if num.isdigit()]

    # Addressing empty input and default values
    city = input("Enter your city (leave blank if not applicable): ").strip() or "Not provided"
    country = input("Enter your country (leave blank if not applicable): ").strip() or "Not provided"

    # Confirming input data
    print("\nThank you! Please review your details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height:.2f} meters")
    print(f"Gender: {gender.capitalize()}")
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)} (hidden for security)")
    print(f"Favorite Numbers: {', '.join(map(str, favorite_numbers))}")
    print(f"Location: {city}, {country}")

    confirm = get_choice_input("Is all information correct? (yes/no): ", ["yes", "no"])
    if confirm == "no":
        print("Let's re-enter your information.\n")
        collect_user_information()
    else:
        print("Information confirmed. Thank you!")


# Comprehensive user input example with handling edge cases
if __name__ == "__main__":
    collect_user_information()
