"""Compare the fixed learning example against rational de Boor evaluation."""
from fractions import Fraction as F
import numpy as np
from cad_bspline import POINTS, KNOTS, DEGREE, basis


def de_boor(u):
    knots = list(map(lambda x: F(int(x)), KNOTS))
    span = len(POINTS)-1 if u == knots[-1] else next(
        i for i in range(DEGREE, len(POINTS)) if knots[i] <= u < knots[i+1])
    d = [[F(int(x)) for x in POINTS[j]] for j in range(span-DEGREE, span+1)]
    for r in range(1, DEGREE+1):
        for j in range(DEGREE, r-1, -1):
            i = span-DEGREE+j
            alpha = (u-knots[i])/(knots[i+DEGREE-r+1]-knots[i])
            d[j] = [(1-alpha)*a+alpha*b for a,b in zip(d[j-1], d[j])]
    return np.array([float(x) for x in d[DEGREE]])


if __name__ == '__main__':
    errors = []
    for i in range(801):
        u = F(i,200)
        actual = basis(float(u)) @ POINTS
        expected = de_boor(u)
        errors.append(float(np.max(np.abs(actual-expected))))
        np.testing.assert_allclose(actual, expected, rtol=1e-12, atol=1e-12)
    for u in (-0.01,4.01):
        try:
            basis(u)
        except ValueError:
            pass
        else:
            raise AssertionError('Outside parameter should fail')
    print(f'PASS: 801 rational de Boor comparisons; max error={max(errors):.3g}; outside domain rejected')
