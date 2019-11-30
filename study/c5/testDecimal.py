from decimal import Decimal
import math
print(repr(Decimal('0.10') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')))
print(repr(Decimal(0.1) + Decimal(0.1) + Decimal(0.10) - Decimal(0.3)))
print(Decimal(1.1))
print(Decimal(1)/Decimal(7))

print(repr(0.1+0.1))

print(int(0o17))

print(int(0x17))

print(int(0b1111))i

print(int('1111', 2))
print(int('0b1111', 2))

print(10//3)
print(10//3.11)

print(10/3)

print(round(2.2))
print(round(2.6))
print(round(-2.2))
print(round(-2.6))


print(math.floor(2.2))
print(math.floor(2.6))
print(math.floor(-2.2))
print(math.floor(-2.6))