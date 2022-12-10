data = open("input.txt").read().splitlines()
pairs = [[[int(u) for u in y.split("-")] for y in x.split(",")] for x in data]

def is_fully_contained(pair):
	return (pair[0][0]<=pair[1][0] and pair[0][1]>=pair[1][1]) or \
			(pair[1][0]<=pair[0][0] and pair[1][1]>=pair[0][1]);

total = 0
for pair in pairs:
	total += 1 if is_fully_contained(pair) else 0

print(f"Part One: {total}")

def is_overlaps(pair):
	return (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or \
			(pair[0][1] >= pair[1][0] and pair[0][1] <= pair[1][1]) or \
			(pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1])

total = 0
for pair in pairs:
	total += 1 if is_overlaps(pair) else 0

print(f"Part Two: {total}")