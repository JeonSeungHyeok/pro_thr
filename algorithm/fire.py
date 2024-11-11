from collections import deque

def diffused_fire(maze, person, fires):
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	n, m = len(maze), len(maze[0])
	queue = deque(fires)
	queue.append((-1,-1))
	time = -1
	visited = [[False]*m for _ in range(n)]
	for fire in fires:
		visited[fire[0]][fire[1]] = True
	
		
	while queue:
		x,y = queue.popleft()
		if x == -1 and y == -1 and len(queue) > 0:
			time +=1
			queue.append((-1,-1))
			continue
		if maze[x][y] == '&':
			return time
		
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			
			if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] != '#':
				queue.append((nx,ny))
				visited[nx][ny] = True
		
	return -1


def main():
	r, c = map(int, input().split())
	maze, person, fire = [], [], []
	
	for i in range(r):
		maze.append(input())
		if '&' in maze[i]:
			person.append((i, maze[i].find('&')))
		for idx,j in enumerate(maze[i]):
			if '@' == j:
				fire.append((i, idx))

	print(diffused_fire(maze, person, fire))

if __name__=='__main__':
	main()
