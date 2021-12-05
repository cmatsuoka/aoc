import fileinput
import re
from typing import Literal, Optional

from pydantic import BaseModel, validator


class Passport(BaseModel):
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: Literal["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid: str
    cid: Optional[str]

    class Config:
        extra = "forbid"

    @validator("byr")
    def validate_byr(cls, v):
        val = int(v)
        assert val >= 1920 and val <= 2002
        return v

    @validator("iyr")
    def validate_iyr(cls, v):
        val = int(v)
        assert val >= 2010 and val <= 2020
        return v

    @validator("eyr")
    def validate_eyr(cls, v):
        val = int(v)
        assert val >= 2020 and val <= 2030
        return v

    @validator("hgt")
    def validate_hgt(cls, v):
        m = re.match(r"([0-9]+)(cm|in)", v)
        assert m is not None
        height = int(m.group(1))
        unit = m.group(2)
        if unit == "cm":
            assert height >= 150 and height <= 193
        elif unit == "in":
            assert height >= 59 and height <= 76
        return v

    @validator("hcl")
    def validate_hcl(cls, v):
        assert re.match(r"#[0-9a-f]{6}$", v)
        return v

    @validator("pid")
    def validate_pid(cls, v):
        assert re.match(r"[0-9]{9}$", v)
        return v


num_valid = 0

# read input file
data = {}
for line in fileinput.input():
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

print(num_valid)
