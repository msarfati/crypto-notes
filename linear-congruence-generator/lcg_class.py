#!/usr/bin/env python
from functools import reduce

DEFAULT_CONFIG = dict(seed=1, modulus=9, a=2, c=0)
POSIX_CONFIG = dict(seed=12345, modulus=2**48, a=0x5DEECE66D, c=11)


class LCG:
    """
    Implementation of Linear Congruential Generator (LCG)

    Ref: https://en.wikipedia.org/wiki/Linear_congruential_generator
    """
    def __init__(self, seed=1, modulus=9, a=2, c=0):
        self.first_seed = seed
        self.seed = seed
        self.modulus = modulus
        self.a = a
        self.c = c

    def step(self):
        self.seed = (self.seed * self.a + self.c) % self.modulus
        return self.seed

str_to_ord = lambda s: [ord(i) for i in s]
ord_to_str = lambda s: reduce(lambda string, c: string + c, [chr(i) for i in s])


def main():
    key = 1337  # Keys are merely numbers for now
    configuration = dict(seed=key, modulus=2**48, a=0x5DEECE66D, c=11)  # Config (except seed) pulled from POSIX glibc

    # Encryption
    lcb = LCG(**configuration)
    plaintext = str_to_ord("Hello world!")
    print("Original plaintext:", ord_to_str(plaintext))
    ciphertext = []
    for i in plaintext:
        ciphertext.append(i ^ lcb.step())
    print("Ciphertext:", ciphertext)

    # Decryption
    lcb = LCG(**configuration)
    plaintext = []
    for i in ciphertext:
        plaintext.append(i ^ lcb.step())
    print("Plaintext:", ord_to_str(plaintext))

if __name__ == '__main__':
    main()
