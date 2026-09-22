class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #start the array off as all zero inputs and the same length as the temperatures array
        stack = [] #contains pairs, the temp and its index [temp,index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #stack isnt empty AND the temp we are at in the loop is greater than the temp on the top of the stack. [-1] = top of stack, [0] first element of the pair.
                stackT, stackInd = stack.pop() #save both the temp and the index
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        
        return res

