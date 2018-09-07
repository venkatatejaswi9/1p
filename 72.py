a=raw_input()
b=['a','e','i','o','u','A','E','I','O','U']
flag=0
for i in a:
	if i in b:
		flag=1
	else:
		flag=0
if(flag==1):
	print "yes"
else:
	print "no"
