import bcrypt
import hashlib


def is_valid_password(password: str) -> bool:
    # Check for empty password

    if not password:
        print("Error: Password cannot be empty.")
        return false

    # Check for special characters only

    if re.fullmatch(r'[^a-zA-Z0-9]+', password):
        print("Error: Password must contain at least one alphanumeric character.")
        return false

    # Check for length constraint

    if len(password) > 256:
        print("Error: Password must be 256 characters or less.")

        return False

    # Check for non-ASCII characters

    if not all(ord(char) < 128 for char in password):
        print("Error: Password must only contain ASCII characters.")

        return False

    return True


def hash_password(password: str, filename: str):
    # Generate a random salt using bcrypt

    salt = bcrypt.gensalt()

    # Combine the salt with the password

    salted_password = password.encode() + salt

    # Hash the salted password using SHA-256 from hashlib

    sha256_hash = hashlib.sha256(salted_password).hexdigest()

    # Further hash the result with bcrypt

    bcrypt_hash = bcrypt.hashpw(sha256_hash.encode(), salt)

    # Write the final hashed password to a file

    with open(filename, 'w') as file:
        file.write(str(bcrypt_hash))

    print("-" * 40)  # line separator

    print(f"Hashed password saved to {filename}")


# Example usage
password = "YourSecurePassword123"
hash_password(password, 'hashed_password.txt')
