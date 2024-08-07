#User function Template for python3
#Question link
#https://www.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides (self, N):
        # code here
        number=str(N) #converted to string
        count=0
        for i in number:
            d=int(i)    #convert string back to int
            if d!=0 and  N % d == 0 :
                count+=1
                
        return count
    


