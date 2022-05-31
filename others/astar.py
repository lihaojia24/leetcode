from queue import PriorityQueue

def remain_cost(point, target):
  return abs(target[0] - point[0]) + abs(target[1] - point[1])

def draw_path(graph, came_from, target):
  graph[target[0]][target[1]] = 2
  while came_from[target]:
    graph[came_from[target][0]][came_from[target][1]] = 2
    target = came_from[target]
  for line in graph:
    print(line)

def a_star_search(graph, start, target):
  nextstep = [[-1,0], [1,0], [0,1], [0,-1]]
  MAX_X, MAX_Y = len(graph), len(graph[0])
  q = PriorityQueue()
  q.put(start, 0)
  came_from = {}
  came_from[start] = None
  cost_so_far = {}
  cost_so_far[start] = 0
  while not q.empty():
    cnt = q.get()
    if cnt == target:
      # TODO: draw path
      draw_path(graph, came_from, target)
      return came_from, cost_so_far, True
    for ns in nextstep:
      nxtX, nxtY = cnt[0] + ns[0], cnt[1] + ns[1]
      nxt = (nxtX, nxtY)
      nxt_cost_so_far = cost_so_far[cnt] + 1
      if (-1<nxtX<MAX_X and -1<nxtY<MAX_Y and graph[nxtX][nxtY] == 0) and (nxt not in cost_so_far or nxt_cost_so_far < cost_so_far[nxt]):
        cost_so_far[nxt] = nxt_cost_so_far
        came_from[nxt] = cnt
        nxt_remain_cost = remain_cost(nxt, target)
        q.put(nxt, nxt_remain_cost+ nxt_cost_so_far) 
  # TODO: draw path
  return came_from, cost_so_far, False

graph = [
        [0,0,0,0],
        [1,1,0,1],
        [0,0,0,0],
        [1,0,0,0]]
start = (0,0)
target = (3,3)
_, _, ans = a_star_search(graph, start, target)
print(ans)
