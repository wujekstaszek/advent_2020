import itertools
import math




def find_numbers_summing_to(how_many,to_what,data):
	permutations = list(itertools.permutations(data,how_many))
	result = list(map(lambda x: int(sum(x)),permutations))
	result_index = result.index(to_what)
	return (math.prod(permutations[result_index]))



data = open("input.txt").read().splitlines()
data = list(map(int,data))
how_many = [2,3]
to = [2020,2020]
for number,to_what in zip(how_many,to):
	print(f"Result for {number} numbers while looking for numbers summing to {to_what}: {find_numbers_summing_to(number,to_what,data)}")
