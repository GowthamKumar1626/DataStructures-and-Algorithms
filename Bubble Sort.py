def bubbleSort(arr, length):
	for i in range(length-1):
		for j in range(length-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	print(arr)


n = int(input("Enter no.of Elements:"))
arr = []
for i in range(n):
	ele = int(input("Enter Element:"))
	arr.append(ele)
bubbleSort(arr, n)
