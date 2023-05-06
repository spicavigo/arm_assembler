# Assembler for ARM

## Antlr Setup

https://github.com/antlr/antlr4/blob/master/doc/getting-started.md

## Generate parser etc.

First generate the antlr4 files (cd into antlr folder):

`antlr4 -Dlanguage=Python3 arm.g4 -visitor`

Test the assembling:

`python3 assembler.py`
