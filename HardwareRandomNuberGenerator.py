import os
from Crypto.Random import random

rand_bytes = os.urandom(4)
rand_int = int.from_bytes(rand_bytes, byteorder="big") % 10 + 1
print(rand_int)