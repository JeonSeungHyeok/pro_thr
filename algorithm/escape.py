def correction(p, c):
		if c in p:
			return '1'
		else:
			return '0'

def main():
	n = int(input())
	problem = set(input().split())
	m = int(input())
	check = input().split()
	for num in check:
		print(correction(problem, num))
	
if __name__ == '__main__':
	main()