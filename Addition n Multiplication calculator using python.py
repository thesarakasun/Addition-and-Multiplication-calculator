ans=0
asd=1
print("\n a)Addition \n b)Multiplication \n \n ")
p=input("Which operation would you like to proceed(Ex: b) ?")
q=int(input("How many operators are there? "))
if(p=="a"):
    for i in range(1,q+1):
        m=int(input("Enter number " + str(i) + "?"))
        ans=ans+m
    print("\n Answer is : ",ans)
elif(p=="b"):
    for i in range(1,q+1):
        d=int(input("Enter number " + str(i) + "?"))
        asd=asd*d
    print("\nAnswer is : ",asd)
print("\n\n\nThank you for using this calculator")
print("thesara.one")
input("\n*Press ENTER to exit")
