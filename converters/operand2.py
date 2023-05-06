"""
Author: Yousuf Fauzan

Convert Operand2 to machine code.
"""
class ShiftOp(object):
    def __init__(self):
        self.shift_type = None
        self.immediate_format = None
        self.rs = None

    def convert(self):
        val = ''
        if self.immediate_format:
            val += self.immediate_format.convert_shiftamt()
        else:
            val += format(self.rs, '04b') + '0'
        val += format(self.shift_type, '02b')
        if self.immediate_format:
            val += '0'
        else:
            val += '1'
        return val

class ImmediateFormat(object):
    def __init__(self):
        self.rotamt = 0
        self.number = 0

    def convert(self):
        if self.rotamt == 0 and self.number > 255:
            self.number, self.rotamt = self.rotate(self.number)
        rotamt = format(self.rotamt,'05b')[:4]
        num = format(self.number,'08b')
        return rotamt + num

    def convert_shiftamt(self):
        return format(self.number,'05b')

    def rotate_left(self, x, n):
        return int(f"{x:032b}"[n:] + f"{x:032b}"[:n], 2)

    def rotate(self, n):
        rot = 0
        for rot in range(2, 32, 2):
            if self.rotate_left(n, rot) < 255:
                return self.rotate_left(n, rot), rot
        raise Exception("Unable to encode number %d", n)


class RegisterFormat(object):
    def __init__(self):
        self.shiftop = None
        self.rm = 0

    def convert(self):
        val = '0'*8
        if self.shiftop:
            val = self.shiftop.convert()
        val += format(self.rm, '04b')
        return val

class Operand2(object):
    def __init__(self):
        self.immediate_format = None
        self.register_format = None

    def convert(self):
        if self.immediate_format:
            return self.immediate_format.convert()
        return self.register_format.convert()

    def convert_scaled_register(self):
        if self.register_format is None:
            raise Exception("Only scaled register format allowed")
        if self.register_format.shiftop and self.register_format.shiftop.immediate_format is None:
            raise Exception("Only scaled register format allowed")
        return self.register_format.convert()
