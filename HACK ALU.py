class ALU:
    def __init__(self, bit_width=8):
        self.bit_width = bit_width

    def add(self, operand1, operand2):
        result = bin(int(operand1, 2) + int(operand2, 2))[2:]
        return result.zfill(self.bit_width)

    def subtract(self, operand1, operand2):
        result = bin(int(operand1, 2) - int(operand2, 2))[2:]
        return result.zfill(self.bit_width)

    def and_op(self, operand1, operand2):
        result = bin(int(operand1, 2) & int(operand2, 2))[2:]
        return result.zfill(self.bit_width)

    def or_op(self, operand1, operand2):
        result = bin(int(operand1, 2) | int(operand2, 2))[2:]
        return result.zfill(self.bit_width)

    def xor_op(self, operand1, operand2):
        result = bin(int(operand1, 2) ^ int(operand2, 2))[2:]
        return result.zfill(self.bit_width)

    def not_op(self, operand):
        result = bin(~int(operand, 2) & ((1 << self.bit_width) - 1))[2:]
        return result.zfill(self.bit_width)

if __name__ == "__main__":
    alu = ALU(bit_width=8)

    operand1 = input("Enter Operand 1 (8 bits): ")
    operand2 = input("Enter Operand 2 (8 bits): ")
    control_bits = input("Enter Control Bits (6 bits, e.g., 000000 for addition, 000001 for subtraction, etc.): ")

    print("Operand 1:", operand1)
    print("Operand 2:", operand2)
    print("Control Bits:", control_bits)

    result = ""

    if control_bits == "000000":
        result = alu.add(operand1, operand2)
    elif control_bits == "000001":
        result = alu.subtract(operand1, operand2)
    elif control_bits == "000010":
        result = alu.and_op(operand1, operand2)
    elif control_bits == "000011":
        result = alu.or_op(operand1, operand2)
    elif control_bits == "000100":
        result = alu.xor_op(operand1, operand2)
    elif control_bits == "000101":
        result = alu.not_op(operand1)
    else:
        print("Invalid control bits entered. Please enter a valid combination.")
        exit(1)

    print("Result (Binary):", result)

    if result:
        # Remove the 'b' prefix and then convert to decimal, octal, and hexadecimal
        result_decimal = int(result[1:], 2)
        result_octal = oct(result_decimal)
        result_hexadecimal = hex(result_decimal)

        print("Result (Decimal):", result_decimal)
        print("Result (Octal):", result_octal)
        print("Result (Hexadecimal):", result_hexadecimal)
