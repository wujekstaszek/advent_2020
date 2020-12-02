import re

def check_password(password_line):
	regex_filter = "([0-9]+)-([0-9]+) (.): (.*)"
	x = re.split(regex_filter,str(password_line))
	bot = int(x[1])
	top = int(x[2])
	letter = x[3]
	password = x[4]
	count = password.count(letter)
	if bot<=count<=top:
		return 1
	return 0

def new_check_password(password_line):
	regex_filter = "([0-9]+)-([0-9]+) (.): (.*)"
	x = re.split(regex_filter,str(password_line))
	bot = int(x[1])
	top = int(x[2])
	letter = x[3]
	password = x[4]
	print(bot,top,letter,password,count)
	if (password[bot-1] == letter) ^ (password[top-1] == letter): 
		return 1
	return 0


if __name__ == "__main__":
	with open("input.txt") as input:
		count = 0
		count2=0
		for password_line in input:
			if check_password(password_line):
				count+=1
			if new_check_password(password_line):
				count2+=1
		print(count)
		print(count2)