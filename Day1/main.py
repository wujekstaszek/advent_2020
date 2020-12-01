



if __name__ == "__main__":


#PART 1 & 2


	with open("input.txt") as input:
		input = [int(x) for x in list(input)]
		input.sort()
		length = len(input)
		for x in range(length):
			a = input[x]
			for y in range(x,length):
				b = input[y]
				absum = a + b
				if(absum < 2020):
					for z in range(y,length):
						c = input[length-z-1]
						abcsum = absum + c
						if(abcsum == 2020):
							print(f"#PART2\n{a*b*c}")
						if(abcsum < 2020):
							break

				if(absum == 2020):
					print(f"#PART1\n{a*b}")





