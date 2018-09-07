m=raw_input()
n=['a','e','i','o','u','A','E','I','O','U']
flag=0
for i in m:
	if i in n:
		flag=1
	else:
		flag=0
if(flag==1):
	print "yes"
else:
	print "no"
