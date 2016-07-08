#!/usr/bin/env python


class LFSR(list):
    """
    Linear Feedback Shift Registers

    Each index is a register.

    https://en.wikipedia.org/wiki/Linear-feedback_shift_register
    """

    def __init__(self, *bits):
        """
        Bits should be 0 or 1
        """
        assert len(bits) > 3, "LFSRs require at least 3 registers."
        self._q = [*bits]

    def shift(self, bit=0):
        self._q.pop()
        self._q = [bit, *self._q]
        return self._q

    def lf_shift(self):
        "Linear feedback shift -- XORs the last 2"
        self.shift(self._q[-1] ^ self._q[-2])

    def __repr__(self):
        return str(self._q)

    def __str__(self):
        return str(self._q)

lfsr = LFSR(0, 0, 0, 1)

for i in range(16):
    lfsr.lf_shift()
    print(lfsr)
