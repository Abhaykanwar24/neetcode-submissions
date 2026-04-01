class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] +=1

        reversed_d = defaultdict(list)
        for num, freq in count.items():
            reversed_d[freq].append(num)

        print(reversed_d)
        values = list(count.values())
        res = []
        max_v = 0
        check = 0
        
        for i in range(k):
            max_v = max(values)          # reset each time
            values.remove(max_v)
            res.extend(reversed_d[max_v])
        

        return res
        
        
        