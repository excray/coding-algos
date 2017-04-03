
from collections import deque

graph = {'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A','G'],
    'D': ['E'],
    'E': ['F'],
    'F': ['C']}

def find_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph:
    return None
  for node in graph.get(start, []):
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath: return newpath
  return None

def findpathfromprev(start, end, path_finder):
  path = []
  while end != start:
    path = path + [end]
    end = path_finder[end]
  path = path + [start]
  path.reverse()
  return path

def find_path_dfs(graph, start, end):
  stack = []
  visited = set()
  path_finder = {}

  stack = stack + [start]
  while len(stack) != 0:
    
    node = stack.pop()
    visited.add(node)
    if node == end:
      return findpathfromprev(start, end, path_finder)
    else:
      #path.pop()
      for adj_node in reversed(graph.get(node, [])):
        if adj_node not in visited:
          stack.append(adj_node)
          path_finder[adj_node] = node

  return None

def find_path_bfs(graph, start, end):
  q = deque()
  path_finder = {}
  q.append(start)
  path_finder[start] = None

  while len(q) != 0:
    node = q.popleft()
    if node == end:
      return findpathfromprev(start, end, path_finder)
    else:
      for adj_node in graph.get(node, []):
        if adj_node not in path_finder:
          q.append(adj_node)
          path_finder[adj_node] = node

  return None 

nodes = ["A", "B", "C", "D", "E", "F", "G"]
for start in nodes:
  for end in nodes:
    dfs = find_path(graph, start, end)
    dfs_iter = find_path_dfs(graph, start, end)
    print(dfs, dfs_iter)
    assert dfs == dfs_iter
    print("DFS: start: {} end: {} path: {}".format(start, end, dfs))
    print("DFS_ITER: start: {} end: {} path: {}".format(start, end, dfs_iter))
    print("BFS: start: {} end: {} path: {}".format(start, end, find_path_bfs(graph, start, end)))
