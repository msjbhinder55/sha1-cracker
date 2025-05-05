import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load the top 10,000 passwords
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = [line.strip() for line in f.readlines()]
    
    # Load salts if needed
    salts = []
    if use_salts:
        with open('known-salts.txt', 'r') as f:
            salts = [line.strip() for line in f.readlines()]
    
    for password in passwords:
        if use_salts:
            # Try each salt with prepend and append
            for salt in salts:
                # Prepend salt
                salted_password = salt + password
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == hash:
                    return password
                
                # Append salt
                salted_password = password + salt
                hashed = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed == hash:
                    return password
        else:
            # Try plain password
            hashed = hashlib.sha1(password.encode()).hexdigest()
            if hashed == hash:
                return password
    
    return "PASSWORD NOT IN DATABASE"