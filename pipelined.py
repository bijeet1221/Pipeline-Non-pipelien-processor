
def B_D(n):  # binary to decimal for unsigned
    return int(n,2)

def binaryToDecimal(binary):  # binary to deciamal for signed
    if(binary[0]=='0'):
        return B_D(binary)
    ans=''
    for i in binary:
        if(i=='0'):
            ans+='1'
        else:
            ans+='0'
    ones_complement=ans[1:]
    twos_complement = bin(int(ones_complement, 2) + int('1', 2))
    twos_complement=twos_complement.replace('b','')
    twos_complement=B_D(twos_complement)
    if(binary[0]=='1'):
        twos_complement=twos_complement*-1
    return twos_complement

def Fetch(i):
    return instructions[i]




# DECODE CYCLE FUNCTION
def Decode(instruction):
    opcode=instruction[0:6]
    if(opcode=='000000'):
        rs=instruction[6:11]
        rt=instruction[11:16]
        rd=instruction[16:21]
        shamt=instruction[21:26]
        fn=instruction[26:32]
        if(fn=='100000'): #add
            l=['add',values[rs],values[rt],rd]
            return l
        elif(fn=='100010'): #sub
            l=['sub',values[rs],values[rt],rd]
            return l
        elif(fn=='000000'):  # sll 
            l=['sll',values[rt],binaryToDecimal(shamt),rd]
            return l
        elif(fn=='101010'): #slt
            l=['slt',values[rs],values[rt],rd]
            return l
       
    elif(opcode=='011100'): #mul
        rs=instruction[6:11]
        rt=instruction[11:16]
        rd=instruction[16:21]
        shamt=instruction[21:26]
        fn=instruction[26:32]
        l=['mul',values[rs],values[rt],rd]
        return l     
                
    elif(opcode=='100011'): #lw
        rs=instruction[6:11]
        rt=instruction[11:16]
        immediate=instruction[16:32]
        l=['lw',values[rs],binaryToDecimal(immediate),rt]
        return l
    
    elif(opcode=='101011'): #sw
        rt=instruction[6:11]
        rs=instruction[11:16]
        immediate=instruction[16:32]
        l=['sw',values[rs],values[rt],binaryToDecimal(immediate)]
        return l
    
    elif(opcode=='001000'): #addi
        rs=instruction[11:16]
        rt=instruction[6:11]
        immediate=instruction[16:32]
        l=['addi',values[rt],binaryToDecimal(immediate),rs]
        return l
    
    elif(opcode=='000101'): #bne
        rs=instruction[6:11]
        rt=instruction[11:16]
        immediate=instruction[16:32]
        l=['bne',values[rs],values[rt],binaryToDecimal(immediate)]
        return l
    
    elif(opcode=='000100'): #beq
        rs=instruction[6:11]
        rt=instruction[11:16]
        immediate=instruction[16:32]
        l=['beq',values[rs],values[rt],binaryToDecimal(immediate)]
        return l
        
# ALU CYCLE FUNCTION    
def ALU(list_values):
    if(list_values[0]=='add'):
        val=list_values[1]+list_values[2]
        return val
    elif(list_values[0]=='sub'):
        val=list_values[1]-list_values[2]
        return val
    elif(list_values[0]=='sll'):
        val=list_values[1]<<list_values[2]
        return val
    elif(list_values[0]=='mul'):
        val=list_values[1]*list_values[2]
        return val
    elif(list_values[0]=='lw'):
        val=list_values[1]+list_values[2]
        return val
    elif(list_values[0]=='sw'):
        val=list_values[2]+list_values[3]
        return val
    elif(list_values[0]=='addi'):
        val=list_values[1]+list_values[2]
        return val
    elif(list_values[0]=='bne'):
        if(list_values[1]!=list_values[2]):
            return True
        else:
            return False
    elif(list_values[0]=='beq'):
        if(list_values[1]==list_values[2]):
            return True
        else:
            return False
    elif(list_values[0]=='slt'):
        if(list_values[1]<list_values[2]):
            return 1
        else:
            return 0
        
# MEMORY CYCLE FUNCTION
def Memory(list_values,result):
    if(list_values[0]=='add' or list_values[0]=='sub' or list_values[0]=='sll' or list_values[0]=='mul' or list_values[0]=='addi' or list_values[0]=='bne' or list_values[0]=='beq' or list_values[0]=='beq' or list_values[0]=='slt'):
        return 'skip'         # Skip to handle instructions where memory is not used
    elif(list_values[0]=='lw'):
        return data_memory[result]
    elif(list_values[0]=='sw'):
        data_memory[result]=list_values[1]
        return 1
        
                
def WriteBack(list_values,val):
    if(list_values[0]=='add'):
        values[list_values[3]]=val
    elif(list_values[0]=='sub'):
        values[list_values[3]]=val
    elif(list_values[0]=='sll'):
        values[list_values[3]]=val
    elif(list_values[0]=='lw'):
        values[list_values[3]]=val
    elif(list_values[0]=='addi'):
        values[list_values[3]]=val
    elif(list_values[0]=='mul'):
        values[list_values[3]]=val
    elif(list_values[0]=='slt'):
        values[list_values[3]]=val
             
 

# Data memory
key_mem=[x for x in range(0,100)]
data_memory={y:0 for y in key_mem}     

# # Input format
print("Enter an integer")
n=int(input())
print("Enter input memory address")
base_add=int(input())
print("Enter output memory address")
out_add=int(input())

    
# register values
values={'10000':0,'10001':0,'10010':0,'10011':0,'10100':0,'10101':0,'10110':0,'10111':0,'01000':0,'01001':0,'01010':0,'01011':0,'01100':0,'01101':0,'01110':0,'01111':0,'11000':0,'11001':0,'00100':0,'00101':0,'00110':0,'00111':0,'00000':0,'00001':0}
values['01100']=n   # t4 contains input
data_memory[base_add]=n

# Pipeline Registors
IF_ID=[]
ID_EX=[]
EX_M=[]
M_W=[]



# Code for factorial
input='''00100000000011010000000000000001
01110001101011000110100000000010
00100001100011001111111111111111
00100001111011110000000000000000
00100000000000010000000000000001
01110011000000011100000000000010
00000000000010101100100000000000
00010101100000001111111111111001'''


#dependency finder
def Dependency_finder(instruction):
    opcode=instruction[0:6]
    if(opcode=='000000'):
        rs=instruction[6:11]
        rt=instruction[11:16]
        rd=instruction[16:21]
        shamt=instruction[21:26]
        fn=instruction[26:32]
        if(fn=='100000'): 
            l=['add',rs,rt,rd]
            return l
        elif(fn=='100010'): 
            l=['sub',rs,rt,rd]
            return l
        elif(fn=='000000'):  
            l=['sll',rt,binaryToDecimal(shamt),rd]
            return l
        elif(fn=='101010'): 
            l=['slt',rs,rt,rd]
            return l
       
    elif(opcode=='011100'): 
        rs=instruction[6:11]
        rt=instruction[11:16]
        rd=instruction[16:21]
        shamt=instruction[21:26]
        fn=instruction[26:32]
        l=['mul',rs,rt,rd]
        return l     
                
    elif(opcode=='100011'): 
        rs=instruction[6:11]
        rt=instruction[11:16]
        immediate=instruction[16:32]
        l=['lw',rs,binaryToDecimal(immediate),rt]
        return l
    
    elif(opcode=='101011'): 
        rt=instruction[6:11]
        rs=instruction[11:16]
        immediate=instruction[16:32]
        l=['sw',rs,values[rt],binaryToDecimal(immediate)]
        return l
    
    elif(opcode=='001000'): 
        rs=instruction[11:16]
        rt=instruction[6:11]
        immediate=instruction[16:32]
        l=['addi',values[rt],binaryToDecimal(immediate),rs]
        return l
    
    elif(opcode=='000101'): 
        rs=instruction[6:11]
        rt=instruction[11:16]
        immediate=instruction[16:32]
        l=['bne',rs,rt,binaryToDecimal(immediate)]
        return l
    
    elif(opcode=='000100'): 
        rs=instruction[6:11]
        rt=instruction[11:16]
        immediate=instruction[16:32]
        l=['beq',rs,rt,binaryToDecimal(immediate)]
        return l

dependencies=[]
instructions=input.split()
length=len(instructions)
i=0
dep=[]
DC=[]
while(i<length):
    str=instructions[i]  
    x=Dependency_finder(str)
    DC.append(Dependency_finder(str))   
    result=ALU(DC)   
    i=i+1
i=0
while(i<length-1):
    if(i<length-2 ):
        if(DC[i][3]==DC[i+1][1] or DC[i][3]==DC[i+1][2]):
            if(i+1 not in dep):
                dep.append(i+1)
            dependencies.append([DC[i][3],i+1])
        if(DC[i][3]==DC[i+2][1] or DC[i][3]==DC[i+2][2]):
            if(i+2 not in dep):
                dep.append(i+2)
            dependencies.append([DC[i][3],i+2])
    else:
        if(DC[i][3]==DC[i+1][1] or DC[i][3]==DC[i+1][2]):
            dependencies.append([DC[i][3],i+1])
            if(i+1 not in dep):
                dep.append(i+1)
    i=i+1


print(f'dependencies at instrustion number= {dep}')
l=[]
for elem in dep:
    if elem not in l:
        l.append(elem)
        l.append(elem)
        l.append(elem)

instructions=input.split()   # splitting the instruction to remove backslash n characters
length=len(instructions)
i=0 
clock=0  # clock
while(i<length+5):
    flag=1  # flag is used to apply stalls
    
    # initialising all are None so that when an instruction is fetched then only the next stages are implemented
    ins = None
    DC = None
    res = None
    mem = None
    
    # Fetch
    if(i<length):
        if(i in l):
            l.pop(0)
            flag=0
        else:
            ins=Fetch(i)
     
    # Decode      
    if(len(IF_ID) != 0):
        DC=Decode(IF_ID[0])
        IF_ID.pop(0)
        
    # ALU and handling branch operations
    if(len(ID_EX) != 0): 
        res=ALU(ID_EX[0])
        if((ID_EX[0][0]=='bne' or ID_EX[0][0]=='beq') and res==True):
            i=i+ID_EX[0][3] - 2
            if (len(IF_ID) != 0):
                IF_ID.pop(0)
        
    # Memory
    if(len(EX_M) != 0):
        mem=Memory(EX_M[0][0],EX_M[0][1])
        mem_val=[EX_M[0][0],EX_M[0][1],mem]
      
    # Writeback  
    if(len(M_W) != 0 ): 
        if(M_W[0][2]!='skip'):
            WriteBack(M_W[0][0],M_W[0][2])      
        else:
            WriteBack(M_W[0][0],M_W[0][1])
        M_W.pop(0)
    
    # Clock increments after each cycle
    clock=clock+1
   
    # Implementing pipeline registors. There are four pipeline registors IF_ID,ID_EX,EX_M,M_W
    if(ins!=None):
        IF_ID.append(ins)
    if(DC!=None):
        ID_EX.append(DC)
    if(res!=None):
        EX_M.append([ID_EX[0],res])
        ID_EX.pop(0)
    if(mem!=None):
        M_W.append(mem_val)
        EX_M.pop(0)
    
    # next iteration of cycle
    if(flag==1):
        i=i+1
 
# Final data memory and clock   
data_memory[out_add]=values['01101']
print(values)
print(data_memory)
print("Clock=",clock)
    
