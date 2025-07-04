nums = [6, 6, 6, 7, 7]
stack = nums
most_common = 0

if len(stack) == 1:
    most_common = stack[0]
else:
    for num in nums:
        if num in stack:
            stack.remove(num)
            if num in nums and num in stack:
                most_common = num
print(stack)
print(most_common)
