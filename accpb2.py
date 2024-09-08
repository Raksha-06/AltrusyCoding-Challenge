n = 6
s="ilikesamsung"
d = { "i", "like", "sam", "sung", "samsung", "mobile"} 
l=len(s)
dp=[False]*(n+1)
dp[0]=True
for i in range(0,n+1):
    for j in range(i+1):
        if dp[j] and s[j:i] in d:
            dp[i]=True
            break
if dp:
    print(1)
else:
    print(0)
        
