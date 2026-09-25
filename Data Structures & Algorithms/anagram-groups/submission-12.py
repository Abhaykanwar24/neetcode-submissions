class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_set = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] +=1
            
            hash_set[tuple(key)].append(s)

        
        return list(hash_set.values())