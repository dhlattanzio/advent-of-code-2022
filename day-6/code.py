data = open("input.txt").read()

letters = []
start_package_index = -1
for i in range(len(data)):
	letters.append(data[i])
	if len(letters) > 4: 
		letters.pop(0)
	if len(letters) == 4 and len(set(letters)) == 4:
		start_package_index = i + 1
		break

print(f"Part One: {start_package_index}")

start_message_index = -1
for i in range(len(data)):
	letters.append(data[i])
	if len(letters) > 14: 
		letters.pop(0)
	if len(letters) == 14 and len(set(letters)) == 14:
		start_message_index = i + 1
		break

print(f"Part Two: {start_message_index}")