def mergesort(arr):
	if len(arr) <= 1:
		return arr
	mid = int(len(arr) / 2)
	lefttree =  arr[:mid]
	righttree = arr[mid:]
	# print("check1")
	# print(lefttree)
	# print(righttree)
	mergesort(lefttree)
	mergesort(righttree)
	i = 0
	j = 0
	k = 0
	while i < len(lefttree) and j < len(righttree):
		# print(lefttree)
		# print(righttree)
		# print(i)
		# print(j)
		# print(lefttree[i])
		# print(righttree[j])
		if (lefttree[i] <= righttree[j]):
			# print("check6")
			arr[k] = lefttree[i]
			# print(arr)
			i = i + 1
			k = k + 1
		else:
			# print("check7")
			arr[k] = righttree[j]
			# print(arr)
			j = j + 1
			k = k + 1
	while i < len(lefttree):
		arr[k] = lefttree[i]
		i = i + 1
		k = k + 1

	while j < len(righttree):
		arr[k] = righttree[j]
		j = j + 1
		k = k + 1

	return arr

s = input("Type Array to sort : ")
arrx = s.split(' ')
arrx = list(map(int, arrx))
result = mergesort(arrx)
print(result)