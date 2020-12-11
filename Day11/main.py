import itertools


def count_seats(data,row,column,x_max,y_max):
	veritcal = []
	horizontal = []
	if row - 1 >= 0:
		veritcal.append(row-1)
	if row + 1 < y_max:
		veritcal.append(row+1)
	if column + 1 < x_max:
		horizontal.append(column+1)	
	if column - 1 >= 0:
		horizontal.append(column-1)
	veritcal.append(row)
	horizontal.append(column)
	product = list(itertools.product(horizontal,veritcal))
	product.remove((column,row))
	occupied = sum([1 if data[y][x]=='#' else 0 for x,y in product])
	return occupied


def count_first_seats(data,row,column,x_max,y_max):
	veritcal_change = [-1,0,1]
	horizontal_change = [-1,0,1]
	all_possibilities = list(itertools.product(veritcal_change,horizontal_change))
	all_possibilities.remove((0,0))
	counter = 0
	for possibility in all_possibilities:
		y,x = possibility
		y += row
		x += column
		found = 0
		while found==0:
			found = 0
			if row == 1 and column ==0:
				print (x,y)
			if 0 <= y <y_max and 0 <= x <x_max:
				if data[y][x] == "#":
					counter += 1
					found = 1
				elif data[y][x] == 'L':
					found = 1
				else:
					y += possibility[0]
					x += possibility[1]
			else: 
				found = 1
			if row == 1 and column ==0:
				print(counter)
	return counter


	occupied = sum([1 if data[y][x]=='#' else 0 for x,y in product])
	return occupied


def check(data,row,column,x_max,y_max):
	seat = data[row][column]
	if seat == '.':
		return '.'
	occuipied_seats = count_first_seats(data,row,column,x_max,y_max)
	if occuipied_seats <1 and seat == 'L':
		return '#'
	elif occuipied_seats > 4 and seat == '#':
		return 'L'
	return seat

with open ("input.txt") as input_file:
	data = input_file.read().splitlines()
	y_max = len(data)
	x_max = len(data[0])
	change = 1
	while change:
		new_data = []
		change = 0
		for row in range(y_max):
			new_row = []
			for column in range(x_max):
				checked = check(data,row,column,x_max,y_max)
				if checked != data[row][column]:
					change = 1 
				new_row.append(checked)
			new_data.append(new_row)
		data = [[x for x in y] for y in new_data]
		print(*data,'\n',sep="\n")
	print(sum([x.count('#') for x in data]))