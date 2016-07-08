#!/usr/bin/env python


class ShiftRegister(list):
    "Implemented as a queue"

    def __init__(self, *bits):
        self._q = [*bits]

    def shift(self, bit=0):
        self._q.pop()
        self._q = [bit, *self._q]
        return self._q

    def __repr__(self):
        return str(self._q)

sr = ShiftRegister(0, 0, 0)
sr.shift(1)
