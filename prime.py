def main():
   b=input("")
   k=0
   for i in range(2,b//2+1):
     if(b%i==0):
        k=k+1
   if(k<=0):
    print("Yes")
   else:
    print("No")
if __name__ == '__main__':
    main()
