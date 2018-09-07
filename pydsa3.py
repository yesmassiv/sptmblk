from Crypto.PublicKey import DSA


def create_dsa_keys(code):
    key = DSA.generate(1024)
    encrypted_key = key.exportKey(
        passphrase=code,
        pkcs8=True,
        protection="PBKDF2WithHMAC-SHA1AndDES-EDE3-CBC"
    )

    with open("private_rsa_key.bin", "wb") as f:
        f.write(encrypted_key)
    with open("my_rsa_public.pem", "wb") as f:
        f.write(key.publickey().exportKey())
    return key.publickey().exportKey()


code = "somecode"

create_dsa_keys(code)
