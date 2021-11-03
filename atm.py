class atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber= cardnumber
        self.pin= pin

    def CashWithdrawl(self,amount):
        new = 1000000-amount
        print("withdrawl amount ", amount)
        print("balance ",new)

    def BalanceEnquiry(self):
        print("balance 1000000")

def main():
    card = input("card number: ")
    pin = input("pin number: ")
    user = atm(card,pin)
    print("1 balance enquiry")
    print("2 withdrawl")
    no = int(input("enter number"))
    if(no == 1):
        user.BalanceEnquiry()
    elif(no == 2):
        amount = int(input("enter amount"))
        user.CashWithdrawl(amount)

if __name__ == "__main__":
    main()
