"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
    # Set Instruction Constants
    INST_LDI  = 0b10000010
    INST_HLT  = 0b00000001
    INST_PRN  = 0b01000111
    INST_ADD  = 0b10100000
    INST_SUB  = 0b10100001
    INST_MUL  = 0b10100010
    INST_DIV  = 0b10100011
    INST_AND  = 0b10101000
    INST_OR   = 0b10101010
    INST_XOR  = 0b10101011
    INST_NOT  = 0b01101001
    INST_SHL  = 0b10101100
    INST_SHR  = 0b10101101
    INST_CALL = 0b01010000
    INST_RET  = 0b00010001
    INST_PUSH = 0b01000101
    INST_POP  = 0b01000110
    INST_CMP  = 0b10100111
    INST_INC  = 0b01100101
    INST_DEC  = 0b01100110
    INST_PRA  = 0b01001000
    INST_JEQ  = 0b01010101
    INST_LD   = 0b10000011
    INST_JMP  = 0b01010100
    INST_ST   = 0b10000100
    INST_IRET = 0b00010011
    INST_JNE  = 0b01010110
    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0b00000000] * 256
        self.reg = [0b00000000] * 8
        self.reg[7] = 0x74
        self.pc = 0
        self.flag = 0b00000000
        self.time = datetime.now().second
        self.time_prev = self.time

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass
