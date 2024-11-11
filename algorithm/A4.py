def make_A4(n,m):
	A4_l = 20
	A4_h = 40
	
	result = (n // A4_h) * (m // A4_l) + (n // A4_l) * (m // A4_h) - (n // A4_h) * (m // A4_h) * 2
	return result

def main():
	n,m = map(int, input().split())
	print(make_A4(n, m))
	
if __name__=='__main__':
	main()