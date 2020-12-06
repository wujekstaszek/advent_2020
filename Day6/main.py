


def check(group):
	questions = [0 for _ in range(26)]
	line_cnt = -1 
	group = group.split("\n")
	for line in group:
		line_cnt += 1 
		for char in line:
			if char != "\n":
				questions[ord('z')-ord(char)] += 1
	sum_cnt = 0
	print(line_cnt)
	for question in questions:
		if question == line_cnt:
			sum_cnt+=1
	return sum_cnt

with open("input.txt") as input_data:
	queue = ""
	groups = []
	for row in input_data:
		if row == "\n":
			groups.append(queue)
			queue =""
		else:
			queue += row
	groups.append(queue)
	print( sum(list(map(check,groups))))
