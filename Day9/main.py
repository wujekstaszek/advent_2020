

def find_sum_to_x(current_preambula,x):
	for j in range(25):
		for i in range(j+1,25):
			if(current_preambula[i] + current_preambula[j] == x):
				return True
	return False


def find_weakness(numbers,x):
	len_num = len(numbers)
	for start in range(len_num):
		sum_of_contigous = numbers[start]
		for end in range(start+1,len_num):
			sum_of_contigous += numbers[end]
			if sum_of_contigous == x:
				return numbers[start] + numbers[end]
			elif sum_of_contigous>x:
				break
	return False





with open("input.txt") as input_data:
	numbers = []
	current_preambula = []
	for row in input_data:
		numbers.append(int(row))

	current_preambula = numbers[:25]
	first_preambula = numbers[:25]
	numbers = numbers[25:]
	x = 0
	for number in numbers:
		found = find_sum_to_x(current_preambula,number)
		if found == False:
			print(number)
			x = number
			break
		else:
			current_preambula.pop(0)
			current_preambula.append(number)
	print(find_weakness( first_preambula+ numbers,x))

