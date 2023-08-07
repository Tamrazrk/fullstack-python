class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated!")
        if amount <= 0:
            raise Exception("amount should be positive!")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Not authenticated!")
        if amount <= 0:
            raise Exception("amount should be positive!")
        if self.balance < amount:
            raise Exception("not enough money")
        self.balance -= amount

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount <= self.minimum_balance:
            raise Exception("remaining balance is lower than minimum balance limit")
        super().withdraw(amount)


class ATM:
    def __init__(self, account_list, try_limit):
        # validate and initialize accounts_list
        for account in account_list:
            if not (
                isinstance(account, BankAccount)
                or isinstance(account, MinimumBalanceAccount)
            ):
                raise Exception("not valid account")

        self.account_list = account_list

        # validate and initialize try_limit
        try:
            if try_limit <= 0:
                raise Exception("try limit must be positive")
            self.try_limit = try_limit
        except:
            self.try_limit = 2

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            try:
                choice = int(input("[1] Log in | [2] Exit  -- input 1 or 2: "))
                if choice not in [1, 2]:
                    raise Exception("invalid choice")
            except:
                print("invalid input")
                continue

            if choice == 1:
                username = input("username: ")
                password = input("password: ")
                self.log_in(username, password)
            else:
                # in case of exit cancel the loop
                return

    def log_in(self, username, password):
        self.current_tries = 1
        while self.current_tries < self.try_limit:
            for account in self.account_list:
                account.authenticate(username, password)
                if account.authenticated:
                    self.show_account_menu(account)
                    # after session reset authenticated
                    account.authenticated = False
                    return

            print("invalid credentials, try again...")
            username = input("username: ")
            password = input("password: ")
            self.current_tries += 1

        print("you reached max tries limit")

    def show_account_menu(self, account):
        while True:
            try:
                choice = int(
                    input("[1] deposit | [2] withdraw | [3] exit -- input 1, 2 or 3: ")
                )
                if choice not in [1, 2, 3]:
                    raise Exception("invalid choice")
            except:
                print("invalid input")
                continue

            if choice == 1:
                amount = int(input("amount: "))
                account.deposit(amount)
            elif choice == 2:
                amount = int(input("amount: "))
                account.withdraw(amount)
            else:
                return


if __name__ == "__main__":
    atm = ATM(
        account_list=[
            BankAccount(1000000, "Tamar", "rich"),
            MinimumBalanceAccount(500, "Mark", "poor", 100),
        ],
        try_limit=3,
    )
