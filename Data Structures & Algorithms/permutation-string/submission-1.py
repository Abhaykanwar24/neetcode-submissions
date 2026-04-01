from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)  # {'a': 1, 'c': 1, 'd': 1}
        s1_set = set(s1)        # {'a', 'c', 'd'}
        s1_len = len(s1)        # 3
        
        # Early return if s2 is too short
        if len(s2) < s1_len:
            return False
        
        # Step 1: Transform s2 in one pass
        # For "dcda" → "dcda" (no 0s needed as all chars are in s1)
        transformed = ''.join(c if c in s1_set else '0' for c in s2)
        
        # Step 2: Split into segments and check
        # Instead of creating all segments, process them on-the-fly
        current_segment = []
        for char in transformed:
            if char == '0':
                # Check segment if it reaches required length
                if len(current_segment) >= s1_len:
                    segment_str = ''.join(current_segment)
                    if Counter(segment_str) == s1_count:
                        return True
                current_segment = []
            else:
                current_segment.append(char)
        
        # Check final segment
        if len(current_segment) >= s1_len:
            segment_str = ''.join(current_segment)
            if Counter(segment_str) == s1_count:
                return True
                
        return False
        


        