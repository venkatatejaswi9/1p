b=int(input())
rev=0
while(b>0):
  rem=b%10
  rev=rev*10+rem
  b=b//10
print(rev)
