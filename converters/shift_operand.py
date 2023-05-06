"""
Author: Yousuf Fauzan

Convert Shift Operand to machine code.
"""
class ShiftOperand(object):
    def __init__(self):
        self.rm = None
        self.rs = None
        self.immediate = None
        self.shift_type = None

    def convert(self):
        val = ''
        # ShAmt
        if self.immediate is not None:
            val += format(self.immediate,'05b')
        else:
            val += format(self.rs, '04b') + '0'
        val += format(self.shift_type, '02b')
        if self.immediate:
            val += '0'
        else:
            val += '1'
        val += format(self.rm, '04b')
        return val