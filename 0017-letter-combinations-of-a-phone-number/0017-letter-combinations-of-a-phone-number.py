class Solution:
    def solve(self, index, subset,digits,mydict,result):
        if index >= len(digits):
            result.append("".join(subset))
            return
        for ch in mydict[digits[index]]:
            subset.append(ch)
            self.solve(index+1,subset,digits,mydict,result)
            subset.pop()


            
    def letterCombinations(self, digits: str) -> list[str]:
        mydict={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        self.solve(0,[],digits,mydict,result)
        return result
        