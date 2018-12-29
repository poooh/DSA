valx = input("Type value of x : ")
valy = input("Type value of y : ")


def karatsuba(x,y):
	if(len(x) == 1 or len(y) == 1):
		return int(x) * int(y)
	midx = int(len(x) / 2)
	midy = int(len(y) / 2)
	a = x[:midx]
	b = x[midx:]
	c = y[:midy]
	d = y[midy:]
	valac = karatsuba(a,c)
	valbd = karatsuba(b,d)
	diff = str((int(a) + int(b)) * (int(c) + int(d)) - valac - valbd)
	val1 = str(valac).ljust(len(str(valac))+len(x), '0')
	val2 = diff.ljust(len(diff)+midx, '0')
	total = int(val1) + int(val2) + valbd
	return total


print(karatsuba(valx,valy))