def removed_ant(ants, d):
	s, e = 0, 0
	max_ant = 0
	while s < len(ants) and e < len(ants):
		length = ants[e] - ants[s]
		count = e - s + 1
		if length <= d:
			e += 1
			if max_ant < count:
				max_ant = count
		else:
			s +=1
	return len(ants) - max_ant

def main():
	n, d = map(int, input().split()) # n : 개미 마리, d : 두 개미사이의 거리
	ants = list(map(int, input().split())) # ants : 개미 집합
	
	print(removed_ant(sorted(ants), d))
	
if __name__=='__main__':
	main()