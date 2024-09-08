n=100
m=500
for i in range(n,m+1):
      bol=1
      temp=i%10
      g=i//10
      while(g>0):
          q=g%10
          if (temp+1==q or temp-1==q):
              g=g//10
              temp=q
              
          else:
              bol=0
              break
      if bol==1:
         print(i)
