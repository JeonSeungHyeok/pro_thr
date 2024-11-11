# 구간 합 응용
# A~B 합 = sum(B) - sum(A-1)
def new_crypto(key1, key2):
	key1 -= 1
	if key1 % 2 :
		if (key1+1) // 2 % 2:
			key1 = 1
		else:
			key1 = 0
	else:
		if (key1+1) // 2 % 2:
			key1 ^= 1

	if key2 % 2 :
		if (key2+1) // 2 % 2:
			key2 = 1
		else:
			key2 = 0
	else:
		if (key2+1) // 2 % 2:
			key2 ^= 1
	
	return key2 ^ key1

def main():
	key1, key2 = map(int, input().split())
	print(new_crypto(key1, key2))
	
if __name__ == '__main__':
	main()