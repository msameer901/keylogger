import hashlib
import os

def hash_password(password: str) -> str:
    """
    Returns the SHA-256 hash of the given password as a hex string.
    """
    hash_object = hashlib.sha256(password.encode('utf-8'))
    return hash_object.hexdigest()

def store_password_hash(password: str, filename: str):
    """
    Hashes the password and writes the hash to a file.
    """
    hashed = hash_password(password)
    with open(filename, 'w') as f:
        f.write(hashed)
    print("✅ Password hash stored successfully.")

def verify_password(input_password: str, filename: str) -> bool:
    """
    Verifies if the hash of the input password matches the stored hash.
    """
    input_hash = hash_password(input_password)
    
    if not os.path.exists(filename):
        print("⚠️ Password file not found.")
        return False

    with open(filename, 'r') as f:
        stored_hash = f.read().strip()

    return input_hash == stored_hash

def view_stored_hash(filename: str):
    """
    Displays the stored hash from the file.
    """
    if not os.path.exists(filename):
        print("⚠️ No password hash stored yet.")
        return

    with open(filename, 'r') as f:
        stored_hash = f.read().strip()
    
    print(f"🔑 Stored password hash: {stored_hash}")

def menu():
    print("\n====== Password Hashing Menu ======")
    print("1. Hash a new password")
    print("2. Verify a password")
    print("3. View stored hashed password")
    print("4. Exit")

if __name__ == "__main__":
    filename = "password.txt"

    while True:
        menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            password = input("Set a new password: ")
            store_password_hash(password, filename)

        elif choice == "2":
            if not os.path.exists(filename):
                print("⚠️ No password hash stored. Please hash a password first.")
                continue

            while True:
                test_password = input("Enter password to verify: ")
                if verify_password(test_password, filename):
                    print("✅ Password is correct!")
                    break
                else:
                    print("❌ Incorrect password. Try again.")

        elif choice == "3":
            view_stored_hash(filename)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter 1, 2, 3, or 4.")
