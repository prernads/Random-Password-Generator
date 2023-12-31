import random
import string

def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Include at least one digit, one uppercase letter, and one lowercase letter
    password.append(random.choice(string.digits))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))

    # Include at least one special character
    password.append(random.choice(string.punctuation))

    # Fill the remaining characters randomly
    for i in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the password to remove predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Test the function
x = generate_password()
print(x)