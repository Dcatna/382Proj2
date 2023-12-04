#Dominic Catena
# I Pledge My Honor That I Have Abided By The Stevens Honor System
import os

def convertInstruction(instructionName, imm_reg2, reg1, targetreg, alusrc):
    #machinecode = '000000000000000' 15 bits op|immediate/reg2|reg1|targetreg|alusrc
    opcodes = {'ADD' : '00', 'SUB' : '01', 'LOAD' : '10', 'STORE' : '11'}
    return opcodes[instructionName] + imm_reg2 + reg1 + targetreg + alusrc
   

if(__name__ == "__main__"):
    if(os.path.exists("inputfile")): #remove files if the already exist
        os.remove("inputfile")
    if(os.path.exists("datafile")):
        os.remove('datafile')

   
    program = open('program.txt', 'r').readlines()
    instructionfile=open("inputfile", 'w') #write to the instruction mem file
    
    instructionfile.write("v3.0 hex words addressed\n") #have to write the header

    baseaddress = 0000 #line starts here in the instruction file, each line has 16 spots(0-15), next address is 0010
   # print(program)
    instlist = []
    for line in program:
    # Skip empty lines or lines with only a newline character
        if(line.strip() == ""):
            continue

        # Remove comments and any leading/trailing whitespace
        line_content = line.split("//")[0].strip()

        # Only add non-empty content to the list
        if line_content:
            instlist.append(line_content)

    print(instlist)
     
        

















