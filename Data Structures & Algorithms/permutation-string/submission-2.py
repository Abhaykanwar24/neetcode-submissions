from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s1_set = set(s1)
        s1_len = len(s1)
        
        if len(s2) < s1_len:
            return False
        
        # Process continuous valid chars with sliding window
        window = []
        for char in s2:
            if char in s1_set:
                window.append(char)
                # When window is big enough, check all possible s1_len segments
                if len(window) >= s1_len:
                    for i in range(len(window) - s1_len + 1):
                        if Counter(window[i:i+s1_len]) == s1_count:
                            return True
            else:
                window = []  # Reset on encountering invalid char
                
        return False
        


        