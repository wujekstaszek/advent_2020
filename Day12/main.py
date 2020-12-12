



data = open("input.txt").read().splitlines()
pos_directions = ['N','E','S','W']
direction = 'E'
x_coord = 0
y_coord = 0
w_x_coord = 10
w_y_coord = 1
for instruction in data:
	ins_dir = instruction[0]
	ins_value = int(instruction[1:])





	if ins_dir == 'F':
		x_coord += ins_value * w_x_coord
		y_coord += ins_value * w_y_coord
	if ins_dir == 'N':
		w_y_coord += ins_value
	if ins_dir == 'S':
		w_y_coord -= ins_value
	if ins_dir == 'E':
		w_x_coord += ins_value
	if ins_dir == 'W':
		w_x_coord -= ins_value

	if ins_dir == 'R':
		times = int(ins_value)//90
		for _ in range(times):
			temp_x = w_x_coord
			temp_y = w_y_coord
			w_x_coord = temp_y
			w_y_coord = - temp_x

	if ins_dir == 'L':
		times = int(ins_value)//90
		for _ in range(times):
			temp_x = w_x_coord
			temp_y = w_y_coord
			w_x_coord = - temp_y
			w_y_coord = temp_x

print(x_coord+y_coord)
