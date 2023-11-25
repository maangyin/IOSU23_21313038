import sys

EPS = 0.00001

def intersect(s, r):
    ((x0,y0),(x1,y1)) = s
    ((x2,y2),(x3,y3)) = r
    if ((x1-x0)*(y2-y0) - (x2-x0)*(y1-y0))*((x1-x0)*(y3-y0) - (x1-x0)*(y3-y0)) < 0:
        return None
    if (x0 == x1 )

segs = []
for line in sys.stdin:
    a,b,c,d=line.split()[0],line.split()[1],line.split()[2],line.split()[3]
    segs.append(((a,b),(c,d)))
ss = []
for i in range(len(segs)):
    ss.append(set())
print(segs)