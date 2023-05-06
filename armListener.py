# Generated from arm_assembly.g4 by ANTLR 4.12.0
from antlr4 import *
from antlr.armParser import armParser

from converters.dp_instruction import DPInstruction
from converters.ls_instruction import LSInstruction
from converters.mov_instruction import MoveInstruction
from converters.multiply_instruction import MulInstruction, MlaInstruction
from converters.operand2 import ShiftOp, ImmediateFormat, RegisterFormat, Operand2
from converters.shift_instruction import ShiftInstruction
from converters.shift_operand import ShiftOperand

def get_number(hex, number):
    if hex is None:
        return int(number)
    return int(hex, 16)

def get_shift_type(shift_type):
    return ['LSL', 'LSR', 'ASR', 'ROR', 'RRX'].index(shift_type)

# This class defines a complete listener for a parse tree produced by armParser.
class armListener(ParseTreeListener):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instruction = None

    # Enter a parse tree produced by armParser#instruction.
    def enterInstruction(self, ctx:armParser.InstructionContext):
        pass

    # Exit a parse tree produced by armParser#instruction.
    def exitInstruction(self, ctx:armParser.InstructionContext):
        if ctx.dp_instruction():
            self.instruction = ctx.dp_instruction().value
        if ctx.mov_instruction():
            self.instruction = ctx.mov_instruction().value
        if ctx.shift_instruction():
            self.instruction = ctx.shift_instruction().value
        if ctx.mul_instruction():
            self.instruction = ctx.mul_instruction().value
        if ctx.mla_instruction():
            self.instruction = ctx.mla_instruction().value
        if ctx.ls_instruction():
            self.instruction = ctx.ls_instruction().value

    # Enter a parse tree produced by armParser#reg.
    def enterReg(self, ctx:armParser.RegContext):
        pass

    # Exit a parse tree produced by armParser#reg.
    def exitReg(self, ctx:armParser.RegContext):
        ctx.value = int(ctx.getText().upper()[1:])


    # Enter a parse tree produced by armParser#immediate.
    def enterImmediate(self, ctx:armParser.ImmediateContext):
        pass

    # Exit a parse tree produced by armParser#immediate.
    def exitImmediate(self, ctx:armParser.ImmediateContext):
        hex = ctx.HEX().getText().upper() if ctx.HEX() else None
        num = ctx.NUMBER().getText() if ctx.NUMBER() else None
        ctx.value = get_number(hex, num)

    # Enter a parse tree produced by armParser#dp_instruction.
    def enterDp_instruction(self, ctx:armParser.Dp_instructionContext):
        pass

    # Exit a parse tree produced by armParser#dp_instruction.
    def exitDp_instruction(self, ctx:armParser.Dp_instructionContext):
        obj = DPInstruction()
        obj.opcode = obj.mapping[ctx.opcode.text.upper()]
        obj.rd = ctx.reg(0).value
        obj.rn = ctx.reg(1).value
        obj.operand2 = ctx.operand2().value
        ctx.value = obj

    # Enter a parse tree produced by armParser#mov_instruction.
    def enterMov_instruction(self, ctx:armParser.Mov_instructionContext):
        pass

    # Exit a parse tree produced by armParser#mov_instruction.
    def exitMov_instruction(self, ctx:armParser.Mov_instructionContext):
        obj = MoveInstruction()
        obj.opcode = obj.mapping[ctx.opcode.text.upper()]
        obj.rd = ctx.reg().value
        obj.operand2 = ctx.operand2().value
        ctx.value = obj

    # Enter a parse tree produced by armParser#shift_instruction.
    def enterShift_instruction(self, ctx:armParser.Shift_instructionContext):
        pass

    # Exit a parse tree produced by armParser#shift_instruction.
    def exitShift_instruction(self, ctx:armParser.Shift_instructionContext):
        obj = ShiftInstruction()
        obj.rd = ctx.reg().value
        obj.shift_operand = ctx.shift_operand().value
        obj.shift_operand.shift_type = get_shift_type(ctx.opcode.text.upper())
        ctx.value = obj

    # Enter a parse tree produced by armParser#mul_instruction.
    def enterMul_instruction(self, ctx:armParser.Mul_instructionContext):
        pass

    # Exit a parse tree produced by armParser#mul_instruction.
    def exitMul_instruction(self, ctx:armParser.Mul_instructionContext):
        obj = MulInstruction()
        obj.rd = ctx.reg(0).value
        obj.rm = ctx.reg(1).value
        obj.rs = ctx.reg(2).value
        ctx.value = obj

    # Enter a parse tree produced by armParser#mla_instruction.
    def enterMla_instruction(self, ctx:armParser.Mla_instructionContext):
        pass

    # Exit a parse tree produced by armParser#mla_instruction.
    def exitMla_instruction(self, ctx:armParser.Mla_instructionContext):
        obj = MlaInstruction()
        obj.rd = ctx.reg(0).value
        obj.rm = ctx.reg(1).value
        obj.rs = ctx.reg(2).value
        obj.rn = ctx.reg(3).value
        ctx.value = obj

    # Enter a parse tree produced by armParser#ls_instruction.
    def enterLs_instruction(self, ctx:armParser.Ls_instructionContext):
        pass

    # Exit a parse tree produced by armParser#ls_instruction.
    def exitLs_instruction(self, ctx:armParser.Ls_instructionContext):
        obj = LSInstruction()
        obj.opcode = ctx.opcode.text.upper()
        obj.rt = ctx.reg(0).value
        obj.rn = ctx.reg(1).value
        if ctx.operand2():
            obj.operand2 = ctx.operand2().value
        ctx.value = obj

    # Enter a parse tree produced by armParser#shift_operand.
    def enterShift_operand(self, ctx:armParser.Shift_operandContext):
        pass

    # Exit a parse tree produced by armParser#shift_operand.
    def exitShift_operand(self, ctx:armParser.Shift_operandContext):
        obj = ShiftOperand()
        obj.rm = ctx.reg(0).value
        if ctx.immediate():
            obj.immediate = ctx.immediate().value
        else:
            obj.rs = ctx.reg(1).value
        ctx.value = obj

    # Enter a parse tree produced by armParser#operand2.
    def enterOperand2(self, ctx:armParser.Operand2Context):
        pass

    # Exit a parse tree produced by armParser#operand2.
    def exitOperand2(self, ctx:armParser.Operand2Context):
        obj = Operand2()
        if ctx.immediate_format():
            obj.immediate_format = ctx.immediate_format().value
        else:
            obj.register_format = ctx.register_format().value
        ctx.value = obj

    # Enter a parse tree produced by armParser#immediate_format.
    def enterImmediate_format(self, ctx:armParser.Immediate_formatContext):
        pass

    # Exit a parse tree produced by armParser#immediate_format.
    def exitImmediate_format(self, ctx:armParser.Immediate_formatContext):
        obj = ImmediateFormat()
        if ctx.COMMA():
            hex = ctx.HEX().getText() if ctx.HEX() else None
            num = ctx.NUMBER().getText() if ctx.NUMBER() else None
            obj.rotamt = get_number(hex, num)
        else:
            obj.rotamt = 0
        obj.number = ctx.immediate().value
        ctx.value = obj

    # Enter a parse tree produced by armParser#register_format.
    def enterRegister_format(self, ctx:armParser.Register_formatContext):
        pass

    # Exit a parse tree produced by armParser#register_format.
    def exitRegister_format(self, ctx:armParser.Register_formatContext):
        obj = RegisterFormat()
        obj.rm = ctx.reg().value
        if ctx.shift_op():
            obj.shiftop = ctx.shift_op().value

        ctx.value = obj

    # Enter a parse tree produced by armParser#shift_op.
    def enterShift_op(self, ctx:armParser.Shift_opContext):
        pass

    # Exit a parse tree produced by armParser#shift_op.
    def exitShift_op(self, ctx:armParser.Shift_opContext):
        obj = ShiftOp()
        obj.shift_type = ctx.shift_type().value
        if ctx.immediate_format():
            obj.immediate_format = ctx.immediate_format().value
        else:
            obj.rs = ctx.reg().value
        ctx.value = obj

    # Enter a parse tree produced by armParser#shift_type.
    def enterShift_type(self, ctx:armParser.Shift_typeContext):
        pass

    # Exit a parse tree produced by armParser#shift_type.
    def exitShift_type(self, ctx:armParser.Shift_typeContext):
        ctx.value = get_shift_type(ctx.getText().upper())



del armParser