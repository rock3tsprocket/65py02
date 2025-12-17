# i am not sorry for what you're about to see :)

""" Group one instructions """

""" BBB = 0b000: (Zero page,X);
    BBB = 0b001: Zero page;
    BBB = 0b010: Immediate;
    BBB = 0b011: Absolute;
    BBB = 0b100: (Zero page,Y);
    BBB = 0b101: Zero page,X;
    BBB = 0b110: Absolute,X;
    BBB = 0b111: Absolute,Y
"""

# OR Accumulator (AAA = 0b000)
def ORA(num, bbb, A):
    global a;
    if bbb == 0b000:
        print("WIP (ORA bbb=0)");

    if bbb == 0b010:
        A[0] = A[0] | num;
    elif bbb == 0b011:
        A[0] = A[0] | mem[num];
    elif bbb == 0b100:
        A[0] = A[0] | num;
    a = A;

# AND Accumulator (AAA = 0b001)
def AND(num, bbb, A):
    global a;
    if bbb == 0b000:
        print("WIP (AND bbb=0)");

    if bbb == 0b010:
        A[0] = (A[0] & num);
    elif bbb == 0b011:
        A[0] = (A[0] & mem[num]);
    elif bbb == 0b100:
        A[0] = A[0] & num;
    a = A;

# EOR/XOR Accumulator (AAA = 0b010)
def EOR(num, bbb, A):
    global a;
    if bbb == 0b000:
        print("WIP (ORA bbb=0)");

    if bbb == 0b010:
        A[0] = A[0] ^ num;
    elif bbb == 0b011:
        A[0] = A[0] ^ mem[num];
    elif bbb == 0b100:
        A[0] = A[0] ^ num;
    a = A;

# Add With Carry (to accumulator) (AAA = 0b011)
def ADC(num, bbb, A, Flags):
    global a, flags;
    if bbb == 0b000:
        print("WIP (ADC bbb=0)");
    elif bbb == 0b010:
        try:
            A[0] = A[0] + num;
        except ValueError:
            A[0] = (num - 0x1) - 0xFF;
            Flags[0] = Flags[0] | 0b00000001;
    elif bbb == 0b011:
        try:
            A[0] = A[0] + mem[num];
        except ValueError:
            A[0] = (mem[num] - 0x1) - 0xFF;
            Flags[0] = Flags[0] | 0b00000001;
    elif bbb == 0b100:
        try:
            A[0] = A[0] + num;
        except ValueError:
            A[0] = (num - 0x1) - 0xFF;
            Flags[0] = Flags[0] | 0b00000001;
    a = A;
    flags = Flags;

# Store Accumulator (AAA = 0b100)
def STA(num, bbb, A):
    print("Not implemented (STA)");

# Load value to Accumulator (AAA = 0b101)
def LDA(num, bbb, A):
    print("Not implemented (LDA)");

# Compare value to Accumulator (AAA = 0b110)
def CMP(num, bbb, A, Flags):
    global flags;
    if bbb == 0b000:
        print("WIP (CMP bbb=0)");
    elif bbb == 0b010:
        if A[0] >= num:
            Flags[0] = (Flags[0] | 0b00000011) & 0b01111111;
        else:
            pass;
    elif bbb == 0b011:
        if A[0] >= mem[num]:
            Flags[0] = (Flags[0] | 0b00000011) & 0b01111111;
        else:
            pass;
    elif bbb == 0b100:
        if A[0] >= num:
            Flags[0] = (Flags[0] | 0b00000011) & 0b01111111;
        else:
            pass;
    flags = Flags;

# Subtract with carry (from accumulator) (AAA = 0b111)
def SBC(num, bbb, A):
    global a;
    if bbb == 0b000:
        print("WIP (SBC bbb=0)");
    elif bbb == 0b010:
        try:
            A[0] = A[0] - num;
        except ValueError:
            A[0] = 0xFF + A[0] - num;
    elif bbb == 0b011:
        try:
            A[0] = A[0] - mem[num];
        except ValueError:
            A[0] = 0xFF + A[0] - mem[num];
    elif bbb == 0b100:
        try:
            A[0] = A[0] - num;
        except ValueError:
            A[0] = 0xFF + A[0] - num;
    a = A;


""" Group two instructions """

""" BBB = 0b000: Immediate;
*    BBB = 0b001: Zero page;
*    BBB = 0b010: Accumulator;
*    BBB = 0b011: Absolute;
*    BBB = 0b101: Zero page,Y if instruction is STX/LDX else Zero page,X;
*    BBB = 0b111: Absolute,Y if instruction is LDX else Absolute,X
"""

# Arithmetic Shift Left (AAA = 0b000)
def ASL(num, bbb, A, Flags):
    global a, flags;
    if bbb == 0b001:
        mem[num] = mem[num] << 1;
        Flags[0] = Flags[0] | 0b00000010 if not mem[num] else flags[0] & 0b11111101;
    elif bbb == 0b010:
        A[0] = A[0] << 1;
        Flags[0] = Flags[0] | 0b00000010 if not A[0] else flags[0] & 0b11111101;
    elif bbb == 0b011:
        mem[num] = mem[num] << 1;
        Flags[0] = Flags[0] | 0b00000010 if not mem[num] else flags[0] & 0b11111101;
    elif bbb == 0b101:
        mem[(num+x[0])%0xFF] = mem[(num+x[0])%0xFF] << 1;
        Flags[0] = Flags[0] | 0b00000010 if not mem[(num+x)%0xFF] else flags[0] & 0b11111101;
    elif bbb == 0b111:
        mem[num+x[0]%0xFFFF] = mem[(num+x[0])%0xFFFF] << 1;
        Flags[0] = Flags[0] | 0b00000010 if not mem[(num+x)%0xFFFF] else flags[0] & 0b11111101;
    a = A;


""" Conditional branching instructions """

# BRK is in main.py due to reasons


""" Some single-byte instructions """

# Clear Carry flag (0x18)
def CLC(Flags):
    global flags;
    Flags[0] = Flags[0] & 0b11111110;

# Set Carry flag (0x38)
def SEC(Flags):
    global flags;
    Flags[0] = Flags[0] | 0b00000001;

# Clear Interrupt flag (0x58)
def CLI(Flags):
    global flags;
    Flags[0] = Flags[0] & 0b11111011;

# Set Interrupt flag (0x78)
def SEI(Flags):
    global flags;
    Flags[0] = Flags[0] | 0b00000100;

# Transfer register Y to Accumulator (0x98)
def TYA(A):
    global a;
    A[0] = y[0];
    a = A;

# Clear Overflow flag (0xB8)
def CLV(Flags):
    global flags;
    Flags[0] = Flags[0] & 0b10111111;
    flags = Flags

# Clear Decimal flag (0xD8)
def CLD(Flags):
    global flags;
    Flags[0] = flags[0] & 0b11110111;
    flags = Flags

# No Operation (0xEA)
def NOP():
    pass;
