from collections import deque, defaultdict

def magician_forest(mapping, mana):
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	n, m = len(mapping), len(mapping[0])
	visited = defaultdict(set)
	visited[mana].add((0,0))
	queue = deque([(0, 0, 0, mana)])
	
	while queue:
		x, y, cnt, mana = queue.popleft()

		if (x, y) == (n-1, m-1):
			return cnt
		
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited[mana]:
				if mapping[nx][ny] == '0':
					queue.append((nx,ny, cnt+1, mana))
					visited[mana].add((nx,ny))
				else:
					if mana>0:
						jx, jy = nx + dx[i], ny + dy[i]
						if 0 <= jx < n and 0 <= jy < m and mapping[jx][jy] == '0' and  (jx, jy) not in visited[mana]:
							queue.append((jx, jy, cnt+1, mana-1))
							visited[mana-1].add((jx,jy))
	return -1

def main():
	R, C, K = map(int, input().split())
	mapping = []
	
	for _ in range(R):
		mapping.append(input())
	
	print(magician_forest(mapping, K // 10))

if __name__ == '__main__':
	main()