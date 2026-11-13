"""Exact subdivision and control-hull checks from the personal learning script."""
from fractions import Fraction as F
import random

P=[(F(0),F(0)),(F(2),F(2)),(F(3),F(2)),(F(3),F(0))]
def mix(a,b,t): return tuple((1-t)*x+t*y for x,y in zip(a,b))
def split(p,t):
    a=[mix(p[i],p[i+1],t) for i in range(3)]
    b=[mix(a[i],a[i+1],t) for i in range(2)]
    c=mix(b[0],b[1],t)
    return [p[0],a[0],b[0],c],[c,b[1],a[2],p[3]]
def evaluate(p,t):
    while len(p)>1: p=[mix(p[i],p[i+1],t) for i in range(len(p)-1)]
    return p[0]
L,R=split(P,F(1,2))
M,N=split(R,F(1,3))
expected=[[(0,0),(1,1),(F(7,4),F(3,2)),(F(9,4),F(3,2))],
 [(F(9,4),F(3,2)),(F(29,12),F(3,2)),(F(23,9),F(13,9)),(F(8,3),F(4,3))],
 [(F(8,3),F(4,3)),(F(26,9),F(10,9)),(3,F(2,3)),(3,0)]]
assert [L,M,N]==expected
for pts,lo,hi in [(L,F(0),F(1,2)),(M,F(1,2),F(2,3)),(N,F(2,3),F(1))]:
    for k in range(101):
        s=F(k,100)
        assert evaluate(pts,s)==evaluate(P,lo+(hi-lo)*s)
def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(pts):
    pts=sorted(set(pts)); lower=[]; upper=[]
    for p in pts:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
        upper.append(p)
    return set(lower[:-1]+upper[:-1])
A=M[0]; B=M[3]; H=(F(5,2),F(3,2))
random.seed(20261015)
cases=[(F(1,8),F(1,12)),(F(1,4),F(1,12)),(F(1,8),F(1,6)),(F(1,4),F(1,6)),(F(1,2),F(1,12)),(F(1,8),F(1,3)),(F(1,2),F(1,3))]
cases += [(F(random.randint(1,100),100),F(random.randint(1,100),100)) for _ in range(1000)]
for a,b in cases:
    C=(A[0]+a,A[1]); D=(B[0]-b,B[1]+b)
    if a<F(1,4) and b<F(1,6): predicted={A,C,D,B}
    elif a<=F(1,4) and b<=F(1,6): predicted={A,H,B}
    elif a>F(1,4) and b<=F(1,6): predicted={A,C,B}
    elif a<=F(1,4) and b>F(1,6): predicted={A,D,B}
    else: predicted={A,C,D,B}
    assert hull([A,B,C,D])==predicted,(a,b)

print('PASS: exact subdivision, 303 exact curve comparisons, 1007 convex-hull parameter cases')
