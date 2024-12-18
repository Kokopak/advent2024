with open("input.txt") as f:
    registers = {}
    lines = iter(f.readlines())

    a_str = int(next(lines).split(": ")[1])
    b_str = int(next(lines).split(": ")[1])
    c_str = int(next(lines).split(": ")[1])

    registers = {"A": a_str, "B": b_str, "C": c_str}

    next(lines)

    program = list(map(int, next(lines).split(": ")[1].split(",")))


def combo(registers, operand):
    if operand in (0, 1, 2, 3):
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]

    return None


def instruction(registers, opcode, operand, output, instruction_pointer):
    if opcode == 0:
        registers["A"] = registers["A"] // (2 ** (combo(registers, operand)))
    elif opcode == 1:
        registers["B"] = registers["B"] ^ operand
    elif opcode == 2:
        registers["B"] = combo(registers, operand) % 8
    elif opcode == 3:
        if registers["A"] != 0:
            return (operand, output)
    elif opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    elif opcode == 5:
        output.append(combo(registers, operand) % 8)
    elif opcode == 6:
        registers["B"] = registers["A"] // (2 ** (combo(registers, operand)))
    elif opcode == 7:
        registers["C"] = registers["A"] // (2 ** (combo(registers, operand)))

    return (instruction_pointer, output)


def run_program(program, registers):
    instruction_pointer = 0
    output = []

    while instruction_pointer != len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        old_instruction_pointer = instruction_pointer

        instruction_pointer, output = instruction(
            registers, opcode, operand, output, instruction_pointer
        )

        if old_instruction_pointer == instruction_pointer:
            instruction_pointer += 2

    return output


def to_3_bits(number):
    return format(number, "#05b").split("b")[1]


def find(program, index, cursor, candidate, min_value):
    if index >= len(program):
        return int("".join(candidate), 2)

    for i in range(8):
        new_candidate = candidate + to_3_bits(i)

        registers = {"A": int(new_candidate, 2), "B": 0, "C": 0}

        output = run_program(program, registers)

        if not abs(cursor) > len(output) and program[cursor] == output[cursor]:
            value = find(program, index + 1, cursor - 1, new_candidate, min_value)

            if value < min_value:
                min_value = value
                break

    return min_value


print(",".join(map(str, run_program(program, registers))))
print(find(program, 0, -1, "", 999999999999999999))
