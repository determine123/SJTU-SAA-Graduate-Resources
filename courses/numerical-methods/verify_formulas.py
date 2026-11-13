"""Reproducible checks of examples; not a proof of every note."""
from fractions import Fraction as F
import math
import numpy as np


def lagrange(nodes, values, x):
    return sum(y*math.prod((x-b)/(a-b) for j,b in enumerate(nodes) if j != i)
               for i,(a,y) in enumerate(zip(nodes,values)))


def simpson(values, h):
    n = len(values)-1
    if n < 2 or n % 2:
        raise ValueError('Even positive subinterval count required')
    return h/3*(values[0]+values[-1]+4*sum(values[1:-1:2])+2*sum(values[2:-1:2]))


if __name__ == '__main__':
    nodes = list(map(F,(-1,0,2)))
    for x in map(F,(-1,0,1,2,3)):
        assert lagrange(nodes,[t*t+2*t+3 for t in nodes],x) == x*x+2*x+3
    for degree in range(4):
        assert simpson([F(i,4)**degree for i in range(5)],F(1,4)) == F(1,degree+1)
    for n in (1,3):
        try:
            simpson([0]*(n+1),1)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid count accepted')
    for nodes,weights,max_degree in (
        ([-1/math.sqrt(3),1/math.sqrt(3)],[1,1],3),
        ([0,-math.sqrt(3/5),math.sqrt(3/5)],[8/9,5/9,5/9],5)):
        for degree in range(max_degree+1):
            expected = 0 if degree % 2 else 2/(degree+1)
            assert abs(sum(w*x**degree for w,x in zip(weights,nodes))-expected)<1e-14
    x=np.array([-2.,-1.,0.,1.,2.]); A=np.column_stack((np.ones_like(x),x))
    y=np.array([0.,2.,1.,4.,3.]); c=np.linalg.lstsq(A,y,rcond=None)[0]
    np.testing.assert_allclose(A.T@(A@c-y),0,atol=1e-13)
    np.testing.assert_allclose(c,[2.,.8],atol=1e-13)
    print('PASS: interpolation; Simpson degree 0-3 and parity; Gauss degree 0-3/0-5; least-squares orthogonality')
