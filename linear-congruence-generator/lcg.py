#!/usr/bin/env python
import time

def lcg(seed, modulus, a, c):
    """
    Method for Linear Congruence Generator

    seed
    modulus
    a
    c
    """
    return (seed * a + c) % modulus


def default_lcg(seed=1):
    return lcg(seed, 9, 2, 0)


STATE = 1


def main():
    global STATE
    for i in range(8):
        STATE = default_lcg(STATE)
        print("{0}: {1}".format(i, STATE))

if __name__ == '__main__':
    main()
