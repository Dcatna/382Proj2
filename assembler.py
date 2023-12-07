#Dominic Catena
# I Pledge My Honor That I Have Abided By The Stevens Honor System
import os

def convertInstruction(instructionName, imm_reg2, reg1, targetreg, alusrc):
    #machinecode = '000000000000000' 15 bits op|immediate/reg2|reg1|targetreg|alusrc
    opcodes = {'ADD' : '00', 'SUB' : '01', 'LOAD' : '10', 'STORE' : '11'}
    return opcodes[instructionName] + imm_reg2 + reg1 + targetreg + alusrc
   

def createInstructions(splitinst):
    for inst in splitinst:
        if(inst[0] == 'ADD'):
            if(imm[1][0].isdigit()): #imm or reg check if the first letter is a reg (L)
                imm = inst[1]
                alusrc = 0
            else:
                imm = inst[1][1:]
                alusrc = 1
            imm = bin(imm).zfill(8) #padding to 8 bits
            sourcereg = inst[2][1:]
            sourcereg = bin(sourcereg).zfill(2)
            targetreg = inst[3][1:]
            targetreg = bin(targetreg).zfill(3)
            return '00' + imm + sourcereg + targetreg + alusrc
        
        elif(inst[0] == 'SUB'):
            if(imm[0].isdigit()): #imm or reg 
                imm = inst[1]
                alusrc = 0
            else:
                imm = inst[1][1:]
                alusrc = 1
            imm = bin(imm).zfill(8) #padding to 8 bits
            sourcereg = inst[2][1:]
            sourcereg = bin(sourcereg).zfill(2)
            targetreg = inst[3][1:]
            targetreg = bin(targetreg).zfill(3)
            return '01' + imm + sourcereg + targetreg + alusrc
        
        elif(inst[0] == 'LOAD'):
            instruction1 = '00' + inst[1] + '001010'
            instruction2 = '00' + inst[1] + '001000'
            targetreg = inst[3][1:]
            targetreg = bin(targetreg).zfill(3)
            instruction3 = '100000000000' + targetreg + '0'
            return [instruction1, instruction2, instruction3]

        elif(inst[0] == 'STORE'):
            sourcereg = inst[1][1:]
            sourcereg = bin(sourcereg).zfill(2)
            instruction1 = '00' + inst[2] + '001010'
            instruction2 = '1100000000' + sourcereg + '0000'
            return [instruction1, instruction2]




if(__name__ == "__main__"):
    if(os.path.exists("inputfile")): #remove files if the already exist
        os.remove("inputfile")
    if(os.path.exists("datafile")):
        os.remove('datafile')

   
    program = open('program.txt', 'r').readlines()
    instructionfile=open("inputfile", 'w') # write to the instruction mem file
    
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

    print(splitinsts)
    createInstructions(splitinsts)
