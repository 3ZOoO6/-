from cryptography.fernet import Fernet
import base64

class AdvancedCrypto:
    def __init__(self, secret_key):
        self.key = base64.urlsafe_b64encode(secret_key.ljust(32)[:32].encode())
        self.cipher = Fernet(self.key)
    
    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data.encode()).decode()
