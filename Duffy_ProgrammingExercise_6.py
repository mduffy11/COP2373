def validate_ssn(ssn):
    # Validate standard SSN with or without hyphen
    pattern = r"(\d{3}-\d{2}-\d{4})|(\d{9})"

    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False

def validate_zip(zip_code):

    # Validate 5 or 9 digit zip code pattern
    pattern = r"\d{5}(-\d{4})?"

    if re.fullmatch(pattern, zip_code):
        return True
    else:
        return False

def main():
    print("Welcome To The Personal Information Validator!")
    print("Please enter your information to be validated.\n")

    # Get user input and strip leading/trailing whitespace
    phone_input = input("Enter your phone number: ").strip()
    ssn_input = input("Enter your Social Security Number: ").strip()
    zip_input = input("Enter your ZIP code: ").strip()

    # Call validation functions
    phone_checked = validate_phone(phone_input)
    ssn_checked = validate_ssn(ssn_input)
    zip_valid = validate_zip(zip_input)

    # Print the results of the validation functions
    print("\n Validation Results:")

    if phone_checked:
        print("The phone number you entered is valid.")
    else:
        print("The phone number you entered is invalid.")

    if ssn_checked:
        print("The social security number you entered is valid.")
    else:
        print("The social security number you entered is invalid.")

    if zip_valid:
        print("The ZIP code you entered is valid.")
    else:
        print("The ZIP code you entered is invalid.")

# Call main() to execute the program
if __name__ == "__main__":
    main()