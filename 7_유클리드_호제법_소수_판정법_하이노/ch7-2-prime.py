# n은 소수인지 확인할 수
# r은 일치 여부확인하는 수
import random

def fermat(n,r):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(k):
		a = random.randint(1, n-1)
		if pow(a, n-1, n) != 1:
			return False
	return True

print(fermat(113,5))