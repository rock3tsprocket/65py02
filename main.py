from instructions import *

def main():
    # Registers and memory
    a = bytearray(1);
    x = bytearray(1);
    y = bytearray(1);
    pc = 0; 
    sp = bytearray(1);
    flags = bytearray(1);
    addr = bytearray(2);
    mem = bytearray(0x10000);

    mem[0x0000] = 0xA9;
    mem[0x0001] = 0x42;
    mem[0x0002] = 0x09;
    mem[0x0003] = 0x41;

    # Declaring bits of the opcode
    aaa = None;
    bbb = None;
    cc = None;

    finishrun = False
    while True:
        opcode = mem[pc];
        print(hex(opcode), hex(pc))
        lownibble = opcode >> 4;
        highnibble = opcode & 0x0F;

        if lownibble == 8:
            print("SB1 logic");
        elif lownibble == 0xA and highnibble > 9:
            print("SB2 logic");
        else:
            aaa = (opcode & 0xE0) >> 5;
            bbb = (opcode & 0x1C) >> 2;
            cc = opcode & 0x03;
    
        # Group one instructions
        if cc == 0b01:
            if aaa == 0b000:
                print("dee")
                ORA(mem[pc+1], bbb, a);
                pc+=2;
            elif aaa == 0b001:
                AND(mem[pc+1], bbb, a);
                pc+=2;
            elif aaa == 0b010:
                EOR(mem[pc+1], bbb, a);
                pc+=2;
            elif aaa == 0b011:
                ADC(mem[pc+1], bbb, a, flags);
                pc+=2;
            elif aaa == 0b100:
                STA(mem[pc+1], bbb, a);
                pc+=2;
            elif aaa == 0b101:
                LDA(mem[pc+1], bbb, a);
                pc+=2;
            elif aaa == 0b110:
                CMP(mem[pc+1], bbb, a, flags);
                pc+=2;
            elif aaa == 0b111:
                SBC(mem[pc+1], bbb, a, flags);
                pc+=2;
    
        # Group two instructions
        elif cc == 0b10:
            if aaa == 0b000:
                ASL(mem[pc+1], bbb, a, flags);
                pc+=2;
        
        # Group three and conditional branching instructions
        elif cc == 0b11:
            # Conditional branching instructions
            if bbb == 0b100:
                if aaa == 0b000:
                    pass; # implemented in CLI thingy

            # Group three instructions
            elif bbb == 0b000 and not aaa & 0b100:
                print("Group three instructions are not implemented");
        

        while True:
            if finishrun:
                if opcode == 0:
                    print("Break encountered");
                    exit();
                #pc = pc+1 if lownibble == 8 or (lownibble == 0xA and highnibble > 9) else pc+2
                break;
            
            if opcode == 0: # BRK
                print("Break encountered\n");
            
            try:
                whattodo = input("What do you want to do? (type 'help' for help)\n> ");
            except (KeyboardInterrupt, EOFError):
                print("\nInterrupted");
                exit();

            if whattodo == "help":
                print("'help': Show this list\n"
                      "'registers': Dump register contents\n"
                      "'memory': Dump memory\n"
                      "'step': Advance by one instruction\n"
                      "'run': Run the program until it reaches a break opcode\n"
                      "'reset': Reset registers\n"
                      "'opcode': Print opcode to be executed\n"
                      "'exit': Exit");
            elif whattodo == "registers":
                print(f"A: {hex(a[0])}\n"
                      f"X: {hex(x[0])}\n"
                      f"Y: {hex(y[0])}\n"
                      f"Program Counter: {hex(pc)}\n"
                      f"Stack Pointer: {hex(sp[0])}\n"
                      f"CPU flags: {format(flags[0], '#010b')}\n");
            elif whattodo == "memory":
                for i in range(0x0, 0x1000):
                    if str(hex(i))[-1] == "0":
                        print(f"\n {hex(i)}: ", end="");
                        continue;
                    print(f"{hex(mem[i])[2:4]} ", end=" ");
                print("")
            elif whattodo == "step":
                #pc = pc+1 if lownibble == 8 or (lownibble == 0xA and highnibble > 9) else pc+2;
                break;
            elif whattodo == "reset":
                a[0]     = 0;
                x[0]     = 0;
                y[0]     = 0;
                pc       = 0;
                sp[0]    = 0;
                flags[0] = 0;
            elif whattodo == "run":
                finishrun = True;
            elif whattodo == "exit":
                exit();
            else: 
                print("Invalid option");
                continue;
            

if __name__ == "__main__":
    main()
