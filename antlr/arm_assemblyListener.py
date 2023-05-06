# Generated from arm_assembly.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .arm_assemblyParser import arm_assemblyParser
else:
    from arm_assemblyParser import arm_assemblyParser

# This class defines a complete listener for a parse tree produced by arm_assemblyParser.
class arm_assemblyListener(ParseTreeListener):

    # Enter a parse tree produced by arm_assemblyParser#reg.
    def enterReg(self, ctx:arm_assemblyParser.RegContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#reg.
    def exitReg(self, ctx:arm_assemblyParser.RegContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#immediate.
    def enterImmediate(self, ctx:arm_assemblyParser.ImmediateContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#immediate.
    def exitImmediate(self, ctx:arm_assemblyParser.ImmediateContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#instruction.
    def enterInstruction(self, ctx:arm_assemblyParser.InstructionContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#instruction.
    def exitInstruction(self, ctx:arm_assemblyParser.InstructionContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#dp_instruction.
    def enterDp_instruction(self, ctx:arm_assemblyParser.Dp_instructionContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#dp_instruction.
    def exitDp_instruction(self, ctx:arm_assemblyParser.Dp_instructionContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#mov_instruction.
    def enterMov_instruction(self, ctx:arm_assemblyParser.Mov_instructionContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#mov_instruction.
    def exitMov_instruction(self, ctx:arm_assemblyParser.Mov_instructionContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#shift_instruction.
    def enterShift_instruction(self, ctx:arm_assemblyParser.Shift_instructionContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#shift_instruction.
    def exitShift_instruction(self, ctx:arm_assemblyParser.Shift_instructionContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#mul_instruction.
    def enterMul_instruction(self, ctx:arm_assemblyParser.Mul_instructionContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#mul_instruction.
    def exitMul_instruction(self, ctx:arm_assemblyParser.Mul_instructionContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#mla_instruction.
    def enterMla_instruction(self, ctx:arm_assemblyParser.Mla_instructionContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#mla_instruction.
    def exitMla_instruction(self, ctx:arm_assemblyParser.Mla_instructionContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#ls_instruction.
    def enterLs_instruction(self, ctx:arm_assemblyParser.Ls_instructionContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#ls_instruction.
    def exitLs_instruction(self, ctx:arm_assemblyParser.Ls_instructionContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#shift_operand.
    def enterShift_operand(self, ctx:arm_assemblyParser.Shift_operandContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#shift_operand.
    def exitShift_operand(self, ctx:arm_assemblyParser.Shift_operandContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#operand2.
    def enterOperand2(self, ctx:arm_assemblyParser.Operand2Context):
        pass

    # Exit a parse tree produced by arm_assemblyParser#operand2.
    def exitOperand2(self, ctx:arm_assemblyParser.Operand2Context):
        pass


    # Enter a parse tree produced by arm_assemblyParser#immediate_format.
    def enterImmediate_format(self, ctx:arm_assemblyParser.Immediate_formatContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#immediate_format.
    def exitImmediate_format(self, ctx:arm_assemblyParser.Immediate_formatContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#register_format.
    def enterRegister_format(self, ctx:arm_assemblyParser.Register_formatContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#register_format.
    def exitRegister_format(self, ctx:arm_assemblyParser.Register_formatContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#shift_op.
    def enterShift_op(self, ctx:arm_assemblyParser.Shift_opContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#shift_op.
    def exitShift_op(self, ctx:arm_assemblyParser.Shift_opContext):
        pass


    # Enter a parse tree produced by arm_assemblyParser#shift_type.
    def enterShift_type(self, ctx:arm_assemblyParser.Shift_typeContext):
        pass

    # Exit a parse tree produced by arm_assemblyParser#shift_type.
    def exitShift_type(self, ctx:arm_assemblyParser.Shift_typeContext):
        pass



del arm_assemblyParser