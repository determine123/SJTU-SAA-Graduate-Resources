"""Exact checks for examples transcribed from personal matrix study notes."""
from sympy import Matrix, eye, zeros, I, sqrt, symbols, factor, limit, oo, simplify
U=Matrix.hstack(Matrix([1,0,0]),Matrix([1,1,0]),Matrix([1,1,1]))
V=Matrix.hstack(Matrix([-1,0,0]),Matrix([0,1,0]),Matrix([0,1,-1]))
D=Matrix.diag(1,1,0); C=Matrix([[-1,-1,-1],[0,1,1],[0,0,0]])
assert V*C==D*U
B=Matrix([[1,2,3],[4,5,6]]);v=Matrix([1,-2,1])
assert B*v==zeros(2,1) and B.rank()==2 and B.nullspace()==[v]
Z=Matrix([[1+I,2-I],[I,-3]])
assert simplify((Z.H*Z).trace()-sum(abs(x)**2 for x in Z))==0
Q=Matrix.hstack(Matrix([1,0,0,-1])/sqrt(2),Matrix([0,1,0,0]),Matrix([3,0,-2,3])/sqrt(22))
G=Matrix.hstack(Matrix([1,0,0,-1]),Matrix([1,2,0,-1]),Matrix([2,1,-1,1]))
R=Matrix([[sqrt(2),sqrt(2),1/sqrt(2)],[0,2,1],[0,0,sqrt(22)/2]])
assert (Q.T*Q-eye(3)).applyfunc(simplify)==zeros(3)
assert (Q*R-G).applyfunc(simplify)==zeros(4,3)
A=Matrix([[2,1,-1],[1,3,2],[0,2,1]]);b=Matrix([3,-2,1]);x=A.inv()*b
for j in range(3):
 Ai=A.copy();Ai[:,j]=b
 assert Ai.det()/A.det()==x[j]
t=symbols('t', real=True);A=Matrix([[1,t,t**2],[t**2,1,t],[t,t**2,1]]);b=Matrix([t**4,t**3,0])
Ai=A.copy();Ai[:,1]=b
assert factor(A.det())==(t-1)**2*(t**2+t+1)**2
assert factor(Ai.det()-(t**3-t**6))==0
assert simplify(Ai.det()/A.det()+t**3/(t**3-1))==0
assert limit(Ai.det()/A.det(),t,oo)==-1
print('PASS: coordinate map, nullspace, complex trace, Gram-Schmidt, Cramer examples and parameter-system limit')
