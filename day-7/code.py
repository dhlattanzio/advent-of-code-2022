data = open("input.txt").read().splitlines()

directories = {}
path = ["/"]
for line in data:
	op = line.split(" ")
	if op[0] == "$":
		if op[1] == "cd":
			if op[2] == "/":
				path = ["/"]
			elif op[2] == "..":
				path.pop(-1)
			else:
				path.append(op[2])
	else:
		key = "/" + "/".join(path[1:])
		directory = directories.get(key, {})
		if op[0] == "dir":
			dirs = directory.get("dirs", [])
			dirs.append(op[1])
			directory["dirs"] = dirs
		else:
			files = directory.get("files", [])
			files.append([op[1], op[0]])
			directory["files"] = files
		directories[key] = directory

map_sizes = {}
def calculate_size(dir_name):
	if dir_name in map_sizes:
		return map_sizes[dir_name]

	total_size = 0
	dir = directories[dir_name]
	if "dirs" in dir:
		for subdir in dir["dirs"]:
			total_size += calculate_size(f"{dir_name}/{subdir}" if dir_name != "/" else f"{dir_name}{subdir}")
	if "files" in dir:
		for file in dir["files"]:
			total_size += int(file[1])

	map_sizes[dir_name] = total_size
	return total_size

total = 0
for key in directories:
	size = calculate_size(key)
	if size <= 100_000:
		total += size
print(f"Part One: {total}")

current_space = 70_000_000 - calculate_size("/")
required_space = 30_000_000 - current_space

list_of_sizes = []
for key in map_sizes:
	list_of_sizes.append(map_sizes[key])
list_of_sizes.sort()

smallest = 0
for size in list_of_sizes:
	if size >= required_space:
		smallest = size
		break
print(f"Part Two: {smallest}")