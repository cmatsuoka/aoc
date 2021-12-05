import fileinput

import simulator


# load code
memory = []
for line in fileinput.input():
    line = line.strip()
    instruction, operand = line.split()
    memory.append(simulator.MemoryPos(instruction, int(operand)))
    
cpu = simulator.Simulator(memory)

try:
    cpu.execute()
except simulator.InfiniteLoop as err:
    print(err)
    
print(f"acc = {cpu.accumulator}")
