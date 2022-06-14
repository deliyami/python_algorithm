def gcd(a, b):
	a, b = max(a,b), min(a,b)
	while b > 0:
		a, b = b, a % b
		return a

print(gcd(1112, 695))