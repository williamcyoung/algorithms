'''
Working on implementation for Gale Shapley. Not the cleanest implementation, but it's done in
a way that is clear to me personally.
'''

class Proposer():
    def __init__(self, name):
        self.name = name
        self.preferences = []
        self.free = True
        self.unproposed = []
        self.proposed = []
        self.match = None
    
    def __repr__(self):
        return "m_" + str(self.name)

class Acceptor():
    def __init__(self, name):
        self.name = name
        self.preferences = []
        self.free = True
        self.match = None

    def __repr__(self):
        return "w_" + str(self.name)

# initialize proposers and acceptors
m_1 = Proposer(1)
m_2 = Proposer(2)
m_3 = Proposer(3)
m_4 = Proposer(4)
w_1 = Acceptor(1)
w_2 = Acceptor(2)
w_3 = Acceptor(3)
w_4 = Acceptor(4)

# set preferences
m_1.preferences = [w_2, w_1, w_3, w_4]
m_2.preferences = [w_2, w_3, w_1, w_4]
m_3.preferences = [w_1, w_3, w_2, w_4]
m_4.preferences = [w_4, w_1, w_2, w_3]
w_1.preferences = [m_1, m_3, m_2, m_3]
w_2.preferences = [m_3, m_4, m_1, m_2]
w_3.preferences = [m_4, m_2, m_3, m_1]
w_4.preferences = [m_3, m_2, m_1, m_4]

men = [m_1, m_2, m_3, m_4]

for man in men:
    man.unproposed = man.preferences

free_men = [m_1, m_2, m_3, m_4]
women = [w_1, w_2, w_3, w_4]

while len(free_men) > 0:
    man = free_men.pop()
    if len(man.proposed) < len(women):
        w = man.unproposed[0]
        man.unproposed.pop(0)
        man.proposed.append(w)
        if w.free:
            man.match = w
            w.match = man
            w.free = False
            man.free = False
        else:
            # get w.match
            if w.preferences.index(w.match) < w.preferences.index(man):
                free_men.append(man)
                continue
            # if index of w.match.name in w.preferences is 
            else:
                free_men.append(w.match)
                man.match = w
                w.match = man

for man in men:
    print(man.match)