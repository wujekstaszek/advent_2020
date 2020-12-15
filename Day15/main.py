data = [0,14,6,20,1,4,0]
data_dic = {0:1,14:2,6:3,20:4,1:5,4:6}
for turn in range(len(data),30000000):
	num = data[-1]
	if num in data_dic:
		data.append(turn - data_dic[num])
		data_dic[num] = turn
	else:
		data.append(0)
		data_dic[num] = turn
print(data[30000000-1])