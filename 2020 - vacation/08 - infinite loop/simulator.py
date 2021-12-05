class InfiniteLoop(Exception):
    def __init__(self):
        super().__init__("infinite loop!")


class MemoryPos:
    def __init__(self, instruction, operand):
        self.instruction = instruction
        self.operand = operand
        self.visited = False
   

class Simulator:
    def __init__(self, mem):
        for pos in mem:
            pos.visited = False

        self._mem = mem
        self._ip = 0
        self._acc = 0

    def execute(self) -> None:
        while True:
            if not self._do_cycle():
                return

    def _do_cycle(self) -> bool:
        if self._ip >= len(self._mem):
            return False
    
        pos = self._mem[self._ip]
        if pos.visited:
            raise InfiniteLoop()
    
        pos.visited = True
    
        if pos.instruction == "nop":
            self._ip += 1
        elif pos.instruction == "acc":
            self._ip += 1
            self._acc += pos.operand
        elif pos.instruction == "jmp":
            self._ip += pos.operand

        return True

    @property
    def accumulator(self) -> int:
        return self._acc
