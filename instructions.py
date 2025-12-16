""" Group one instructions """

# OR Accumulator (AAA = 0b000)
def ORA(num):
    if bbb == 0b000:
        print("WIP (ORA bbb=0)");

    if bbb == 0b010:
        a[0] = a[0] | num;
    elif bbb == 0b011:
        a[0] = a[0] | mem[num];
    elif bbb == 0b100:
        a[0] = a[0] | num;

# AND Accumulator (AAA = 0b001)
def AND(num):
    if bbb == 0b000:
        print("WIP (AND bbb=0)");

    if bbb == 0b010:
        a[0] = (a[0] & num);
    elif bbb == 0b011:
        a[0] = (a[0] & mem[num]);
    elif bbb == 0b100:
        a[0] = a[0] & num;

# EOR/XOR Accumulator (AAA = 0b010)
def EOR(num):
    if bbb == 0b000:
        print("WIP (ORA bbb=0)");

    if bbb == 0b010:
        a[0] = a[0] ^ num;
    elif bbb == 0b011:
        a[0] = a[0] ^ mem[num];
    elif bbb == 0b100:
        a[0] = a[0] ^ num;

# Add With Carry (to accumulator) (AAA = 0b011)
def ADC(num):
    if bbb == 0b000:
        print("WIP (ADC bbb=0)");
    elif bbb == 0b010:
        try:
            a[0] = a[0] + num;
        except ValueError:
            a[0] = (num - 0x1) - 0xFF;
            flags[0] = flags[0] | 0b00000001;
    elif bbb == 0b011:
        try:
            a[0] = a[0] + mem[num];
        except ValueError:
            a[0] = (mem[num] - 0x1) - 0xFF;
            flags[0] = flags[0] | 0b00000001;
    elif bbb == 0b100:
        try:
            a[0] = a[0] + num;
        except ValueError:
            a[0] = (num - 0x1) - 0xFF;
            flags[0] = flags[0] | 0b00000001;

# Store Accumulator (AAA = 0b100)
def STA(num):
    print("Not implemented (STA)")

# Load value to Accumulator (AAA = 0b101)
def LDA(num):
    print("Not implemented (LDA)")

# Compare value to Accumulator (AAA = 0b110)
def CMP(num):
    if bbb == 0b000:
        print("WIP (CMP bbb=0)");
    elif bbb == 0b010:
        if a[0] >= num:
            flags[0] = (flags[0] | 0b00000011) & 0b01111111;
        else:
            pass;
    elif bbb == 0b011:
        if a[0] >= mem[num]:
            flags[0] = (flags[0] | 0b00000011) & 0b01111111;
        else:
            pass;
        elif bbb == 0b100:
            if a[0] >= num:
                flags[0] = (flags[0] | 0b00000011) & 0b01111111;
            else:
                pass;


# Subtract with carry (from accumulator) (AAA = 0b111)
def SBC(num):
    if bbb == 0b000:
        print("WIP (SBC bbb=0)");
    elif bbb == 0b010:
        try:
            a[0] = a[0] - num;
        except ValueError:
            a[0] = 0xFF + a[0] - num;
    elif bbb == 0b011:
        try:
            a[0] = a[0] - mem[num];
        except ValueError:
            a[0] = 0xFF + a[0] - mem[num];
    elif bbb == 0b100:
        try:
            a[0] = a[0] - num;
        except ValueError:
            a[0] = 0xFF + a[0] - num;



""" Some single-byte instructions """
# Break (0x00)
def BRK():
    print("Break encountered.");
    break;

# Clear Carry flag (0x18)
def CLC():
    flags[0] = flags[0] & 0b11111110;

# Set Carry flag (0x38)
def SEC():
    flags[0] = flags[0] | 0b00000001;

# Clear Interrupt flag (0x58)
def CLI():
    flags[0] = flags[0] & 0b11111011;

# Set Interrupt flag (0x78)
def SEI():
    flags[0] = flags[0] | 0b00000100;

# Transfer register Y to Accumulator (0x98)
def TYA():
    a[0] = y[0];

# Clear Overflow flag (0xB8)
def CLV():
    flags[0] = flags[0] & 0b10111111;

# Clear Decimal flag (0xD8)
def CLD():
    flags[0] = flags[0] & 0b11110111;

# No Operation (0xEA)
def NOP():
    pass;
