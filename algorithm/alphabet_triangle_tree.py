def calc_tree(n, tree):
	store = {}
	store[0] = {0: tree[0][0]}

	for i in range(1, n):
		store[i] = {}
		for j in range(len(tree[i])):
			if j == 0:
				store[i][j] = tree[i][j] + store[i-1][j]
			elif j == len(tree[i]) - 1:
				store[i][j] = tree[i][j] + store[i-1][j-1]
			else:
				store[i][j] = tree[i][j] + max(store[i-1][j-1], store[i-1][j])

	return max(store[n-1].values())


def main():
	n = int(input())
	tree = []

	for _ in range(n):
		tree.append(list(map(lambda x: ord(x) - 64, input())))

	print(calc_tree(n, tree))
	
if __name__ == '__main__':
	main()
