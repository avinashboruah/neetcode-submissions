class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency using a regular dic
        counts={}
        for num in nums:
            counts[num] = counts.get(num,0) +1

        # sort the unique numbers by their count
        sorted_nums=sorted(counts, key=counts.get, reverse=True)

        return sorted_nums[:k]