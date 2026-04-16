class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            start_index = j + 1
            end_index = start_index + length

            res.append(s[start_index:end_index])

            i = end_index

        return res
