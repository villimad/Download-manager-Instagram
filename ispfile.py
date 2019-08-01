from first import InstDWIMG
from pars_page import Profile

with open('profile.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

p = len(mylist)
for q1 in range(0, p, 1):
    g = mylist[q1]
    One = Profile(g)
    d = One.Pars()
    k = len(d)
    for q2 in range(0, k, 1):
        r = d[q2]
        r = r[:-1]
        r = r[1:]
        two = InstDWIMG(r)
        two.dw()
        pass
    pass
