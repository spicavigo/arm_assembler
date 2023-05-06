grammar arm_assembly;

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

// Registers
R0: R '0';
R1: R '1';
R2: R '2';
R3: R '3';
R4: R '4';
R5: R '5';
R6: R '6';
R7: R '7';
R8: R '8';
R9: R '9';
R10: R '10';
R11: R '11';
R12: R '12';
R13: (R '13')|(S P);
R14: (R '14')|(L R);
R15: (R '15')|(P C);

// Data Ops
AND: A N D;
EOR: E O R;
SUB: S U B;
ADD: A D D;
ORR: O R R;
MOV: M O V;
MVN: M V N;

// Multiply Ops
MUL : M U L;
MLA : M L A;

// Load and Store Ops
LDR : L D R;
STR : S T R;

// Shift Ops
LSL: L S L;
LSR: L S R;
ASR: A S R;
ROR: R O R;
RRX: R R X;

LABEL: '.'?[a-zA-Z_]+ ':';

//Literals
HASH: '#';
HEX: '0' X ([0-9a-fA-F])+;
NUMBER: '-'? [0-9]+ ;

LBRACKET: '[';
RBRACKET: ']';
SPACE: (' '|'\t')+;
COMMA: ',' SPACE?;
WS: [ \t\r\n]+ -> skip;

reg: (R0|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15);
immediate: HASH (HEX|NUMBER);

instruction: dp_instruction 
			| mov_instruction 
			| shift_instruction 
			| mul_instruction
			| mla_instruction
			| ls_instruction;

dp_instruction: opcode=(ADD|SUB|AND|EOR|ORR) SPACE reg COMMA reg COMMA operand2;

mov_instruction: opcode=(MOV|MVN) SPACE reg COMMA operand2;

shift_instruction: opcode=(LSL|LSR|ASR|ROR|RRX) SPACE reg COMMA shift_operand;

mul_instruction: MUL SPACE reg COMMA reg COMMA reg;

mla_instruction: MLA SPACE reg COMMA reg COMMA reg COMMA reg;

ls_instruction: opcode=(LDR|STR) SPACE reg COMMA LBRACKET reg (COMMA operand2)? RBRACKET;

shift_operand: reg COMMA (immediate|reg);

operand2: immediate_format | register_format;

immediate_format: immediate | immediate COMMA (HEX|NUMBER);

register_format: reg | reg COMMA shift_op;

shift_op: shift_type SPACE (immediate_format|reg);

shift_type: LSL|LSR|ASR|ROR|RRX;
