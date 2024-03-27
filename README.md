# Non-pipelined processor

This Python code implements a non-pipelined processor that calculates factorial of n numbers, calculates the n-th Fibonacci number, and performs sorting of n numbers.

## Utility functions
- `B_D`: Converts an unsigned binary string to its decimal equivalent.
- `binaryToDecimal`: Converts any signed binary string to its decimal equivalent.

## Main functions
- `Decode`: Performs the instruction decode phase of the processor. Decodes the instruction by taking the opcode and checking its value.
- `ALU`: Performs the execute phase of the processor. Takes the list returned from the decode phase and performs the necessary calculations.
- `Memory`: Performs the Memory phase of the processor. Accesses memory for load and store instructions, otherwise returns 'skip'.
- `Writeback`: Performs the Writeback phase of the processor. Takes the list of the decode phase and the result from the ALU or memory function.

## Running the code
- Initializes a data memory of 1000 locations as a dictionary with each location having a value 0.
- Takes input required.
- Creates a dictionary which stores the registers and their values.
- Runs the code in a while loop which fetches each instruction and performs the 4 other phases using the functions described above.
- Prints the clock value and the values of the data memory at the end of execution.

# Pipelined processor

This Python code implements a pipelined processor that calculates factorial of n numbers and calculates the n-th Fibonacci number.

## Main functions
- `Decode`: Performs the instruction decode phase of the processor.
- `ALU`: Performs the execute phase of the processor.
- `Memory`: Performs the Memory phase of the processor.
- `Writeback`: Performs the Writeback phase of the processor.

## Running the code
- Initializes a data memory of 1000 locations as a dictionary with each location having a value 0.
- Takes the input required.
- Creates a dictionary which stores the registers and their values.
- Runs the code in a while loop which fetches each instruction and performs the 4 other phases using the functions described above.
- Prints the clock value and the values of the data memory at the end of execution.

## Dependencies
- Found using the function `DependencyFinder` which checks whether the destination of the previous instruction is being used as a source in the next 2 instructions.

## Pipelining Logic
- Uses four pipeline registers to store the individual stage wise data (IF_ID, ID_EX, EX_M, M_WB).
- Executes all five stages (fetch, decode, ALU, memory, writeback) for different instructions simultaneously in each clock cycle.

## Handling hazards
- Control hazards are handled by flushing the ongoing pipeline whenever `bne`/`beq` is executed.
- Data hazards are handled by using stalls to maintain the uniform functioning of the pipeline.

Note: Assumes that the writeback and read cannot happen in the same clock cycle.
