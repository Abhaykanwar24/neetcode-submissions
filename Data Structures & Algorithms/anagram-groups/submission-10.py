class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for s in strs:
            key =[0] * 26
            for c in s:
                key[ord(c) - ord("a")] +=1
            key = tuple(key)

            if key not in hash_map:
                hash_map[key] = []

            hash_map[key].append(s)


        return list(hash_map.values())