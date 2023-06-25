#nested if statement
n=int(input("Enter the number:"))
if(n>=0):
   if(n==0):
       print("Zero is neither positive nor negative")
   else: 
       print(n,"is positive")
else:    
    print(n,"is negative")
