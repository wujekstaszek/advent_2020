

with open("input.txt") as input_data:
	max_seat_id = 1
	seats = [[0 for _ in range(8)] for _ in range(128)]
	for row in input_data:
		top = 127
		bot = 0
		left = 0
		rigth = 7

		for char in row:
			if char == 'F':
				x = (top - bot+1)//2
				top -= x
			elif char == "B":
				x = (top - bot+1)//2
				bot += x
			elif char == "R":
				x = (rigth-left+1)//2
				left += x
			elif char == "L":
				x = (rigth-left+1)//2
				rigth -= x
		seats[top][left] = 1
		seat_id = top * 8 + left
		if max_seat_id < seat_id:
			max_seat_id = seat_id
	for i in range(128):
		for j in range(0,8):
			if seats[i][j] == 0:
				print(i * 8 + j)