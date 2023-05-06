"""
Author: Yousuf Fauzan

Program to test this assembler
"""

from antlr4 import *
from antlr.arm_Lexer import arm_Lexer
from antlr.arm_Parser import arm_Parser
from armListener import armListener
import sys

def printval(val):
    print(f'Binary:     {val[:4]} {val[4:7]} {val[7:11]} {val[11]} {val[12:16]} {val[16:20]} {val[20:]}')
    print(f'Hex:        {hex(int(val, 2))}')
    print()

def assemble(command):
    lexer = arm_assemblyLexer(InputStream(command))
    stream = CommonTokenStream(lexer)
    parser = arm_assemblyParser(stream)
    tree = parser.instruction()
    printer = armListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    val = printer.instruction.convert()
    print(f'Assembling: {lexer.inputStream.strdata}')
    printval(val)
    return hex(int(val, 2))

assert assemble('MOV r1, r2') == '0xe1a01002'
assert assemble('MOV r1, #3, 4') == '0xe3a01203'
assert assemble('MOV r1, r2, lsl #3') == '0xe1a01182'
assert assemble('LSL r1, r2, #3') == '0xe1a01182'
assert assemble('MOV r1, r2, ASR r3') == '0xe1a01352'
assert assemble('ASR r1, r2, r3') == '0xe1a01352'
assert assemble('add    r7, r3, #5') == '0xe2837005'
assert assemble('sub    r8, r6, r3') == '0xe0468003'
assert assemble('mul    r3, r4, r5') == '0xe0030594'
assert assemble('mla    r1, r2, r3, r4') == '0xe0214392'
assert assemble('ldr    r1, [r2]') == '0xe5921000'
assert assemble('ldr r1, [r2, #12]') == '0xe592100c'
assert assemble('ldr    r2, [r0, #4]') == '0xe5902004'
assert assemble('str    r1, [r2, r3]') == '0xe7821003'
assert assemble('STR r1, [r2, r3, lsl #2]') == '0xe7821103'
