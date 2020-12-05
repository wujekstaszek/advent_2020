import re


def check_valid(passport):
	to_find = [("byr:[0-9]{4}",[str(x) for x in range(1920,2003)]),\
	("iyr:[0-9]{4}",[str(x) for x in range(2010,2021)]),\
	("eyr:[0-9]{4}",[str(x) for x in range(2020,2031)]),\
	("hgt:[0-9]{2,3}[a-z]{2}",[str(x)+"cm" for x in range(150,194)]+[str(x)+"in" for x in range(59,77)]),\
	("hcl:\#[0-9a-f]{6}",0),\
	("ecl:(amb|blu|brn|gry|grn|hzl|oth)",0),\
	("pid:[0-9]{1,9}",0)]
	for word in to_find:
		found = re.search(word[0],passport)
		if found == None:
			print(word)
			print(passport)
			return 0
		if word[1] != 0 :
			lol = str(found.group(0))[4:]
			if lol not in word[1]:
				return 0
	return 1


with open("input.txt") as input_data:
	queue = ""
	passports=[]
	for line in input_data:
		if line !="\n":
			queue += line
		else:
			passports.append(queue)
			queue=""
	passports.append(queue)
	counter = sum(list(map(check_valid,passports)))
	print(counter)
