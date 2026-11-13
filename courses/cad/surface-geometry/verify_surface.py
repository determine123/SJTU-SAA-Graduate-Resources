"""Exact surface-form checks from the personal CAD verification script."""
import sympy as s

u,v,k=s.symbols('u v k',real=True)
r=s.Matrix([u-u**3/3+u*v**2,v-v**3/3+v*u**2,u*u-v*v])
ru,rv=r.diff(u),r.diff(v); h=1+u*u+v*v
normal=s.simplify(ru.cross(rv)/h**2)
assert s.simplify(normal.dot(normal)-1)==0
assert [s.factor(ru.dot(ru)),s.factor(ru.dot(rv)),s.factor(rv.dot(rv))]==[h**2,0,h**2]
assert [s.simplify(normal.dot(r.diff(u,2))),s.simplify(normal.dot(r.diff(u).diff(v))),s.simplify(normal.dot(r.diff(v,2)))]==[2,0,-2]
assert s.factor((s.diag(2,-2)-k*s.diag(h**2,h**2)).det())==s.factor(k*k*h**4-4)


print('PASS: unit normal, first and second fundamental forms, principal-curvature characteristic equation')
