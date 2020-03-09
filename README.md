# Hashcatomator
A small tool to automatize wordlist attacks on Truecrypt and Veracrypt Volumes using Hashcat

What it does:
- works his way through all Truecrypt/Veracrypt Hashcat Methods in all combinations as seen below
- automatically uses all dictionaries in the given folder

What do you need:
- Hashcat preinstalled (https://hashcat.net/hashcat/)
- Location of Hashcat
- Location and Name of the Hash u want to attack
- Location of the folder containing the dictionaries
- if u want to do True- or Veracrypt(if unknown try Truecrypt first, as it is much faster overall)

Hashcat Methods used:

   62XY | TrueCrypt                                        | Full-Disk Encryption (FDE)
     X  | 1 = PBKDF2-HMAC-RIPEMD160                        | Full-Disk Encryption (FDE)
     X  | 2 = PBKDF2-HMAC-SHA512                           | Full-Disk Encryption (FDE)
     X  | 3 = PBKDF2-HMAC-Whirlpool                        | Full-Disk Encryption (FDE)
     X  | 4 = PBKDF2-HMAC-RIPEMD160 + boot-mode            | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure AES                        | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure Serpent                    | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure Twofish                    | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure AES                        | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure Serpent                    | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure Twofish                    | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded AES-Twofish            | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Serpent-AES            | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Twofish-Serpent        | Full-Disk Encryption (FDE)
      Y | 3 = XTS 1536 bit all                             | Full-Disk Encryption (FDE)

  137XY | VeraCrypt                                        | Full-Disk Encryption (FDE)
     X  | 1 = PBKDF2-HMAC-RIPEMD160                        | Full-Disk Encryption (FDE)
     X  | 2 = PBKDF2-HMAC-SHA512                           | Full-Disk Encryption (FDE)
     X  | 3 = PBKDF2-HMAC-Whirlpool                        | Full-Disk Encryption (FDE)
     X  | 4 = PBKDF2-HMAC-RIPEMD160 + boot-mode            | Full-Disk Encryption (FDE)
     X  | 5 = PBKDF2-HMAC-SHA256                           | Full-Disk Encryption (FDE)
     X  | 6 = PBKDF2-HMAC-SHA256 + boot-mode               | Full-Disk Encryption (FDE)
     X  | 7 = PBKDF2-HMAC-Streebog-512                     | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure AES                        | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure Serpent                    | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure Twofish                    | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure Camellia                   | Full-Disk Encryption (FDE)
      Y | 1 = XTS  512 bit pure Kuznyechik                 | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure AES                        | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure Serpent                    | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure Twofish                    | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure Camellia                   | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit pure Kuznyechik                 | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded AES-Twofish            | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Camellia-Kuznyechik    | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Camellia-Serpent       | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Kuznyechik-AES         | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Kuznyechik-Twofish     | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Serpent-AES            | Full-Disk Encryption (FDE)
      Y | 2 = XTS 1024 bit cascaded Twofish-Serpent        | Full-Disk Encryption (FDE)
      Y | 3 = XTS 1536 bit all                             | Full-Disk Encryption (FDE)
      
Comment Language: German
