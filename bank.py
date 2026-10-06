


class Bank:
    bank_name='SBI'
    IFSCC_Code=12345678
    Branch='Indore'
    def __init__(self,name,ACC_NO,cid,__bankBalance,__password):
        self.name=name
        self.ACC_NO=ACC_NO
        self.id=cid
        self.__bankBalance=__bankBalance
        self.__password=__password

    def Bank_info(self):
        print('Bank_name =',self.bank_name)
        print('IFSCC code =',self.IFSCC_Code)
        print('Branch =',self.Branch)
        print('Name =',self.name)
        print('ACC_NO =',self.ACC_NO)
        print('Id =',self.id)
        print('--------------------------------\n')


    def Balance_enquiry(self):
        print('you current balance is =',self.__bankBalance)
        print('----------------------------------------------\n')


    def Deposit(self):
        amount=float(input('Enter Depositing anount'))
        if amount>0:
            self.__bankBalance += amount
            print('Deposited Balance is =',amount)
            print('-------------------------------------\n')
            self.Balance_enquiry()

        else:
            print('Invalid Balance')
    

    def Withdraw(self):
        amount=float(input('Enter Withdrawl anount ='))
        if self.__bankBalance >=amount and amount >0:
            self.__bankBalance -=amount
            print('Withdrawl Balance is =',amount)
            print('-------------------------------------\n')
            self.Balance_enquiry()
        else:
            print('Insufficient Balance ')
    

    def match_password(self):
        limit=3
        while limit >0:
            password=input(f'limit={limit}, enter the password')
            if password == self.__password:
                return True
            else:
                limit-=1
                print('Invalid Password. please try again.')
        

        
# on created Local database
c1=Bank('aman',1,1,1234.5,'aman@123')
c2=Bank('anshuman',2,2,1234.5,'anshuman@123')




# Bank class object call by methord
def mathord(obj):
    while True:
        print('-------------------------------------\n')
        print('1 for Bank Information')
        print('2 for Bank Balance Enquiry')
        print('3 for Bank Deposit ')
        print('4 for Withdraw')
        print('5 for Exit')
        choise=int(input('Enter the Choise'))
        print('-------------------------------------\n')
        match (choise):
            case 1:
                obj.Bank_info()
            case 2:
                obj.Balance_enquiry()
            case 3:
                obj.Deposit()
            case 4:
                obj.Withdraw()
            case 5:
                print('Thank you for Banking with Us')
                break

Cst_data=[c1,c2]


def login(list_of_customer):
    limit=3
    is_id_matched=False
    is_password_matched=False
    while limit>0:
        id=int(input(f'limit={limit}, enter the Id'))
        for customer in list_of_customer:
            if id == customer.id:
                is_id_matched=True
                if customer.match_password():
                    is_password_matched=True
                    mathord(customer)
                    break
                else:
                    print('Invalid Password')
        if not is_id_matched:
            limit-=1
            print('Invalid id. please try again.')
        if is_password_matched:
            break

                

def signup():
    name=input('enter the name ')
    ACC_NO=int(input('enter the account number '))
    cid=int(input('enter the id number '))
    bankBalance=float(input('enter the bank Balance '))
    password=input('enter the password ')

    new_customer=Bank(name,ACC_NO,cid,bankBalance,password)

    print(' Your Account is created')

    return new_customer



def display(list_of_customer):
    print('1 : Signup')
    print('2 : Login')
    print('3 : Exit')
    choise=int(input('Enter the Choise'))
    match (choise):
        case 1 :
            list_of_customer.append(signup())
            display(list_of_customer)
        case 2:
            login(list_of_customer)
        case 3:
            print('thank you for banking with us')

    print('-----------------------------')


display(Cst_data)


