def main():
	n, m = map(int, input().split())
	money = list(map(int, input().split()))
	
	prefix_sum = [0] * (n + 1)

	for i in range(n):
		prefix_sum[i+1] = prefix_sum[i] + money[i]
	
	for _ in range(m):
		a, b = map(int, input().split())
		result = prefix_sum[b] - prefix_sum[a - 1]
		print(('+' if result > 0 else '') + str(result))
		
if __name__ == '__main__':
	main()
