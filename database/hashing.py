import hashlib 

def hash_sha3_512(password):
    """
    Hashes a password using SHA3-512.
    Arguments:
        password <str>: The password to be hashed.
    """
    return hashlib.sha3_512(password.encode('utf-8')).hexdigest()