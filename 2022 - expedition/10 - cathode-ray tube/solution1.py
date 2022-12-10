import fileinput


def solve(input_file):
    tick = 0
    ins_cycles = 0
    ins = ""  # instruction
    ops = []  # operands
    reg_x = 1
    signal_strength = 0

    while True:
        if (tick + 20) % 40 == 0:
            signal_strength += tick * reg_x

        if ins_cycles == 0:
            if ins == "addx":
                reg_x += int(ops[0])

            # fetch new instruction
            line = input_file.readline().strip()
            if not line:
                break

            (ins, *ops) = line.split(" ")
            ins_cycles = 2 if ins == "addx" else 1

        ins_cycles -= 1
        tick += 1

    return signal_strength


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))
