"""
Author: Yousuf Fauzan

Convert Shift Instruction to machine code. It uses Shift Operand (shift_operand.py)
"""
class ShiftInstruction(object):
    def __init__(self):
        self.rd = None
        self.shift_operand = None

    def convert(self):
        # Cond Code
        val = '1110'
        # OpType
        #if self.shift_operand.immediate is not None:
            #val += '001'
        #else:
        val += '000'
        # Opcode
        val += '1101'
        # S
        val += '0'
        # Rn
        val += '0000'
        # Rd
        val += format(self.rd, '04b')
        # Operand2
        val += self.shift_operand.convert()
        return val