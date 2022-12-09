data = open("input.txt").read().splitlines()

replaceMap = {"X": "A", "Y": "B", "Z": "C"}
pointsMap  = {"A": 1, "B": 2, "C": 3}
winMap = {"A": "C", "B": "A", "C": "B"}
loseMap = {"C": "A", "A": "B", "B": "C"}

plays = [f"{x[0]} {replaceMap[x[2]]}" for x in data]

def get_points(a, b):
	if a == b:
		return 3
	return 0 if winMap[a] == b else 6

points = sum([pointsMap[x[2]] + get_points(x[0], x[2]) for x in plays])
print(f"Part One: {points}")

points = 0
for play in plays:
	a, b = play.split(" ")
	if b == "A":
		points += pointsMap[winMap[a]]
	elif b == "B":
		points += 3 + pointsMap[a]
	else:
		points += 6 + pointsMap[loseMap[a]]

print(f"Part Two: {points}")