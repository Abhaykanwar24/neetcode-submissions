class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = []
        for i in range(len(strs)):
            sorted_str.append("".join(sorted(strs[i])))
        print(sorted_str)

        res = []
        seen=set()
        for i in range(len(sorted_str)):
            if sorted_str[i] not in seen:
                group = [strs[i]]
                for j in range(i+1 , len(sorted_str)): 
                    if sorted_str[i] == sorted_str[j]:
                        group.append(strs[j])

                res.append(group)
                seen.add(sorted_str[i])

        return res
        
        