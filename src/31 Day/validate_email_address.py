''''
    Day 31
    Create a program that checks if a given string is a valid email address.

    "Email addresses must consist of 4 components: 
    - the regional address:
            From Wikipedia:
            - uppercase and lowercase Latin letters A to Z and a to z
            - digits 0 to 9
            - printable characters !#$%&'*+-/=?^_`{|}~
                (but usually only _%+- allowed by mail servers/clients)
            - dot ., provided that it is not the first or last character
            and provided also that it does not appear consecutively 
            (e.g., John..Doe@example.com is not allowed).
    - @, 
    - the domain name, 
    - and the domain name identifier."

    Output:
    Check email format using regular expression r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    example@example.com - valid
    example%@example.com - valid
    very.common@example.com - valid
    x@example.com - valid
    long.email-address-with-hyphens@and.subdomains.example.com - valid
    user.name+tag+sorting@example.com - valid
    name/surname@example.com - invalid
    admin@example - invalid
    example@s.example - valid
    " "@example.org - invalid
    "john..doe"@example.org - invalid
    mailhost!username@example.org - invalid
    invalid_email.com - invalid
    abc.example.com - invalid
    a@b@c@example.com - invalid
    just"not"right@example.com - invalid

    Check email format using email_validator library.

    example@example.com - valid
    example%@example.com - valid
    very.common@example.com - valid
    x@example.com - valid
    long.email-address-with-hyphens@and.subdomains.example.com - valid
    user.name+tag+sorting@example.com - valid
    name/surname@example.com - valid
    admin@example - invalid
    example@s.example - valid
    " "@example.org - invalid
    "john..doe"@example.org - invalid
    mailhost!username@example.org - valid
    invalid_email.com - invalid
    abc.example.com - invalid
    a@b@c@example.com - invalid
    just"not"right@example.com - invalid
'''
import re
from email_validator import validate_email, EmailNotValidError


def validate_email_address_regex(email_addresses):
    ''' Validate email address using regular expression '''
    # This regex allows _%+- characters
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    for email_address in email_addresses:
        # Check if the email matches the regular expression
        if re.match(email_regex, email_address):
            print(f"{email_address} - valid")
        else:
            print(f"{email_address} - invalid")


def validate_email_address_validator_lib(email_addresses):
    ''' Validate email address using email_validator library '''
    for email_address in email_addresses:
        try:
            # Validate the email address
            emailinfo  = validate_email(email_address, check_deliverability=False)
            print(f"{email_address} - valid")
        except EmailNotValidError:
            print(f"{email_address} - invalid")


if __name__ == "__main__":
    # Test the function with the examples from Wikipedia
    test_emails = ["example@example.com",
               "example%@example.com",
              "very.common@example.com",
              "x@example.com",
              "long.email-address-with-hyphens@and.subdomains.example.com",
              "user.name+tag+sorting@example.com",
              "name/surname@example.com",
              "admin@example",
              "example@s.example",
              "\" \"@example.org",
              "\"john..doe\"@example.org",
              "mailhost!username@example.org",
              "invalid_email.com",
              "abc.example.com",
              "a@b@c@example.com",
              "just\"not\"right@example.com"
    ]

    print("\nCheck email format using regular expression "\
          "r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'\n")
    validate_email_address_regex(test_emails)

    print("\nCheck email format using email_validator library.\n")
    validate_email_address_validator_lib(test_emails)
