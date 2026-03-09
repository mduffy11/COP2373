import re


def validate_phone(phone_number):
    """
    Validates a phone number against the accepted standard formats.

    Parameters:
        phone_number (str): The phone number entered by the user.

    Variables:
        pattern (str): The regular expression pattern used to match valid phone formats.

    Logic:
        1. Store a regular expression pattern for all accepted phone formats.
        2. Use re.fullmatch() to require the entire string to match the pattern.
        3. Return True when the phone number matches an accepted format.
        4. Return False when the phone number does not match an accepted format.

    Return:
        bool: True if the phone number is valid, or False otherwise.
    """
    # Match these one of these phone formats: (xxx) xxx-xxxx, xxx-xxx-xxxx,
    #								xxx.xxx.xxxx, xxx xxx xxxx, or xxxxxxxxxx.
    pattern = r"""
        \(\d{3}\) \d{3}-\d{4} |   # (xxx) xxx-xxxx
        \d{3}-\d{3}-\d{4}      |   # xxx-xxx-xxxx
        \d{3}\.\d{3}\.\d{4}    |   # xxx.xxx.xxxx
        \d{3} \d{3} \d{4}      |   # xxx xxx xxxx
        \d{10}                      # xxxxxxxxxx
    """

    # Return True only when the full phone number matches the pattern.
    if re.fullmatch(pattern, phone_number, re.VERBOSE):
        return True
    else:
        return False



def validate_ssn(ssn):
    """
    Validates a social security number against the accepted standard formats.

    Parameters:
        ssn (str): The social security number entered by the user.

    Variables:
        pattern (str): The regular expression pattern used to match valid SSN formats.

    Logic:
        1. Store a regular expression pattern for the accepted SSN formats.
        2. Use re.fullmatch() to require the entire string to match the pattern.
        3. Return True when the social security number matches an accepted format.
        4. Return False when the social security number does not match an accepted format.

    Return:
        bool: True if the social security number is valid, or False otherwise.
    """
    # Match the social security number against the accepted formats.
    pattern = r"(\d{3}-\d{2}-\d{4})|(\d{9})"

    # Return True only when the full social security number matches the pattern.
    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False



def validate_zip(zip_code):
    """
    Validates a ZIP code against the accepted standard formats.

    Parameters:
        zip_code (str): The ZIP code entered by the user.

    Variables:
        pattern (str): The regular expression pattern used to match valid ZIP code formats.

    Logic:
        1. Store a regular expression pattern for the accepted ZIP code formats.
        2. Use re.fullmatch() to require the entire string to match the pattern.
        3. Return True when the ZIP code matches an accepted format.
        4. Return False when the ZIP code does not match an accepted format.

    Return:
        bool: True if the ZIP code is valid, or False otherwise.
    """
    # Match the ZIP code against the accepted formats.
    pattern = r"\d{5}(-\d{4})?"

    # Return True only when the full ZIP code matches the pattern.
    if re.fullmatch(pattern, zip_code):
        return True
    else:
        return False



def main():
    """
    Runs the personal information validator by collecting input and printing validation results.

    Parameters:
        None

    Variables:
        phone_input (str): The phone number entered by the user after stripping outside whitespace.
        ssn_input (str): The social security number entered by the user after stripping outside whitespace.
        zip_input (str): The ZIP code entered by the user after stripping outside whitespace.
        phone_checked (bool): The validation result returned by validate_phone().
        ssn_checked (bool): The validation result returned by validate_ssn().
        zip_checked (bool): The validation result returned by validate_zip().

    Logic:
        1. Print a welcome message and brief program instructions.
        2. Prompt the user for a phone number, social security number, and ZIP code.
        3. Strip leading and trailing whitespace from each input.
        4. Call the matching validation function for each input value.
        5. Print whether each input is valid or invalid.

    Return:
        None
    """
    # Print the program title and instructions.
    print("Welcome To The Personal Information Validator!")
    print("Please enter your information to be validated.\n")

    # Read each value and remove leading and trailing whitespace.
    phone_input = input("Enter your phone number: ").strip()
    ssn_input = input("Enter your Social Security Number: ").strip()
    zip_input = input("Enter your ZIP code: ").strip()

    # Store the results returned by each validation function.
    phone_checked = validate_phone(phone_input)
    ssn_checked = validate_ssn(ssn_input)
    zip_checked = validate_zip(zip_input)

    # Print the validation results heading.
    print("\nValidation Results:")

    # Print whether the phone number is valid or invalid.
    if phone_checked:
        print("The phone number you entered is valid.")
    else:
        print("The phone number you entered is invalid.")

    # Print whether the social security number is valid or invalid.
    if ssn_checked:
        print("The social security number you entered is valid.")
    else:
        print("The social security number you entered is invalid.")

    # Print whether the ZIP code is valid or invalid.
    if zip_checked:
        print("The ZIP code you entered is valid.")
    else:
        print("The ZIP code you entered is invalid.")


# Call main() only when the file runs directly.
if __name__ == "__main__":
    main()

