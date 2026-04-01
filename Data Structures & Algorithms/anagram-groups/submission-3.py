from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = defaultdict(list)
        result = []
        for string in strs:
            c_count = {}
            for char in string:
                c_count[char] = c_count.get(char, 0) + 1

            key = tuple(sorted(c_count.items()))

            count[key].append(string)

        result = list(count.values())
        return result


        