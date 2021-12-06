import fileinput

import simulator


def solve(input_file):
    # load code
    memory = []
    for line in input_file:
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
            return cpu.accumulator
        except simulator.InfiniteLoop as err:
            pass

        pos.instruction = "jmp"

    return None


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))
