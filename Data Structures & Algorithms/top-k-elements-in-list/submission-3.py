class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1

        result = []
        for _ in range(k):
            max_freq = -1
            max_key = None
            for key ,count in freq.items():
                if count > max_freq:
                    max_freq = count
                    max_key = key

            result.append(max_key)

            freq.pop(max_key)


        return result


            
            



        