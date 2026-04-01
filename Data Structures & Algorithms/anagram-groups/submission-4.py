from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_string = defaultdict(list)
        for string in strs:
            hash_char = {}
            for char in string:
                hash_char[char] = hash_char.get(char,0)+1

            key = tuple(sorted(hash_char.items()))

            hash_string[key].append(string)

        result = list(hash_string.values())

        return result

            

            

        