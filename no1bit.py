class Solution:
    def hammingWeight(self, n: int) -> int:
         s=str(bin(n)[2:])
         c=0
         for i in s:
            if i=="1":
                c+=1
         return c
	
        
        
           
                 
            
                