N, M = map(int, input().split())

planet = {}

for i in range(N):
    tmp = {i+1: {'small': set(), 'big': set()}}
    planet.update(tmp)

for i in range(M):
    big, small = map(int, input().split())


    planet[big]['small'].add(small)
    planet[big]['small'].update(planet[small]['small'])
    for s in planet[small]['small']:
        planet[s]['big'].add(big)
        planet[s]['big'].update(planet[big]['big'])


    planet[small]['big'].add(big)
    planet[small]['big'].update(planet[big]['big'])
    for b in planet[big]['big']:
        planet[b]['small'].add(small)
        planet[b]['small'].update(planet[small]['small'])

for i in range(1, N+1):
    small_count = len(planet[i]['small'])
    big_count = len(planet[i]['big'])
    print(big_count, small_count)
    
#------------------------------------------------------------------------
# from collections import defaultdict, deque

# def count_planets(N, comparisons):
#     larger_than = defaultdict(list)  # a > b 일 때 a에서 b로 가는 간선
#     smaller_than = defaultdict(list)  # 반대로 b에서 a로 가는 간선

#     # 그래프 구성
#     for a, b in comparisons:
#         larger_than[a].append(b)
#         smaller_than[b].append(a)

#     # 각 행성보다 큰 행성의 수를 찾는 DFS 함수
#     def dfs(graph, start):
#         visited = [False] * (N + 1)
#         stack = [start]
#         visited[start] = True
#         count = 0
#         while stack:
#             node = stack.pop()
#             for neighbor in graph[node]:
#                 if not visited[neighbor]:
#                     visited[neighbor] = True
#                     stack.append(neighbor)
#                     count += 1
#         return count

#     results = []
#     for i in range(1, N + 1):
#         larger_count = dfs(larger_than, i)
#         smaller_count = dfs(smaller_than, i)
#         results.append((larger_count, smaller_count))
    
#     return results

# # 입력 처리
# N, M = map(int, input().split())
# comparisons = [tuple(map(int, input().split())) for _ in range(M)]

# # 결과 계산 및 출력
# results = count_planets(N, comparisons)
# for larger, smaller in results:
#     print(smaller, larger)
