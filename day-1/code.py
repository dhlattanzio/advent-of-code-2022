data = open("input.txt").read().split("\n\n")
elfs = [sum([int(y) for y in x.split("\n")]) for x in data]
print(f"Part One: {max(elfs)}")

elfs.sort()
print(f"Part Two: {sum(elfs[-3:])}")