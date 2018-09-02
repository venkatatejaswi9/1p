m=int(input())
b=''
while(m!=0):
	t=m%10
	if t%2!=0:
            b=b+' '+str(t)
	m=m//10
print(b[::-1])
