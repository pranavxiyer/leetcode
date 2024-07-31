# prefix:
# given an array of numbers, create a prefix array of the smallest number to the left
# ex:
# input: [5, 9, 2, 6]
# output: [5, 5, 2, 2
def create_prefix_array(arr):
    prefix = []
    smallest = float("inf")
    for num in arr:
        smallest = min(smallest, num)
        prefix.append(smallest)
    return prefix

# postfix:
# given an array of numbers, create a postfix array of the smallest number to the right
# input: [6, 1, 3, 9]
# output: [1, 1, 3, 9]
def create_postfix_array(arr):
    postfix = [0 for i in range(len(arr))]
    smallest = float("inf")
    i = len(arr) - 1
    while i >= 0:
        num = arr[i]
        smallest = min(smallest, num)
        postfix[i] = smallest
        i -= 1
    return postfix