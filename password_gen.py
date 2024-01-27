import random

lwr = "abcdefghijklmnopqrstuvwxyz"
upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbols = "!@#$%&[]{}"

all = lwr + upr + num + symbols
length = 8
password = "".join(random.sample(all,length))
print(password)
# 