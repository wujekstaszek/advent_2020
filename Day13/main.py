data = open("input.txt").read().splitlines()
earliest_timestamp = int(data[0])
buses = list(filter(lambda x: x!='x',data[1].split(',')))
buses = list(map(int,buses))
buses = [[bus,bus] for bus in buses]

min_dep = 0 
min_bus = 0
repeat = 1
while repeat:
	repeat = 0
	for bus in buses:
		if bus[0] <= earliest_timestamp:
			repeat = 1
			bus[0] += bus[1]
min_bus = min([bus[0] for bus in buses])
for bus in buses:
	if bus[0] == min_bus:
		print((bus[0] - earliest_timestamp) * bus[1])





data = open("input.txt").read().splitlines()
earliest_timestamp = int(data[0])
buses = list(map(int,data[1].replace('x','0').split(',')))
cnt = 0
cnt_list = []
for i in range(len(buses)-1,-1,-1):
	if buses[i] != 0:
		count = buses[i:].count(0)
		cnt_list.insert(0,count - cnt)
		cnt = count
buses= list(filter(lambda x: x!=0,buses))
buses = [[bus,bus,cnt] for bus,cnt in zip(buses,cnt_list)]
print(buses)
repeat = 1 
while repeat:
	repeat = 1
	cnt = 0
	for bus in buses:
		cnt += bus[2]
		if buses[0][0] + cnt % bus[0] != 0:
			buses[0][0] += buses[0][1]
			print(bus)
			break

	else: 
		repeat = 0

print(buses[0][0])










