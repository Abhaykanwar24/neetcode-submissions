from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)  # Get frequency of s1 characters
        s1_set = set(s1)  # Set for quick lookup

    # Step 1: Transform s2, replacing chars not in s1 with '0'
        transformed = [char if char in s1_set else '0' for char in s2]

    # Step 2: Extract continuous segments by splitting on '0'
        segments = ''.join(transformed).split('0')

    # Step 3: Check if any segment has the exact frequency match as s1
        for segment in segments:
            if Counter(segment) == s1_count:  # Frequency must match exactly
                return True

        return False

        


        