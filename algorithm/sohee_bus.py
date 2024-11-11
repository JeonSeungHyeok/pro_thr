def board(n, t, start, delay):
	min_value = t
	index = 0
	
	for i in range(n):
		time = start[i]
		
		while True:
			if t <= time:
				if min_value > time - t:
					min_value = time - t
					index = i
				break
			time += delay[i]
	return index + 1

def main():
	n, t = map(int, input().split()) # n : 버스 개수, t : 소희 도착 시간
	start, delay = [], []
	
	for _ in range(n):	# 버스 n대 나열
		s, d = map(int, input().split()) # s : 최초 운행시간, d : 회귀 시간
		start.append(s), delay.append(d)
	
	print(board(n, t, start, delay))
	
	
if __name__=='__main__':
	main()