import fileinput
from typing import Optional

from pydantic import BaseModel


class Passport(BaseModel):
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str]


def solve(input_file):
    num_valid = 0

    # read input file
    data = {}
    for line in input_file:
        line = line.strip()
        if not line:
            try:
                Passport(**data)
                num_valid += 1
            except ValueError:
                pass
            data = {}

        for field in line.split():
            key, val = field.split(":")
            data[key] = val

    try:
        Passport(**data)
        num_valid += 1
    except ValueError:
        pass

    return num_valid


if __name__ == "__main__":
    print(solve(fileinput.FileInput()))
