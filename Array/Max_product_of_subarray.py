def maxSubarrayProduct(arr, n):

	result = arr[0]

	for i in range(n):

		mul = arr[i]

		for j in range(i + 1, n):
			result = max(result, mul)
			mul *= arr[j]

		result = max(result, mul)

	return result

# arr = [1, -2, -3, 0, 7, -8, -2]
arr=[1,2,-3,0,-4,-5]
n = len(arr)
print("Maximum Sub array product is", maxSubarrayProduct(arr, n))


