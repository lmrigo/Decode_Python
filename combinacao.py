def fatorial (n):
	if n == 0:
		return 1
	else:
		return n*fatorial(n-1)


def combinacao (n,s):
	return fatorial(n)/(fatorial(s)*fatorial(n-s))

print combinacao(3,2)
print combinacao(4,2)