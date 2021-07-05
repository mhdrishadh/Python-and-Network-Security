# Method 1

#1. Write a program in Python to generate MD5 of string data


import hashlib

hash_object = hashlib.md5(b'Rishadh')
hex_dig = hash_object.hexdigest()
print(hex_dig)


#2.Write a program in Python to generate hashes of string data using 3 algorithm from hashlib

import hashlib

# Using SHA224 algorithm

hash_object = hashlib.sha224(b'Rishadh')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# Using SHA256 algorithm

hash_object = hashlib.sha256(b'Rishadh')
hex_dig = hash_object.hexdigest()
print(hex_dig)

# Using SHA512 algorithm

hash_object = hashlib.sha512(b'Rishadh')
hex_dig = hash_object.hexdigest()
print(hex_dig)


# Method 2
# If we take input from user(string as input)

x = input()

import hashlib

hash_object = hashlib.md5(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)


# Using SHA224 algorithm

hash_object = hashlib.sha224(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

# Using SHA256 algorithm

hash_object = hashlib.sha256(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)

# Using SHA512 algorithm

hash_object = hashlib.sha512(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)