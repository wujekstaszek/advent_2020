import re

def slope(list_input,mov_ver,mov_hor):
	x = 0
	y = 0
	height = len(list_input)
	width = len(list_input[1])-2
	counter = 0
	while 0<=y+mov_hor<height:
		x += mov_ver
		y += mov_hor
		if x > width:
			x = x - width-1
		if x < 0:
			x = width + x - 1
		if (list_input[y][x] == '#'):
			counter +=1
	return counter

with open("input.txt") as input:
	list_input = list(input)

	print(list_input)
	mov_vertical = 3
	mov_horizontal = 1
	moves = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	print(f'PART1: {slope(list_input,3,1)}')
	result = 1 
	for move in moves:
		result *= slope(list_input,move[0],move[1])
	print(f'PART2:{result}')
