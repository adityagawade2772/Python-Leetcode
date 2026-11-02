class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        a = self.optimal(fruits)
        return a
    def bruit(self, fruits):
        n= len(fruits)
        maxi = 0
        for i in range(0,n):  
            myset = set()
            for j in range(i,n):
                if fruits[j] not in myset:
                    myset.add(fruits[j])
                if len(myset)>2:
                    break
                
                maxi =max(maxi,j-i+1)
        return maxi

    def optimal(self, fruits):
        l= 0
        r=0
        maxi = 0
        n = len(fruits)
        mydict = {}
        while r< n:
            mydict[fruits[r]]= mydict.get(fruits[r],0)+1
            if len(mydict)>2:
                mydict[fruits[l]] -=1
                if mydict[fruits[l]] == 0:
                    del mydict[fruits[l]]
                l +=1
            maxi = max(maxi, r-l+1)
            r+=1
        return maxi
        

        