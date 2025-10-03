from collections import Counter
from typing import List

def find_lhs(nums: List[int]) -> int:
    """
    Returns the length of the longest harmonious subsequence (LHS) in nums.
    A harmonious subsequence is one where the difference between max and min is exactly 1.
    We count frequencies and for each value x consider freq[x] + freq[x+1].
    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0

    freq = Counter(nums)
    max_len = 0
    for x in freq:
        if x + 1 in freq:
            max_len = max(max_len, freq[x] + freq[x + 1])
    return max_len

# Example usage / quick tests
if __name__ == "__main__":
    examples = [
        ([1,3,2,2,5,2,3,7], 5),  # subsequence [3,2,2,2,3] length 5
        ([1,2,3,4], 2),          # [1,2] or [2,3] or [3,4]
        ([1,1,1,1], 0),          # no pair with diff 1
        ([], 0),
        ([1,2,2,1], 4)
    ]

    for arr, expected in examples:
        res = find_lhs(arr)
        print(f"{arr} -> LHS length = {res} (expected {expected})")
