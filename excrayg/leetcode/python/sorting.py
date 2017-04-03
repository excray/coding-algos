

#Recursive insertion sort
def rec_insertion(seq, i):
	if i > 0:
		rec_insertion(seq, i-1)
		j = i-1
		while j>0 and seq[j-1] > seq[j]:
			#swap(seq[j-1],seq[j])
			seq[j-1], seq[j] = seq[j], seq[j-1]
			j-=1
		#print seq



import unittest
import random
class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        random.shuffle(self.seq)

    def test_rec_insertion(self):
        # make sure the shuffled sequence does not lose any elements      
        rec_insertion(self.seq, len(self.seq))
        self.assertEqual(self.seq, range(10))        
        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, rec_insertion, (1,2,3))
    

if __name__ == '__main__':
    unittest.main()
    