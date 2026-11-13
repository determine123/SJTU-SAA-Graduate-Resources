"""Reproduce concrete floating-point examples; standard library only."""
from decimal import Decimal, localcontext
from fractions import Fraction
import math
import sys

assert sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
assert sys.float_info.epsilon == 2.0**-52
assert math.nextafter(1.0, math.inf) - 1.0 == sys.float_info.epsilon
assert Fraction(13.25) == Fraction(53, 4)
assert Fraction(0.1) != Fraction(1, 10)
with localcontext() as ctx:
    ctx.prec = 60
    x, y = Decimal('0.3721478693'), Decimal('0.3720230572')
    exact = x - y
    rounded = Decimal('0.37215') - Decimal('0.37202')
    assert exact == Decimal('0.0001248121')
    relative = abs(rounded - exact) / abs(exact)
    assert Decimal('0.0415') < relative < Decimal('0.0416')
    for xs in ('1e4', '1e8', '1e12'):
        xd = Decimal(xs)
        ref = 1 / ((xd + 1).sqrt() + xd.sqrt())
        xf = float(xs)
        stable = 1 / (math.sqrt(xf + 1) + math.sqrt(xf))
        assert abs(Decimal.from_float(stable) - ref) / ref < Decimal('5e-16')
    for xs in ('1e-4', '1e-8', '1e-12'):
        xd = Decimal(xs)
        ref = xd*xd / ((1+xd*xd).sqrt()+1)
        xf = float(xs)
        stable = xf*xf / (math.sqrt(1+xf*xf)+1)
        assert abs(Decimal.from_float(stable)-ref)/ref < Decimal('5e-16')
    for xs in ('1e-16', '-1e-16', '1e-8', '-1e-8'):
        xd = Decimal(xs); xf = float(xs)
        for got, ref in ((math.expm1(xf), xd.exp()-1), (math.log1p(xf), (1+xd).ln())):
            assert abs(Decimal.from_float(got)-ref)/abs(ref) < Decimal('5e-16')
print('PASS: binary64 spacing, exact fractions, decimal cancellation, rationalized expressions, expm1 and log1p')
