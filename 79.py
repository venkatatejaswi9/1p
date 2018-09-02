a=int(raw_input())
b=int(raw_input())
c=a*b
r=0
for i in range(2,c):
  if(c==(i*i)):
    r=r+1
if(r==1):
  print "yes"
else:
  print"no"
