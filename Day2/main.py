import re

class password:
	def __init__(self,line):
		regex_filter = "([0-9]+)-([0-9]+) (.): (.*)"
		x = re.match(regex_filter,str(line))
		self.bot = int(x[1])
		self.top = int(x[2])
		self.letter = x[3]
		self.password = x[4]

	def check_password(self):
		count = self.password.count(self.letter)
		if self.bot<=count<=self.top:
			return 1
		return 0

	def new_check_password(self):
		if (self.password[self.bot-1] == self.letter) ^ (self.password[self.top-1] == self.letter): 
			return 1
		return 0


if __name__ == "__main__":
	with open("input.txt") as input_data:
		data = input_data.read().splitlines()
		all_paswords = list(map(password,data))
		checked_passwords_part1 = sum(list(map(lambda x: x.check_password(),all_paswords)))
		checked_passwords_part2 = sum(list(map(lambda x: x.new_check_password(),all_paswords)))
		print(checked_passwords_part1)
		print(checked_passwords_part2)