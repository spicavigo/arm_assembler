"""
Author: Yousuf Fauzan

Convert Data Processing Instruction to machine code. It uses Operand2 (operand2.py)
"""
class DPInstruction(object):
    def __init__(self):
        self.mapping = {
            'AND': 0,
            'ADD': 4,
            'SUB': 2,
            'EOR': 1,
            'ORR': 12
        }
        self.opcode = None
        self.rd = None
        self.rn = None
        self.operand2 = None


    def convert(self):
        # Cond Code
        val = '1110'
        # OpType
        if self.operand2.immediate_format:
            val += '001'
        else:
            val += '000'
        # Opcode
        val += format(self.opcode, '04b')
        # S
        val += '0'
        # Rn
        val += format(self.rn, '04b')
        # Rd
        val += format(self.rd, '04b')
        # Operand2
        val += self.operand2.convert()
        return val