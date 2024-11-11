# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math
def main():
	a, b = map(int, input().split())
	diff = abs(a-b)
	count = 0
	if diff >= 1:
		print(2)
	else:
		for i in range(2, int(math.sqrt(a))+1):
			if not a % i:
				count = 1
				print(i)
				break
		if not count:
			print(a)
if __name__ == '__main__':
	main()