
class account (object):
    def __init__(self,balance):
        self.balance=balance or {}

user=account("10000")
myint=10000
abc=input("please enter your account number: ")
print("scanning......")
print("validating...")
print("validating information....")
print("account accesed..")
print("wating for serverip to respond....")
print("done")
print("error pin requried............> error code(#7703240569459375680359068)")
print("")
print("")
print("")
cba=input("please enter your pin number: ")
print("")
print("")
print("")
print("press 1 for cash withdrawl")
print("press 2 for balance")
print("press 3 to see your account no.")
print("press 4 to see pin number")
gda=input(":")

if(gda=="1"):
    amu=int(input("enter amount: "))    
    print("please take the money below :)")
    print("your balance remaning= |>")
    print(myint-amu)

elif(gda=="2"):
    print(user.balance)

elif(gda=="3"):
    print(abc)

elif(gda=="4"):
    print(cba)    

print("thanks for using our atm.")