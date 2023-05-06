"""
Author: Yousuf Fauzan

Convert Load and Store Instruction to machine code. It uses Operand2 (operand2.py)
"""
class LSInstruction(object):
    def __init__(self):
        self.opcode = None
        self.rt = None
        self.rn = None
        self.operand2 = None
        self.immediate = None

    def convert(self):
        if self.operand2 is None:
            self.immediate = 0
        if self.operand2 and self.operand2.immediate_format:
            self.immediate = self.operand2.immediate_format.number
            self.operand2 = None
        # Cond Code
        val = '1110'
        # OpType
        if self.immediate is not None:
            # Immediate format
            val += '010'
        else:
            val += '011'
        # Opcode
        if self.immediate is not None and self.immediate < 0:
            self.immediate = abs(self.immediate)
            val += '1000'
        else:
            val += '1100'
        # L/S
        if self.opcode == 'LDR':
            val += '1'
        else:
            val += '0'
        # Rn
        val += format(self.rn, '04b')
        # Rt
        val += format(self.rt, '04b')
        # Immediate or Scaled Register
        if self.immediate is not None:
            val += format(self.immediate,'012b')
        else:
            val += self.operand2.convert_scaled_register()
        return val