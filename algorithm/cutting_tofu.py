def k_cut(n):
	return n // 2 + 1

def main():
	n = int(input()) # n : 너비
	print(k_cut(n))

if __name__=='__main__':
	main()