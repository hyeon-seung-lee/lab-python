class Account:
    """은행 계좌 클래스
    field(데이터): 계좌번호(accountno), 잔고(balance)
    method(기능): 입금(deposit)-> self.sum, 출금(withdraw)->self.sum, 이체(transfer) -> other(상대방 account 객체 자체), self.sum(금액)
    """

    def __init__(self, accountno, balance=0):
        self.money = 0
        self.accountno = accountno
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        self.money = money
        return f'after deposit {self.money}, my balance is {self.balance}\n'

    def withdraw(self, money):
        self.balance -= money
        self.money = money
        return f'after withdraw{self.money}, my balance is {self.balance}\n'

    def transfer(self, other, money):
        self.balance -= money
        self.money = money
        other.balance += money
        return f'After transfering {self.money} to other is completed, my balance is {self.balance} and \n other balance is {other.balance}'

    def __str__(self):
        return f'my accountno : {self.accountno}, my balance : {self.balance}'

    def __eq__(self, other):
        return self.accountno == other.accountno


if __name__ == '__main__':
    user1 = Account(100, 10000)
    user2 = Account(200, 20000)

    print(user1)
    print(user1.deposit(100))
    print(user1.withdraw(1000))
    print(user1.transfer(user2, 2000))
