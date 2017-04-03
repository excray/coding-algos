from random import randrange


#Problem statement:
#Given a set of people who are sitting on some seats, 
#and they like to sit on some other seats,
#find a permutation such that max people are satisfied. 
#[2,2,0,5,3,5,7,4]
def naive_max_perm(preferred_seats, seats_in_contention):
	if len(seats_in_contention) <= 1:
		return seats_in_contention
	seats_that_are_preferred = set(preferred_seats[i] for i in seats_in_contention)
	seats_not_preferred = seats_in_contention - seats_that_are_preferred
	if seats_not_preferred:
		seats_in_contention -= seats_not_preferred
		return naive_max_perm(preferred_seats, seats_in_contention)

	return seats_in_contention

from collections import Counter
def max_perm(preferred_seats):
	n = len(preferred_seats)
	seats_in_contention = set(range(n))
	count = Counter(preferred_seats)
	seats_not_preferred = [i for i in seats_in_contention if count[i]==0 ]
	while seats_not_preferred:
		k = seats_not_preferred.pop()
		seats_in_contention.remove(k)
		j = preferred_seats[k]
		count[j] -= 1
		if count[j] == 0:
			seats_not_preferred.append(j)

	return seats_in_contention

#
def naive_celebrity(celeb_graph):
	num_nodes = len(celeb_graph)
	for node1 in range(num_nodes):
		for node2 in range(num_nodes):
			if node1 == node2:
				continue
			if celeb_graph[node1][node2] == 1: #node1 knows someone
				break
			if celeb_graph[node2][node1] == 0: #someone doesnt know node1
				break
		else:
			print(node1)


import unittest
import random
class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		self.preferred_seats = [2,2,0,5,3,5,7,4]
		self.seats_in_contention = set(range(len(self.preferred_seats)))

	def test_naive_max_perm(self):
	# make sure the shuffled sequence does not lose any elements      
		perm = naive_max_perm(self.preferred_seats, self.seats_in_contention)
		self.assertEqual(perm, {0,2,5})  

	def test_max_perm(self):
		perm = max_perm(self.preferred_seats)
		self.assertEqual(perm, {0,2,5})

	def test_naive_celeb(self):
		n = 10
		celeb_graph = [[randrange(2) for i in range(n)] for i in range(n)]
		print(celeb_graph)
		naive_celebrity(celeb_graph)

if __name__ == '__main__':
	unittest.main()


