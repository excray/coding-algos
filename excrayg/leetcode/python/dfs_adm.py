
import sys

class EdgeNode:
	def __init__(self, _y, _wt=0, _next=None):
		self.y = _y
		self.weight = _wt
		self.next = _next


class Graph:
	def __init__(self, num_vertices=0, num_edges = 0, directed = False):
		self.num_vertices = num_vertices
		self.num_edges = num_edges
		self.directed = directed
		self.edges = {}
		self.degree = {}
		self.vertices = set()

	#nv ne
	#e1 e2
	def read(self, fname):
		with open(fname) as f:
			fl = f.readlines()	
			
		assert(len(fl)>=2)
		l = list(map( lambda x: int(x), fl[0].split()))
		self.num_vertices = l[0]			
		num_edges = l[1]

		for i in range(num_edges):
			l = list(map( lambda x: int(x), fl[i+1].split()))
			self.insert_edge(l[0], l[1], self.directed)
			self.vertices.add(l[0])
			self.vertices.add(l[1])

		for i in self.vertices:
			if i not in self.edges:
				self.edges[i] = None


	def insert_edge(self, x, y, directed):
		e = EdgeNode(y)
		if x in self.edges:
			t = self.edges[x]
			e.next = t
			self.edges[x] = e
		else:
			self.edges[x] = e

		if x in self.degree:
			self.degree[x]+=1
		else:
			self.degree[x] = 0

		if not directed:
			self.insert_edge(y,x,True)

		self.num_edges+=1

	def print_graph(self):
		print("Number of vertices: {} Number of Edges: {}".format(self.num_vertices, self.num_edges))
		k = sorted(self.edges.keys())
		for l in k:
			print("{}: ".format(l))
			e = self.edges[l]
			while e:
				print("{} -> {} ".format(l, e.y))
				e = e.next
			print()


class Search(object):
	"""docstring for Search"""
	def __init__(self, arg):
		super(Search, self).__init__()
		self.graph = arg

		self.time = 0
		self.discovered = {}
		self.entry_time = {}
		self.parent = {}
		self.processed = {}
		self.exit_time = {}

		for k in self.graph.vertices:
			self.discovered[k] = False
			self.entry_time[k] = None
			self.parent[k] = None
			self.processed[k] = False
			self.exit_time[k] = None


	def process_vertex_early(self, x):
		print("Process vertex early: {}".format(x))


	def edge_classification(self, x, y):

		if self.parent[y] == x:
			print("Tree edge")
			return

		if self.discovered[y] and not self.processed[y]:
			print("Back edge")
			return

		if self.processed[y] and (self.entry_time[y] < self.entry_time[x]):
			print("Forward edge")
			return

		if self.processed[y] and (self.entry_time[y] > self.entry_time[x]):
			print("Cross edge")
			return


	def process_edge(self, x, y, s):

		print("Processing edge: {} {} {}".format(x, y, s))
		self.edge_classification(x,y)
		if self.parent[x] != y and self.discovered[y]:
			print("Found cycle from {} to {} ".format(y,x))

	def process_vertex_late(self, x):
		print("Process vertex late: {}".format(x))

	def dfs(self, x):
		self.discovered[x] = True
		self.time+=1
		self.entry_time[x] = self.time

		self.process_vertex_early(x)
		e = self.graph.edges[x]	
		while e:
			y = e.y
			if not self.discovered[y]:
				self.parent[y] = x
				self.process_edge(x,y,"IF")	
				self.dfs(y)
			elif not self.processed[y] or self.graph.directed:
				self.process_edge(x, y, "ELSE")

			e = e.next

		self.process_vertex_late(x)
		self.time += 1
		self.exit_time[x] = self.time
		self.processed[x] = True

	def dfs_stat(self):
		for k in self.graph.edges.keys():
			print("{}: Entry time: {}, Exit time: {} Parent: {}".format(k, self.entry_time[k], self.exit_time[k]
								, self.parent[k]))

		
d = False
if len(sys.argv) == 3:
	d = True

g = Graph(0,0,d)
g.read(sys.argv[1])
g.print_graph()

s = Search(g)
s.dfs(1)
s.dfs_stat()

#num edges is wrong.





