import fileinput

import simulator


def solve(input_file):
    # load code
    memory = []
    for line in input_file:
        line = line.strip()
        instruction, operand = line.split()
        memory.append(simulator.MemoryPos(instruction, int(operand)))

    cpu = simulator.Simulator(memory)

    try:
        cpu.execute()
    except simulator.InfiniteLoop as err:
        print(err)

    return cpu.accumulator


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))
