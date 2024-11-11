from Cryptodome.Cipher import AES
from hashlib import md5
encrypted_mail = bytes([0x68, 0xda, 0xe1, 0x1b, 0x20, 0x6e, 0xbc, 0x1f, 0x1, 0xff, 0x6f, 0x4, 0x89, 0x8a, 0x6e, 0x1d])

for yy in range(100):
    for mm in range(1, 13):
        for dd in range(1, 32):
            yymmdd = "%02d%02d%02d" % (yy, mm, dd)
            key = md5(yymmdd.encode()).digest()
            cipher = AES.new(key, AES.MODE_CBC, key)
            dat = cipher.decrypt(encrypted_mail)
            try:
                decrypted_text = dat.decode('utf-8')
                print(decrypted_text)
                if decrypted_text.startswith("data:"):
                    print("Found!", yymmdd)
                    exit()
            except UnicodeDecodeError:
                #print(yymmdd)
                # Continue if the decrypted text is not a valid UTF-8 string
                continue
