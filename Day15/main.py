data_dic = {0:1,14:2,6:3,20:4,1:5,4:6}
num = 0
for turn in range(len(data_dic.keys()),30000000):

	if turn == 2019 or turn == (30000000-1):
		print(f"{turn+1} turn: {num}")
	temp_num = num	
	num = turn - data_dic[num]+1 if num in data_dic else 0
	data_dic[temp_num] = turn+1