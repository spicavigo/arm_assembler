"""
Author: Yousuf Fauzan

Convert MUL and MLA Instruction to machine code.
"""
class MulInstruction(object):
    def __init__(self):
        self.rd = None
        self.rm = None
        self.rs = None

    def convert(self):
        # Cond Code
        val = '1110'
        # OpType
        val += '000'
        # Opcode
        val += '000'
        # A
        val += '0'
        # S
        val += '0'
        # Rd
        val += format(self.rd, '04b')
        # Rn
        val += '0000'
        # Rs
        val += format(self.rs, '04b')
        # Multicd
        val += '1001'
        # Rm
        val += format(self.rm, '04b')
        return val

class MlaInstruction(object):
    def __init__(self):
        self.rd = None
        self.rm = None
        self.rs = None
        self.rn = None

    def convert(self):
        # Cond Code
        val = '1110'
        # OpType
        val += '000'
        # Opcode
        val += '000'
        # A
        val += '1'
        # S
        val += '0'
        # Rd
        val += format(self.rd, '04b')
        # Rn
        val += format(self.rn, '04b')
        # Rs
        val += format(self.rs, '04b')
        # Multicd
        val += '1001'
        # Rs
        val += format(self.rm, '04b')
        return val