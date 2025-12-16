import instructions

def main():
    # Registers and memory
    a = bytearray(1);
    x = bytearray(1);
    y = bytearray(1);
    pc: int = 0; 
    sp = bytearray(1);
    flags = bytearray(1);
    addr = bytearray(2);
    mem = bytearray(0x10000);

    mem[0x0000] = 0xA9;
    mem[0x0001] = 0x42;
    mem[0x0002] = 0x09;
    mem[0x0003] = 0x41;

    opcode: bin = mem[pc];
    print(opcode)
    lownibble = opcode >> 4;
    highnibble = opcode & 0x0F;

    if lownibble == 8:
        print("SB1 logic");
    elif lownibble == 0xA and highnibble == 7:
        print("SB2 logic");
    else:
        aaa: hex = (opcode & 0xE0) >> 5;
        bbb: hex = (opcode & 0x1C) >> 2;
        cc: hex = opcode & 0x03;
    
    # Group one instructions
    if cc == 0b01:
        if aaa == 0b000:
            ORA(mem[pc+1]);
        elif aaa == 0b001:
            AND(mem[pc+1]);
        elif aaa == 0b010:
            EOR(mem[pc+1]);
        elif aaa == 0b011:
            ADC(mem[pc+1]);
        elif aaa == 0b100:
            STA(mem[pc+1]);
        elif aaa == 0b110:
            LDA(mem[pc+1]);
        elif aaa == 0b111:
            CMP(mem[pc+1]);

    # Group two instructions
    elif cc == 0b10:
        print("Group 2 instructions have not been implemented yet.")
    
    # Group three and conditional branching instructions
    elif cc == 0b11:
        # Conditional branching instructions
        if bbb == 0b100:
            print("CB");
        # Group three instructions
        elif bbb == 0b000 and not aaa & 0b100:
            print("G3");
    
    pc+=2;
    
    print(f"A: {a[0]}\nX: {x[0]}\nY: {y[0]}\nProgram Counter: {pc}\nStack Pointer: {sp[0]}\nCPU flags: {bin(flags[0])}\nAddress bus: {addr[0]}{addr[1]}");

if __name__ == "__main__":
    main()
