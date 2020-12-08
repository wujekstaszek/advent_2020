

acc = 0
instructions = []
index = 0


def execute_count():
	global acc
	global instructions
	global index
	if(instructions[index][1] == 1):
		return acc
	instructions[index][1] += 1
	com = instructions[index][0][0:3]
	value = int(instructions[index][0][3:]) 
	if com == "nop":
		index += 1
		return execute_count()
	if com == "acc":
		index += 1
		acc += value
		return execute_count()
	if com == "jmp":
		index += value
		return execute_count()
	

def execute(length,instructions,index,acc,change):
	if (length <= index):
		return acc
	if(instructions[index][1] == 2):
		return 0
	print(f"{index} {instructions[index][0]}")
	instructions[index][1] += 1
	com = instructions[index][0][0:3]
	value = int(instructions[index][0][3:]) 

	if com == "nop":

		index += 1
		result = execute(length,instructions,index,acc,change)
		index -= 1 
		if result!= 0:
			return result
		if change == 0:
			change = 1
			instructions[index][0].replace("nop","jmp",1)
			index += value
			result = execute(length,instructions,index,acc,change)
			if result != 0:
				return result
			index -=value
			instructions[index][0].replace("jmp","nop",1)
			change = 0



	if com == "acc":

		index += 1
		acc += value
		return execute(length,instructions,index,acc,change)

	if com == "jmp":
		index += value
		result = execute(length,instructions,index,acc,change)
		if result != 0:
			return result
		index -= value
		if change == 0 :
			change = 1 
			instructions[index][0].replace("jmp","nop",1)
			index += 1
			result = execute(length,instructions,index,acc,change)

			if result != 0:
				return result
			index -= 1
			instructions[index][0].replace("nop","jmp",1)
			change = 0
		

	instructions[index][1] -= 1
	return 0


with open("input.txt") as input_data:
	for row in input_data:
		instructions.append([row,0])

	print(execute_count())

	length = len(instructions)
	print(execute(length,instructions,0,0,0))
