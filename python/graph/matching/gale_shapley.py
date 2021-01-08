'''
Working on implementation for Gale Shapley. Not the cleanest implementation, but it's done in
a way that is clear to me personally.
'''

class Proposer():
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.free = True
        self.unproposed = preferences
        self.proposed = []
        self.match = None

class Acceptor():
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.free = True
        self.match = None

# initialize proposers and acceptors
m_1 = Proposer(1, [2, 1, 3, 4])
m_2 = Proposer(2, [2, 3, 1, 4])
m_3 = Proposer(3, [1, 3, 2, 4])
m_4 = Proposer(4, [4, 1, 2, 3])
w_1 = Acceptor(1, [1, 3, 2, 4])
w_2 = Acceptor(2, [3, 4, 1, 2])
w_3 = Acceptor(3, [4, 2, 3, 1])
w_4 = Acceptor(4, [3, 2, 1, 4])

free_men = [m_1, m_2, m_3, m_4]
women = [w_1, w_2, w_3, w_4]

while free_men:
    man = free_men.pop()
    if len(man.proposed) < len(women):
        w = man.unproposed[0]
        if w.free:
            man.unproposed.pop(0)
            man.proposed.append(w)
            man.match = w
            w.match = man