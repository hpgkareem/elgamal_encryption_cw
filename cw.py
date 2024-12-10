import random
def prime_number(number):

    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):  
        if number % i == 0:
            return False
    return True
    

def key_generation():

    P = 107 # do not, define p and g in the code, generate them
    G = 10 # sets, a bunch of for loops
    if not prime_number(P):
        raise ValueError("P must be a prime number.")
    if G <= 1 or G >= P:
        raise ValueError("G must be between 2 and P-1.")

    X = random.randint(1, P-2)
    H = (G^X) % P

    public_key = (P, G, H)
    private_key = X
    return public_key, private_key



def encrypt_the_message(public_key, message):

    P, G, H = public_key  
    K = random.randint(1, P - 2)  
    cipher1 = (G^K) % P  
    m = message
    cipher2 = (m * ((H^K) % P)) % P 
    ciphertext = (cipher1, cipher2)
    return ciphertext
 


def decrypt_the_message(ciphertext, private_key, public_key):

    cipher1, cipher2 = ciphertext  
    x = private_key  
    P, G, H = public_key  
    secret = (cipher1^x) % P
    secret_reversed = (secret^-1) % P  
    m = (cipher2 * secret_reversed) % P  
    return m


public_key, private_key = key_generation()
print(f"Public Key: {public_key} & private key: {private_key}") 


message = int(input("enter your message here:")) # needs to allow strings as well
if not (0 <= message < public_key[0]):
        raise ValueError(f"Message must be between 0 and {public_key[0] - 1}.")

ciphertext = encrypt_the_message(public_key, message)
print(f"Ciphertext: {ciphertext}")

decrypted_message = decrypt_the_message(ciphertext, private_key, public_key)
print(f"Decrypted Message: {decrypted_message}")



