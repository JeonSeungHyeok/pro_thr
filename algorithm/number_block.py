def main():
	n = int(input())
	stack = []
	count, num = 0, 0
	
	for _ in range(2 * n):
		cmd = input().strip()
		if cmd == 'remove':
			num += 1
			if stack and stack[-1] != num:
				count += 1
				stack = []
			if stack:
				stack.pop()
		else:
			stack.append(int(cmd.split()[1]))
	print(count)

if __name__ == '__main__':
	main()
