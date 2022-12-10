data = open("input.txt").read().splitlines()
trees = [[int(y) for y in x] for x in data]

cols = len(trees[0])
rows = len(trees)
grid = []
for y in range(rows):
	tmp = []
	for x in range(cols):
		tmp.append(None)
	grid.append(tmp)

# Horizontal
for y in range(rows):
	grid[y][0] = True
	max_value = trees[y][0]
	for x in range(1, cols):
		if trees[y][x] > max_value:
			grid[y][x] = True
			max_value = trees[y][x]

	grid[y][-1] = True
	max_value = trees[y][-1]
	for x in range(1, cols):
		if trees[y][-x-1] > max_value:
			grid[y][-x-1] = True
			max_value = trees[y][-x-1]

# Vertical
for x in range(cols):
	grid[0][x] = True
	max_value = trees[0][x]
	for y in range(1, rows):
		if trees[y][x] > max_value:
			grid[y][x] = True
			max_value = trees[y][x]

	grid[-1][x] = True
	max_value = trees[-1][x]
	for y in range(1, rows):
		if trees[-y-1][x] > max_value:
			grid[-y-1][x] = True
			max_value = trees[-y-1][x]

total = 0
for x in grid:
	for y in x:
		total += 1 if y is not None else 0
print(f"Part One: {total}")

def calculate_visibles(trees, x, y, mx, my):
	total = 0
	height = trees[y][x]
	x += mx
	y += my
	while x >= 0 and x < len(trees) and y >= 0 and y < len(trees[0]):
		total += 1
		if trees[y][x] >= height:
			break
		x += mx
		y += my

	return total

def calculate_score(trees, x, y):
	total = calculate_visibles(trees, x, y, 0, -1)
	total *= calculate_visibles(trees, x, y, -1, 0)
	total *= calculate_visibles(trees, x, y, 0, 1)
	total *= calculate_visibles(trees, x, y, 1, 0)
	return total

result = 0
for y in range(rows):
	for x in range(cols):
		result = max(result, calculate_score(trees, x, y))
print(f"Part Two: {result}")