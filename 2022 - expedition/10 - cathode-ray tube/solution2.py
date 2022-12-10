import fileinput


def solve(input_file):
    ins_cycles = 0
    ins = ""  # instruction
    ops = []  # operands
    reg_x = 1
    crt_column = 0
    output = ""

    while True:
        if ins_cycles == 0:
            if ins == "addx":
                reg_x += int(ops[0])

            # fetch new instruction
            line = input_file.readline().strip()
            if not line:
                break

            (ins, *ops) = line.split(" ")
            ins_cycles = 2 if ins == "addx" else 1

        # render row
        output += "#" if crt_column in (reg_x - 1, reg_x, reg_x + 1) else "."

        # update crt sweep
        crt_column += 1
        if crt_column >= 40:
            crt_column = 0
            output += "\n"

        ins_cycles -= 1

    return output


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))
