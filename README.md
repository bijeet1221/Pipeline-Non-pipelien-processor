Part 1: Non-pipelined processor
We have written a python code that calculates factorial of n numbers, calculates the n th
Fibonacci number and performs sorting of n numbers.
Below is a brief explanation of different parts of the code:
Utility functions:
We have made a function called B_D which converts an unsigned binary string to its decimal
equivalent. The function binaryToDecimal uses the above function B_D to convert any signed
binary string to its decimal equivalent.
Main functions:
Decode: This function is used to perform the instruction decode phase of the processor. The
instruction is decoded by taking the opcode (first 6 bits of the binary instruction) and
checking its value. For all R type instructions opcode is “000000” so we need to check the
function code which is present in the last 6 bits of the instruction. After decoding the
instruction, we return a list which stores the instruction name and the values of registers
required for that instruction.ALU: This function is used to perform the execute phase of the processor. It takes the list
returned from the decode phase and performs the necessary calculations and returns the
required result.
Memory: This function is used to perform the Memory phase of the processor. It takes the list
returned from the decode phase and the result from the execute phase. Then this function
returns ‘skip’, i.e., no memory access is required for all instructions except load and store
instructions, for which it accesses the memory and loads/stores data as per the instruction.
Writeback: This function is used to perform the Writeback phase of the processor. It takes 2
inputs, the list of the decode phase and if the Memory function returned ‘skip’, the second
input is the result of the ALU or else it is the value returned from the memory function.
Running the code: We have initialized a data memory of 1000 locations as a dictionary with
each location having a value 0. Next, we have taken the input required. A dictionary is created
which stores the registers and their values. We have an input string which represents the
program to be run. Finally, the code runs in the while loop which fetches each instruction
(Instruction Fetch phase) and performs the 4 other phases using the functions described
above. The clock value and the values of the data memory at the end of execution are then
printed.
Part 2: Pipelined processor
We have written a python code that calculates factorial of n numbers and calculates the n th
Fibonacci number.
Below is a brief explanation of different parts of the code:
Utility functions:
We have made a function called B_D which converts an unsigned binary string to its decimal
equivalent. The function binaryToDecimal uses the above function B_D to convert any signed
binary string to its decimal equivalent.
Main functions:
Decode: This function is used to perform the instruction decode phase of the processor. The
instruction is decoded by taking the opcode (first 6 bits of the binary instruction) and
checking its value. For all R type instructions opcode is “000000” so we need to check the
function code which is present in the last 6 bits of the instruction. After decoding the
instruction, we return a list which stores the instruction name and the values of registers
required for that instruction.
ALU: This function is used to perform the execute phase of the processor. It takes the list
returned from the decode phase and performs the necessary calculations and returns the
required result.Memory: This function is used to perform the Memory phase of the processor. It takes the list
returned from the decode phase and the result from the execute phase. Then this function
returns ‘skip’, i.e., no memory access is required for all instructions except load and store
instructions, for which it accesses the memory and loads/stores data as per the instruction.
Writeback: This function is used to perform the Writeback phase of the processor. It takes 2
inputs, the list of the decode phase and if the Memory function returned ‘skip’, the second
input is the result of the ALU or else it is the value returned from the memory function.
Running the code: We have initialized a data memory of 1000 locations as a dictionary with
each location having a value 0. Next, we have taken the input required. A dictionary is created
which stores the registers and their values. We have an input string which represents the
program to be run. Finally, the code runs in the while loop which fetches each instruction
(Instruction Fetch phase) and performs the 4 other phases using the functions described
above. The clock value and the values of the data memory at the end of execution are then
printed.
Dependencies: Dependencies are found by using the function DependencyFinder which
checks whether the destination of the previous instruction is being used as a source in the
next 2 instructions.
Pipelining Logic: To implement pipeline concept, we have used four pipeline regist3rs to
store the individual stage wise data. Like the fetch information is stored in the pipeline
register IF_ID, decode information in ID_EX, ALU information in EX_M and memory
information in M_WB pipeline registers.
In each clock of the cycle, all the five stages fetch, decode, ALU, memory and writeback
happens for different instructions simultaneously.
The pipeline registers are designed in such a way that for each instruction if one the stage
information is not passed into the corresponding pipeline register then the whole
operation stops.
Handling hazards: To handle control hazards, whenever the bne/beq is executed, the
ongoing pipeline is flushed by popping the elements from pipeline registers. The instructions
above the bne/beq are executed irrespective of the flush.
To handle data hazards, we have used stalls to maintain the uniform functioning of the
pipeline.
The stalls are implemented based on the dependencies found by the dependencies finder
function which provides a list of instructions which have data hazards.
Whenever there is an instruction which is present in the list, the fetch and decode are
stopped and this results to stopping of other instructions. It continues after a stall of 3 clock
cycles ensuring there is writeback of the registers.
We have assumed that the writeback and read cannot happen in the same clock cycle.
