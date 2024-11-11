def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)

def plus(n):
	result = 0
	for i in n:
		result += int(i)
	return str(result)
	
def main():
	n = int(input())
	if n >= 6:
		print('9')
	else:
		l = str(factorial(n))
		while True:
			if len(l) == 1:
				print(l)
				break
			l = plus(l)

if __name__=='__main__':
	main()