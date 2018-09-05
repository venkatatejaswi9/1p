n=int(raw_input())
m=raw_input().split()
num=int(m[0])
for i in range(1,n):
	if(num<int(m[i])):
		num=int(m[i])
print num
