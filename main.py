from Cryptodome.Util import number as num
from random import randint
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import binascii


# Function code
def fast_exp(base, exp, mod):
    r = 1
    if 1 & exp:
        r = base
    while exp:
        exp >>= 1
        base = (base * base) % mod
        if exp & 1: r = (r * base) % mod
    return r

def euclidean(n_phi, n_e):
    n_e2 = 1
    tab1 = [n_phi, n_phi]
    tab2 = [n_e, n_e2]
    while tab2[0] != 1:
        nn = tab1[0] // tab2[0]
        tmp1 = tab2[0] * nn
        tmp2 = tab2[1] * nn
        new1 = tab1[0] - tmp1
        new2 = tab1[1] - tmp2
        if new2 < 0:
            new2 = new2 % n_phi
        tab1[0] = tab2[0]
        tab1[1] = tab2[1]
        tab2[0] = new1
        tab2[1] = new2
    return tab2[1]

def generate():
    f = True
    n_length = int(input("\nIntroduce the length of your key (2048 bytes common and faster / 4096 bytes safest): "))
    while f:
        e = 65537
        p = num.getPrime(n_length//2)
        q = num.getPrime(n_length//2)
        n = p*q
        phi = (p-1)*(q-1)
        if phi % e == 0:
            pass
        else:
            break
    #print(f"Your p number is: {p}\nYour q number is: {q}\nYour modulus is: {n}\nPhi is: {phi}")
    d = euclidean(phi, e)
    #print(f"Your e number is {e}")
    #print(f"Your d number is {d}")

    m = randint(5000,9000)
    c = (m**e) % n
    dec = fast_exp(c,d,n)
    if dec != m:
        print("ALERT, SOMETHING WENT WRONG, GENERATE YOUR KEYS AGAIN")
        return 0
    rsaKey = RSA.construct((n, e))

    pubKey = rsaKey.export_key()
    pubKey = pubKey.decode('ascii')
    comps = [n, e, d]
    privrsaKey = RSA.construct(comps);
    privKey = privrsaKey.export_key()
    privKey = privKey.decode('ascii')
    print("This are your keys: \n")
    print(f"\n{pubKey}")
    print(f"\n{privKey}")
    do = input("\n\nDo you wish to export them?\n Introduce y (yes) or n (no): ")
    while (do != 'y') and (do != 'n'):
        do = input("\n\nDo you wish to export them?")
    if do == 'y':
        text_file = open("pubKey.txt", 'wt')
        text_file.write(pubKey)
        text_file.close()
        text_file = open("privKey.txt", 'wt')
        text_file.write(privKey)
        text_file.close()
    if do == 'n':
        return 0

def encrypt(msg, pubKey):
    encryptor = PKCS1_OAEP.new(pubKey)
    string = bytes(msg, encoding='utf-8')
    encrypted = encryptor.encrypt(string)
    encrypted = binascii.hexlify(encrypted)

    return encrypted


if __name__ == '__main__':
    action = input("\nYou are welcome to @gasparllamazares RSA key generator, please choose an option.\n\n1) Generate Key Pair\n2) Import Key Pair (Not available yet)\n\nIntroduce option: ")
    while action != ('1'):
        action = input("Please select a valid option: ")
    if action == '1':
        generate()
    if action == '2':
        print("Option under development, coming soon...")

    #string = input("\nIntroduce un texto para encriptar: ")
    #encrypted = encrypt(string, pubkey)
    #encrypted = encrypted.decode("utf-8")
    #print(f"The encrypted string with your public key is: {encrypted}")

