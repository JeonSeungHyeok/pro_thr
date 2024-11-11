def catch_fish(fish, m):
	result = 0
	count = 0
	for i in range(len(fish)):
		result = fish[i]
		if result == m:
			count += 1
			continue
		for j in range(i+1,len(fish)):
			result+= fish[j]
			if result == m:
				count += 1
				break
			elif result > m:
				break
	return count

def main():
	n,m = map(int, input().split())
	fish = list(map(int, input().split()))
	
	print(catch_fish(fish, m))
	
if __name__ == '__main__':
	main()