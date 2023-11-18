# hack-alu
This repository contains a simple implementation of a HACK ALU (Arithmetic Logic Unit) in Python. The ALU supports basic arithmetic and logic operations such as addition, subtraction, AND, OR, XOR, and NOT.

>> ALU Operations
The ALU supports the following operations:

Addition: Control Bits 000000
Subtraction: Control Bits 000001
AND: Control Bits 000010
OR: Control Bits 000011
XOR: Control Bits 000100
NOT (Operand 1): Control Bits 000101

>> Example Usage:

Enter Operand 1 (8 bits): 10101100
Enter Operand 2 (8 bits): 11011010
Enter Control Bits (6 bits, e.g., 000000 for addition, 000001 for subtraction, etc.): 000000

Operand 1: 10101100
Operand 2: 11011010
Control Bits: 000000
Result (Binary): 11000110
Result (Decimal): 198
Result (Octal): 306
Result (Hexadecimal): 0xc6
