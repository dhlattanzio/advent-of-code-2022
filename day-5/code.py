import re
import copy

data = open("input.txt").read()

# Data parsing
index_proc = data.index("\n\n");
stacks_draw = data[:index_proc].splitlines()

stacks = {}
for stack in stacks_draw:
	index = stack.find("[")
	while index != -1:
		number = index // 4
		letter = stack[index + 1]
		stacks[number] = stacks.get(number, [])
		stacks[number].append(letter)

		index = stack.find("[", index + 1)

procedures = [[int(y) for y in re.sub("[a-z]", "", x).strip().split("  ")] \
				for x in data[(index_proc + 2):].splitlines()]

# Day One
stacks_copy = copy.deepcopy(stacks)
for procedure in procedures:
	for i in range(procedure[0]):
		letter = stacks_copy[procedure[1] - 1].pop(0)
		stacks_copy[procedure[2] - 1].insert(0, letter)

result = ""
for x in range(len(stacks_copy)):
	result += stacks_copy[x][0]
print(f"Part One: {result}")

# Day Two
stacks_copy = copy.deepcopy(stacks)
for procedure in procedures:
	for i in range(procedure[0]):
		letter = stacks_copy[procedure[1] - 1].pop(0)
		stacks_copy[procedure[2] - 1].insert(i, letter)

result = ""
for x in range(len(stacks_copy)):
	result += stacks_copy[x][0]
print(f"Part Two: {result}")