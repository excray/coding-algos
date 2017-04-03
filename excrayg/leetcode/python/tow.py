
class pegs:
	def __init__(self, naam, vals):
		self.name = naam
		self.l = vals


def toh(s, h, t, n):
	if n == 0:
		return

	
	toh(pegs(s.name, s.l), t, h, n-1)

	
	if s.l:
		print("moving disk %d from %s to %s" %(s.l[len(s.l)-1], s.name, t.name))
		t.l.append(s.l.pop())

	
	toh(pegs(h.name, h.l), s, t, n-1)


s = pegs("peg1", [3,2,1])
h = pegs("peg2", [])
t = pegs("peg3", [])

toh(s,h,t, len(s.l))

print(t.l)


