import random
import string

def generate_complex_password(min_length=16, max_length=32, use_special_chars=True, use_uppercase=True):
    if min_length > max_length:
        raise ValueError("Minimum length cannot be greater than maximum length.")

    password_length = random.randint(min_length, max_length)

    # Define the character sets to choose from
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Combine the character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure that the password contains at least one character from each set
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters) if use_uppercase else ''
    password += random.choice(digits)
    password += random.choice(special_chars) if use_special_chars else ''

    # Fill the rest of the password with random characters
    for _ in range(password_length - len(password)):
        password += random.choice(all_chars)

    # Shuffle the password to make it more secure
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Example usage
password = generate_complex_password()
print(password)
