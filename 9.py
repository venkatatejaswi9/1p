a,K=map(int,raw_input().split( ))
a=list(map(int,raw_input().split()))
sum=0
for i in range(0,(K+1)):
	sum=sum+i
	a.append(sum)
print(sum)
