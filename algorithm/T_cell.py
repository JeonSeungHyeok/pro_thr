def number(n):
	count = 0
	binary = []
	while True:
		if n == 0:
			return count, binary
		binary.append(n % 2)
		if n % 2:
			count +=1
		n //= 2

def main():
	n = int(input())
	count, num = number(n)
	print(count)
	for i in range(len(num)):
		if num[i] == 1:
			print(i,end=' ')

if __name__=='__main__':
	main()