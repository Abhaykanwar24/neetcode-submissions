class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_String = ""
        for s in strs:
            encode_String += str(len(s)) + "#" + s
        return encode_String

    def decode(self, s: str) -> List[str]:
        decode_string = []
        c = 0 
        while c < len(s):
            i = c
            while s[i] != "#":
                i +=1
            length = int(s[c:i])
            c = i + 1
            i = c + length
            decode_string.append(s[c:i])
            c = i 
        return decode_string
