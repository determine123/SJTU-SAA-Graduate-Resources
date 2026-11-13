"""Exact symbolic checks for the fixed matrix in the accompanying note."""
from sympy import Matrix, eye, zeros, Rational, sqrt, symbols, expand
A = Matrix([[3,-2,-4],[-2,6,-2],[-4,-2,3]])
v = Matrix([2,1,2]); I = eye(3)
assert A == 7*I-v*v.T
z=symbols('lambda')
assert expand(A.charpoly(z).as_expr()-(z+2)*(z-7)**2)==0
assert (A+2*I).rref()[0] == Matrix([[1,0,-1],[0,1,-Rational(1,2)],[0,0,0]])
assert (A-7*I).rref()[0] == Matrix([[1,Rational(1,2),1],[0,0,0],[0,0,0]])
Q=Matrix.hstack(v/3, Matrix([1,0,-1])/sqrt(2), Matrix([-1,4,-1])/(3*sqrt(2)))
D=Matrix.diag(-2,7,7)
assert (Q.T*Q-I).applyfunc(expand)==zeros(3)
assert (A*Q-Q*D).applyfunc(expand)==zeros(3)
assert (Q*D*Q.T-A).applyfunc(expand)==zeros(3)
P=v*v.T/9; R=I-P
assert P*P==P and R*R==R and P*R==zeros(3) and P+R==I
assert A == -2*P+7*R
assert -P/2+R/7 == A.inv()
for k in (0,1,2,5):
    assert A**k == (-2)**k*P+7**k*R
assert A.trace()==12 and A.det()==-98
print('PASS: characteristic polynomial, both RREFs, orthonormal eigenbasis, spectral reconstruction, projectors, inverse and powers')
