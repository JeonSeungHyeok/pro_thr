def can_complete_tasks(n, days):
	for first_s, first_e in days.items():
		for sub_s, sub_e in days.items():
			if first_s == sub_s:
				continue
			if first_e > sub_s and first_e < sub_e:
				return 'No'
		days[first_s] = 0
	return "Yes"


def parse_date(date):
	month, day = map(int, date.split('/'))
	return month * 31 + day  

def main():
	n = int(input()) 
	day = {}
	for _ in range(n):
		start, end = input().split()
		if not day.get(parse_date(start)):
			day[parse_date(start)] = parse_date(end)
		elif day.get(parse_date(start)) < parse_date(end):
			day[parse_date(start)] = parse_date(end)

	day = dict(sorted(day.items()))
	print(can_complete_tasks(n, day))

if __name__ == '__main__':
	main()