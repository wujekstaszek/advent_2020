import itertools
import math
import functools

def slope(moves,list_input):
	mov_hor,mov_ver = moves[1],moves[0]
	x,y = 0,0
	height = len(list_input)
	width = len(list_input[1])-2
	counter = 0
	while 0<=y+mov_hor<height:
		x += mov_ver	
		y += mov_hor
		if x > width:
			x = x - width-1
		counter += 1 if list_input[y][x] == '#' else 0
	return counter


with open("input.txt") as input_data:
	list_input = list(input_data)
	moves = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	print(f'PART1: {slope([3,1],list_input)}')
	result = math.prod(map(slope,moves,itertools.repeat(list_input)))
	print(f'PART2: {result}')
