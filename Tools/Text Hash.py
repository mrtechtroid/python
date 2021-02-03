# Github: Mr Techtroid
# Allows People To Hash Strings Of Text In Almost All Hash Types Supported By HashLib. 
import hashlib
print("Enter the string you want to hash")
string = input("String:")
def hashalgorithm(string):
        
        hash1 = hashlib.md5(string.encode())
        print("Your MD5 Hashed string Is " + hash1.hexdigest())
        hash2 = hashlib.sha1(string.encode())
        print("Your SHA1 Hashed string Is " + hash2.hexdigest())
        hash3 = hashlib.sha224(string.encode())
        print("Your SHA224 Hashed string Is " + hash3.hexdigest())
        hash4 = hashlib.sha256(string.encode())
        print("Your SHA256 Hashed string Is " + hash4.hexdigest())
        hash5 = hashlib.sha384(string.encode())
        print("Your SHA284 Hashed string Is " + hash5.hexdigest())
        hash6 = hashlib.sha512(string.encode())
        print("Your SHA512 Hashed string Is " + hash6.hexdigest())
        hash7 = hashlib.blake2b(string.encode())
        print("Your BLAKE2b Hashed string Is " + hash7.hexdigest())
        hash8 = hashlib.blake2s(string.encode())
        print("Your BLAKE2s Hashed string Is " + hash8.hexdigest())
hashalgorithm(string)