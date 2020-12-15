




data = open("input.txt").read().splitlines()
memory = {}
for line in data:
	if line[0:4] == "mask":
		mask = line[7:]
	else: 
		addres = line.split('=')[0].split('[')[1].split(']')[0]
		value = line.split('=')[1]
		value = '{0:b}'.format(int(value)).zfill(36)
		result = ""
		if addres not in memory.keys():
			memory[addres] = 36*"0"
		for bit in range(len(mask)):
			result += value[bit] if mask[bit] == 'X'  else mask[bit]
		memory[addres] = result
cnt = 0
for val in memory.values():
	cnt += int(val,2)
print(cnt)




def find_addreses(addres,start):
	result = []

	for bit in range(start,len(addres)):
		if addres[bit] == 'X':
			temp1 = (addres[:bit] + '1'+ addres[bit+1:])
			result += (find_addreses(temp1,bit))
			temp1 = (addres[:bit] + '0'+ addres[bit+1:])
			result += (find_addreses(temp1,bit))
			return result
	return [addres]




memory = {}
for line in data:
	if line[0:4] == "mask":
		mask = line[7:]
	else: 
		addres = '{0:b}'.format(int(line.split('=')[0].split('[')[1].split(']')[0])).zfill(36)
		value = line.split('=')[1]
		value = '{0:b}'.format(int(value)).zfill(36)
		result = ""
		addreses = []
		temp_addr = ""
		for bit in range(len(mask)):
			if mask[bit] == '1':
				temp_addr += '1'
			elif mask[bit] == '0':
				temp_addr += addres[bit]
			else:
				temp_addr += 'X'
		addreses += find_addreses(temp_addr,0)
		for addres in addreses:
			result = ""
			if addres not in memory.keys():
				memory[addres] = 36*"0"
			for bit in range(len(mask)):
				result += value[bit]
			memory[addres] = result
cnt = 0
for val in memory.values():
	cnt += int(val,2)
print(cnt)

