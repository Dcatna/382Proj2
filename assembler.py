#Dominic Catena
# I Pledge My Honor That I Have Abided By The Stevens Honor System
import os

def createInstructions(splitinst):
    instructionlist = []
    for inst in splitinst:
        
        if(inst[0] == 'ADD'):
            if(inst[3][0].isdigit()): #imm or reg check if the first letter is a reg (L)
                imm = inst[3]
                alusrc = 0
            else:
                imm = inst[3][1:]
                alusrc = 1
            
            imm = bin(int(imm))[2:].zfill(8) #padding to 8 bits
            sourcereg = inst[2][1:]
            sourcereg = bin(int(sourcereg))[2:].zfill(2)
            targetreg = inst[1][1:]
            targetreg = bin(int(targetreg))[2:].zfill(3)
            instructionlist.append('00' + str(imm) + str(sourcereg) + str(targetreg) + str(alusrc))
        
        elif(inst[0] == 'SUB'):
            if(inst[3][0].isdigit()): #imm or reg 
                imm = inst[3]
                alusrc = 0
            else:
                imm = inst[3][1:]
                alusrc = 1
            imm = bin(int(imm))[2:].zfill(8) #padding to 8 bits
            sourcereg = inst[2][1:]
            sourcereg = bin(int(sourcereg))[2:].zfill(2)
            targetreg = inst[1][1:]
            targetreg = bin(int(targetreg))[2:].zfill(3)
            instructionlist.append('01' + str(imm) + str(sourcereg) + str(targetreg) + str(alusrc))
        
        elif(inst[0] == 'LOAD'): #takes 3 cycles and three different instrcutjons
            instruction1 = '00' + bin(int(inst[1][1:]))[2:].zfill(8) + '001010'#point
            instruction2 = '00' + bin(int(inst[1][1:]))[2:].zfill(8) + '001000'#fetch
            targetreg = inst[1][1:]
            targetreg = bin(int(targetreg))[2:].zfill(3)
            instruction3 = '100000000000' + str(targetreg) + '0' #load
            instructionlist.append([instruction1, instruction2, instruction3])
            
        elif(inst[0] == 'STORE'): # takes 2 cycles and 2 instrucitons 
            sourcereg = inst[1][1:]
            sourcereg = bin(int(sourcereg))[2:].zfill(2)
            instruction1 = '00' + bin(int(inst[2]))[2:].zfill(8) + '001010'
            instruction2 = '1100000000' + str(sourcereg) + '0000'
            instructionlist.append([instruction1, instruction2])
    return instructionlist

if(__name__ == "__main__"):
    if(os.path.exists("inputfile.txt")): #remove files if the already exist
        os.remove("inputfile.txt")
    if(os.path.exists("datafile.txt")):
        os.remove('datafile.txt')

   
    program = open('program.txt', 'r').readlines()
    instructionfile=open("inputfile.txt", 'w') # write to the instruction mem file
    
    instructionfile.write("v3.0 hex words addressed\n") #have to write the header

    baseaddress = 0000 #line starts here in the instruction file, each line has 16 spots(0-15), next address is 0010
   # print(program)
    instlist = []
    for line in program: # putting all instructions ina list
    
        if(line.strip() == ""):# skip empty lines
            continue
        line_content = line.split("//")[0].strip()#remove comments and any whitespace

        if line_content: # only addcontent to the list
            instlist.append(line_content)

    #print(instlist)

    splitinsts = []
    for inst in instlist: #seperates each isntructions into its individual parts
        inst = inst.split()
        splitinsts.append(inst)

    #print(splitinsts)
    instructions = createInstructions(splitinsts)
    #print(instructions)
    i = 0
    instructionfile.write(str(baseaddress).zfill(4) + ": ")
    for instruction in instructions:
        if(i == 16):
            instructionfile.write("\n" + str(baseaddress + 10).zfill(4) + ": ")
        elif(type(instruction) == list):
            for x in instruction:
                print(hex(int(x, 2))[2:].zfill(4), x)
                instructionfile.write(hex(int(x, 2))[2:].zfill(4) + " ")
                i+=1
        else:
            print(hex(int(instruction, 2))[2:].zfill(4), instruction)
            instructionfile.write(hex(int(instruction, 2))[2:].zfill(4) + " ")
            i+=1
    print(hex(int(instructions[0][0]))[2:].zfill(4))
    print(str(baseaddress + 10).zfill(4))
    
