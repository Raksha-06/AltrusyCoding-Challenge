prices=[1,4,5,3,2,1,6]
prices=sorted(prices)
money=6
n=len(prices)
l=[]
for i in range(n):
    su=0
    for j in range(i,n):
        su+=prices[j]
        if(su<=money):
            l.append(len(prices[i:j+1]))
print(max(l))
            
