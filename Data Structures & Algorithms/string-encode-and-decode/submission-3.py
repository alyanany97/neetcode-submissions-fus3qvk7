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
                j+= 1
            
            length = int(s[i:j]) #includes element at i but excludes element at j
            startPoint = j + 1
            endPoint = startPoint + length

            res.append(s[startPoint:endPoint])

            i = endPoint
        
        return res

