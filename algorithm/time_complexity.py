def count_zero(n):
	result = 0
	while True:
		if n < 5:
			return result
		else:
			result += n // 5
			n //= 5
			
	

def main():
	n=int(input())
	print(count_zero(n))
	
if __name__=='__main__':
	main()
	