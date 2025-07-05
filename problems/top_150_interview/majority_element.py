from collections import Counter

def majorityElement(nums: List[int]) -> int:
    count = Counter(nums)
    n = len(nums) // 2
    print(count)
    for num, cnt in count.items():
        if cnt > n:
            return num

# using the Counter method can be more efficient because it organizes the counts in a single pass, 
# in a dictionary-like structure. 