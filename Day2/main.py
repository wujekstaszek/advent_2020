import re

def check_password(password_line):
	regex_filter = "([0-9]+)-([0-9]+) (.): (.*)"
	x = re.match(regex_filter,str(password_line))
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
	x = re.match(regex_filter,str(password_line))
	bot = int(x[1])
	top = int(x[2])
	letter = x[3]
	password = x[4]
	if (password[bot-1] == letter) ^ (password[top-1] == letter): 
		return 1
	return 0


if __name__ == "__main__":
	with open("input.txt") as input_data:
		data = input_data.read().splitlines()
		checked_passwords_part1 = sum(list(map(check_password,data)))
		checked_passwords_part2 = sum(list(map(new_check_password,data)))
		print(checked_passwords_part1)
		print(checked_passwords_part2)