m=int(raw_input())
n=raw_input().split()
for i in range(m):
	for j in range(n):
		if(int(n[i])<int(n[j])):
			temp=n[i]
			n[i]=n[j]
			n[j]=temp
for i in range(m):
	print n[i],
