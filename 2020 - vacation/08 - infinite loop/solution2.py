import fileinput

import simulator


# load code
memory = []
for line in fileinput.input():
    line = line.strip()
    instruction, operand = line.split()
    memory.append(simulator.MemoryPos(instruction, int(operand)))
    
# patch code and reexecute
for pos in memory:
    if pos.instruction != "jmp":
       continue

    pos.instruction = "nop"   

    success = False
    cpu = simulator.Simulator(memory)
    try:
        cpu.execute()
        success = True
        break
    except simulator.InfiniteLoop as err:
        pass

    pos.instruction = "jmp"

if success:
    print(f"acc = {cpu.accumulator}")
else:
    print("didn't find a solution")
