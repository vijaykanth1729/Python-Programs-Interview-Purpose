# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Enter a value to generate password: "))
if passlen>75:
    raise Exception("Your password length should be below 75")
else:
    p =  "".join(random.sample(s,passlen ))
    print(p)
