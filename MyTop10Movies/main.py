# Python program to find sum of array
# elements using recursion.

# Return sum of elements in A[0..N-1]
# using recursion.
def _findSum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + _findSum(arr[1:])
#         Chops the first element of the array off and passes it to the next iteration
#         making [1, 2, 3, 4, 5] into [2, 3, 4, 5]

# driver code
arr = []
# input values to list
arr = [1, 2, 3, 4, 5]

# calculating length of array
N = len(arr)

ans = _findSum(arr)
print(ans)

# This code is contributed by Khare Ishita