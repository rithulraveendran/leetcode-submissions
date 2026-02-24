class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        max_freq = 0
        freq={}
        val = -1
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
                if freq[num] > max_freq:
                    max_freq = freq[num]
                    val = num
                elif freq[num] == max_freq:
                    if val == -1 or num < val:
                        val = num       
        return val

