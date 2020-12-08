import re

def find_colors(data,color):
	colors = []
	inside_colors = []
	bag_counter = 0
	counter = 0
	to_find =f"^{color} (.*)"
	print(to_find)
	for row in data:
		found = re.search(to_find,row)
		if found != None:
			contain = re.findall("([0-9]) (.*?) bag",row)
			if contain != None:
				for color in contain:
					number = color[0]
					name = color[1]
					bag_counter += int(number) * find_colors(data, str(name))
					bag_counter += int(number)

	return bag_counter




used_colors =["shiny gold"]
def found_father_color(data,color):
	colors = []
	inside_colors = []
	to_find =f"(.+) bags (.+){color}"

	for row in data:
		found = re.search(to_find,row)
		if found != None:
			inside_colors.append(found.group(1))

	if inside_colors is not None:
		for inside_color in inside_colors:
			if inside_color not in used_colors:
				used_colors.append(inside_color)
				colors += found_father_color(data,inside_color)
	colors.append(color)
	return colors


with open("input.txt") as input_data:
	input_strings = input_data.read().split("\n")
	#all_colors = found_father_color(input_strings,"shiny gold")
	#print(len(list(set(all_colors))))
	#print(used_colors)
	print(find_colors(input_strings,"shiny gold"))