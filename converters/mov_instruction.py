"""
Author: Yousuf Fauzan

Convert Move Instruction to machine code. It uses Operand2 (operand2.py)
"""
class MoveInstruction(object):
    def __init__(self):
        self.mapping = {
            'MOV': 13,
            'MVN': 15,
        }
        self.opcode = None
        self.rd = None
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
        val += '0000'
        # Rd
        val += format(self.rd, '04b')
        # Operand2
        val += self.operand2.convert()
        return val