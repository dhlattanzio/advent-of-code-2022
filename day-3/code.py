data = open("input.txt").read().splitlines()
compartments = [[x[:(len(x)//2)], x[(len(x)//2):]] for x in data]

shareItems = []
for x in compartments:
	for y in set(x[0]):
		if y in x[1]:
			shareItems.append(y)

def calculate_total(shareItems):
	total = 0
	for item in [ord(x) - 96 for x in shareItems]:
		total += item + (58 if item <= 0 else 0)
	return total

print(f"Part One: {calculate_total(shareItems)}")

shareItems = []
groups = [data[(x*3):((x+1)*3)] for x in range(len(data) // 3)]
for group in groups:
	group.sort(key=lambda x: len(x))
	for letter in set(group[-1]):
		if letter in group[0] and letter in group[1]:
			shareItems.append(letter)

print(f"Part Two: {calculate_total(shareItems)}")