
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
        l=['addi',rs,values[rt],binaryToDecimal(immediate)]
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
        val=list_values[2]+list_values[3]
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
        values[list_values[1]]=val
    elif(list_values[0]=='mul'):
        values[list_values[3]]=val
    elif(list_values[0]=='slt'):
        values[list_values[3]]=val
             
 



# Data memory
key_mem=[x for x in range(0,1000)]
data_memory={y:0 for y in key_mem}     

# Input format
print("Enter no of integers")
t=int(input())
print("Enter intgers")
l=[]
for i in range(t):
    n=int(input())
    l.append(n)
print("Enter input memory address")
m=int(input())
base_add=m
print("Enter output memory address")
out_add=int(input())
for i in range(len(l)):
    data_memory[m]=l[i]
    m=m+4
    

values={'10000':0,'10001':0,'10010':0,'10011':0,'10100':0,'10101':0,'10110':0,'10111':0,'01000':0,'01001':0,'01010':0,'01011':0,'01100':0,'01101':0,'01110':0,'01111':0,'11000':0,'11001':0,'00100':0,'00101':0,'00110':0,'00111':0,'00000':0,'00001':0}
values['01010']=base_add   # t2 contains input base address
values['01011']=out_add    # t3 contains output base address
values['01001']=t          # t1 contains number of inputs


# Sorting Code
input='''00000000000000001011100000100000 
00000001011000001010100000100000               
00000001010000000111100000100000          
00100001010011000000000110010000          
10001101010110010000000000000000        
10101101100110010000000000000000        
00100001100011000000000000000100          
00100001010010100000000000000100          
00100010111101110000000000000001          
00010110111010011111111111111010         
00000000000000001011100000100000         
00000000000000000110000000100000         
00000001111000000101000000100000         
00100001010011000000000110010000          
00000000000010010010100010000000          
00000000101011000010100000100000          
00010010111010010000000000010100          
00000000000000001011000000100000          
00000000000101101000000010000000          
00000001100100001000000000100000          
00100010000100000000000000001000          
00000000101100000000100000101010 
00010100001000000000000000001011
00100000000000010000000000001000
00000010000000011000000000100010
10001110000011010000000000000000
10001110000011100000000000000100
00000001110011010000100000101010
00010000001000000000000000000010
10101110000011100000000000000000
10101110000011010000000000000100
00100010110101100000000000000001
00000010110010010000100000101010
00010100001000001111111111110000
00100010111101110000000000000001
00000010111010010000100000101010
00010100001000001111111111101011
00000000000000001010000000100000
10001101100100110000000000000000
10101110101100110000000000000000
00100001100011000000000000000100
00100010101101010000000000000100
00100010100101000000000000000001
00010110100010011111111111111010'''


# Code for factorial
# input='''00100000000011100000000000000000
# 00100001010011110000000000000000
# 00100001011110000000000000000000
# 10001101010011000000000000000000
# 00100001110011100000000000000001
# 00100000000011010000000000000001
# 00010001100000000000000000000110
# 01110001101011000110100000000010
# 00100001100011001111111111111111
# 00010101100000001111111111111101
# 10101101011011010000000000000000
# 00100001010010100000000000000100
# 00100001011010110000000000000100
# 00100001100011000000000000000001
# 10101101011011000000000000000000
# 00010101110010011111111111110011
# 00100001111010100000000000000000
# 00100011000010110000000000000000'''


instructions=input.split()
length=len(instructions)
i=0
clock=0
while(i<length):
    str=instructions[i]  #Fetch Cycle
    clock=clock+5
    DC=Decode(str)   #Decode Cycle
    result=ALU(DC)   #ALU Cycle
    if((DC[0]=='bne' or DC[0]=='beq') and result==True):  # handing bne and beq
        i=i+DC[3]
    mem=Memory(DC,result) #Memory Cycle
     #Writeback Cycle
    if(mem!='skip'): 
        WriteBack(DC,mem) 
    else:
        WriteBack(DC,result)  
    i=i+1
    

print(data_memory)
print("Clock=",clock)
    


























