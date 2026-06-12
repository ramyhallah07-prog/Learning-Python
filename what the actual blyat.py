from itertools import zip_longest
class Category:
    def __init__(self, name = ''):
        self.name = name
        self.ledger = []
        self.withdrawls = []
    def deposit(self, amount, description = ''):
        self.amount = amount
        self.description = description

        self.ledger.append({'amount': self.amount, 'description': self.description})

    def withdraw(self, amount, description = ''):
        self.amount = amount
        self.description = description

        if self.check_funds(self.amount):
            self.ledger.append({'amount': -self.amount, 'description': self.description})
            self.withdrawls.append(self.amount)
            return True
        return False
    def get_balance(self):
        return sum(self.ledger[a]['amount'] for a in range(len(self.ledger)))
    
    def transfer(self, amount, category):
        self.amount = amount
        self.category = category

        if self.check_funds(self.amount):
            self.category.deposit(self.amount, f'Transfer from {self.name}')
            self.withdraw(self.amount, f'Transfer to {self.category.name}')
            return True
        return False
    def check_funds(self, amount):

        self.amount = amount

        current_balance = self.get_balance()

        if current_balance >= self.amount and self.amount > 0:
            return True
        return False
    
    def __str__(self):

        if len(self.name) > 30:
            self.name = '***'+self.name[:21] + '...***'       
        line = 30-len(self.name)
        if line % 2 == 0:
            left = line//2
            right = line//2
        else:
            left = line//2
            right = line//2 + 1
        result = f'{"*"*left}{self.name}{"*"*right}\n'
        for item in self.ledger:
            if len(item['description']) + len(str(item['amount'])) < 30:
                result += f'{item["description"]}{" " * (27 - len(item["description"]) - len(str(item["amount"])))}{item["amount"]:.2f}\n'
            elif len(item['description']) + len(str(item['amount'])) >= 30:
                end_discription = 30 - len(str(item['amount'])) - 8 
                result += f'{item["description"][:end_discription]}{"...  "}{item["amount"]:.2f}\n' + 'Total: ' + f'{self.get_balance():.2f}\n' + f'{"*"*30}'
        return result.rstrip()

def create_spend_chart(*categories):
    print('Percentage spent by category \n')
    total_spent = 0
    for category in categories:
        total_spent += sum(total for total in category.withdrawls)
    i = 110
    for _ in range(11):
        i -= 10
        print(f'{i:3d}|', end = '')
        for category in categories:
            percentage = (sum(category.withdrawls) / total_spent) * 100
            if percentage >= i:
                print(f'{" "}{"o":3s}', end = '')
            else:
                print(f'{" "}{" ":3s}', end = '')
        print()
    print('    ' + len(categories)*'----')
    names = [category.name for category in categories]
    for row in zip_longest(*names, fillvalue=' '):
        print(' '*5 + (3*' ').join(row))
        
    
    
    
    





















bourse = Category('Bourse')
samy = Category('Samy BLYAAAAT')
saber = Category('Saber')
zahra = Category('Zahra')
saber.deposit(1000, 'Saber')
saber.withdraw(100, 'GYM SUUKA')
bourse.deposit(200, 'Bob')
bourse.deposit(100, 'Zahra')
bourse.deposit(99, 'Younes')
bourse.deposit(1, 'Younes')
#print(bourse.get_balance())
print(bourse.withdraw(25, 'GYM SUUKA'))
#print(bourse.get_balance())
#print(bourse.withdraw(1000))
#print(bourse.get_balance())
print(bourse.transfer(100, samy))
print(bourse.get_balance())
print(samy.get_balance())
samy.withdraw(25, 'GYM SUUKA')
#print(samy)
#print(bourse)
zahra.deposit(1000, 'Zahra')
zahra.withdraw(100, 'GYM SUUKA')
create_spend_chart(samy, bourse, saber, zahra)


print(samy)

'''
test = [{'bob' : 10}, {'bob' : 1000}, {'bob' : 101}]
bobs_amount = 0
for t in test:
    results = t['bob']
print(results)
'''