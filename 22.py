import hashlib

# Input text
text = "Hello hashing"

# Encode to bytes and generate SHA256 hash
hash_value = hashlib.sha256(text.encode()).hexdigest()

print("Original Text:", text)
print("Hashed Value:", hash_value)
