import math


data = sorted(list(map(int, open("input.txt").read().splitlines())))
adapter_voltage = max(data) + 3
data.append(adapter_voltage)


x = 0
counter = [0,0,0]
for y in data:
	counter[y-x-1] +=1
	x=y
print (counter[0]*counter[2])




#part2

def find_a_ways(data,x=0):
	for index in range(len(data)-1):
		i = index + 1
		while data[i][0] - data[index][0] < 4:
			i+=1
			if i >= len(data):
				break
			data[i-1][1] += data[index][1]

	return data




data.insert(0,0)
data = [[x,0] for x in data]
data[0][1] = 1 
print (find_a_ways(data)[len(data)-2][1])


