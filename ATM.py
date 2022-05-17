class Atm:
    def __init__(self,balanceEnquiry,amountWithdrawal,cashDeposit,transferCash):
        self.balanceEnquiry=balanceEnquiry
        self.amountWithdrawal=amountWithdrawal
        self.cashDeposit=cashDeposit
        self.transferCash=transferCash

    def checkBalance(self):
        print("Your Balance is ",self.balanceEnquiry)

    def withdrawAmount(self,amount):
        print("The amount you have withdrawn till date is",self.balanceEnquiry-amount)
        
    def cashDepositing(self,amount):
        print("You have deposited ",self.balanceEnquiry+amount," till date")
       
    
    def transferrCash(self):
        print("You have transferred ",self.transferCash," till date.")
        
balanceEnquiry=0
amountWithdrawal=0
cashDeposit=0
transferCash=0

user1=Atm(balanceEnquiry,amountWithdrawal,cashDeposit,transferCash)
chooseAnOption=int(input("Enter 1 for balance enquiry,2 for amount Withdrawal,3 for cash deposit and 4 for cash transfer."))

if(chooseAnOption==1):
    user1.checkBalance()

elif(chooseAnOption==2):
   
    withdrawalreq=int(input("Enter the amount you wish to withdraw."))
    user1.withdrawAmount(withdrawalreq)
    print("Amount withdrawed")

elif(chooseAnOption==3):
    
    depositrequest=int(input("Enter the amount you wish to deposit."))
    user1.cashDepositing(depositrequest)
    balanceEnquiry=(balanceEnquiry-depositrequest)
    
    print("Amount Deposited!")

elif(chooseAnOption==4):
    user1.transferrCash()
        
   
    print("Amount Transferred")

else:
    print("Wrong Input")

