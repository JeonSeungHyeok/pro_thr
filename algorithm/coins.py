def money(coins):
	n = len(coins)
	dp = [0] * n
	dp[0] = coins[0]
	
	for i in range(1,n):
		dp[i] = max(coins[i], dp[i-1]+coins[i])
	if max(dp) < 0:
		return 0
	return max(dp)

def main():
	N = int(input())
	coins = list(map(int, input().split()))
	print(money(coins))

if __name__=='__main__':
	main()