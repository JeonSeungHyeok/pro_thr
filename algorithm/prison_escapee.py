# CCW(Counter ClockWise)
def main():
	n =int(input())
	coordinate = []
	for _ in range(n):
		coordinate.append(list(map(float,input().split())))
	
	for i in range(2,n):
		first = [coordinate[i-1][0] - coordinate[i-2][0], coordinate[i-1][1] - coordinate[i-2][1]]
		second = [coordinate[i][0] - coordinate[i-1][0], coordinate[i][1] - coordinate[i-1][1]]
		result = first[0] * second[1] - first[1] * second[0]
		print("LEFT" if result > 0 else "RIGHT")

if __name__ == '__main__':
	main()