import string
from random import choices
import secrets
class PasswordManager:
    def __init__(self):
        self.password_maneger_account = [{'username' : 'admin', 'password' : 'admin'},]
        self.accounts = {}
        self.login = False
        self.user = None
    def login_user(self, username, password):
        for user in self.password_maneger_account:
            if user['username'] == username and user['password'] == password:
                self.login = True
                self.user = username
                return 'Login Successfully'
        return 'Failed to login'
    def create_password_maneger_account(self, username, password):
        self.password_maneger_account.append({'username' : username, 'password' : password})
    def add_account(self, url, username, password):
        if not url in self.accounts:
            self.accounts[url] = [{"User Name: " : username, "Password: " : password}]
        elif url in self.accounts:
            self.accounts[url].append({"User Name: " : username, "Password: " : password})
    def delete_account(self, url, username):
        for i,acc in enumerate(self.accounts[url]):
            if acc['User Name: '] == username:
                del self.accounts[url][i]
   
    @property
    def show_accounts(self):
        if self.login == True:
            return self.accounts
        else:
            raise ValueError('Login Failed')


    def password_generator(self, lenth, lower , upper , nums , spetial_char, addition):
        char = string.ascii_letters
        char_low = string.ascii_lowercase
        char_up = string.ascii_uppercase
        num = string.digits
        spetials = string.punctuation
        additions = addition
        _password = ''
        if lower:
            _password = ''.join(secrets.choice(char_low) for _ in range(lower))
        if upper:
            _password += ''.join(secrets.choice(char_up) for _ in range(upper))
        if nums:
            _password += ''.join(secrets.choice(num) for _ in range(nums))
        if spetial_char:
            _password += ''.join(secrets.choice(spetials) for _ in range(spetial_char))
        password = ''.join(secrets.choice(char+num+spetials) for _ in range(lenth - len(_password))) if len(_password) < lenth else ''.join(secrets.choice(_password) for _ in range(lenth))
        if additions:
            password += additions
        return password
       
    def generate_password(self):
        COMMON_PATTERNS = [
    "1234", "12345", "123456", "123456789",
    "password", "password123", "admin", "admin123",
    "qwerty", "asdfgh", "zxcvbn",
    "letmein", "welcome", "login", "root",
    "abc123", "iloveyou",
    "1111", "0000", "123123"
]
        password_score = 0
        lenth = int(input("Password length: "))
        has_lower = input("do you want lower case? (y/n): ")
        if has_lower == 'y':
            lower = int(input('Lower Case number: '))
            password_score += 10
        elif has_lower == 'n':
            lower = 0
            password_score -= 5
        has_upper = input("do you want upper case? (y/n): ")
        if has_upper == 'y':
            upper = int(input("Upper Case number: "))
            password_score += 10
        elif has_upper == 'n':
            upper = 0
            password_score -= 5
        has_degits = input('Do you want degits? (y/n): ')
        if has_degits == 'y':
            nums = int(input("Degits number: "))
            password_score += 10
        elif has_degits == 'n':
            nums = 0
            password_score -= 5
        has_spetials = input('do you want spetial degits? (y/n): ')
        if has_spetials == 'y':
            spetial_char = int(input("Spetial Characters number: "))
            password_score += 15
        elif has_spetials == 'n':
            spetial_char = 0
            password_score -= 5
        has_addition = input("do you want to add something? (y/n): ")
        if has_addition == 'y':
            addition = input("what's your addition? : ")
            password_score -= 10
        elif has_addition == 'n':
            addition = ''


        password_score += (lower + upper + nums + spetial_char + len(addition)) *2
        if (lower + upper + nums + spetial_char + len(addition)) >= 16 : password_score += 20
        elif (lower + upper + nums + spetial_char + len(addition)) >= 12 : password_score += 10
        if lenth < 8:
            password_score -= 20
        generated_password = self.password_generator(lenth, lower, upper, nums, spetial_char, addition)
        for pattern  in COMMON_PATTERNS:
            if pattern in generated_password:
                password_score -= 30
        if 0 < password_score < 30:
            print('Weak Password!!')
        elif 30 < password_score < 60:
            print("Normal Password")
        elif 60 < password_score < 90:
            print("Strong Password")    
        elif password_score > 90:
            print("Very Strong Password!!")
        return generated_password






























pm = PasswordManager()
pm.create_password_maneger_account('ramy', 'ramy123')
pm.create_password_maneger_account('zahra', 'ramy123')
print(pm.login_user('zahra', 'ramy123'))
# pm = PasswordManager('ramy', 'ramy123')


# generated_password = pm.generate_password()
# print(generated_password)
pm.add_account('www.google.com', 'ramy.uchiha7@gmail.com', 'ramy@2007')
pm.add_account('www.google.com', 'ramy.hallah7@gmail.com', 'ramy@1812')
pm.add_account('www.google.com', 'ramy20074@gmail.com', 'ramy@0402')
pm.add_account('www.github.com', 'ramy.uchiha7@gmail.com', 'zahrablyat')
pm.delete_account('www.google.com', 'ramy20074@gmail.com')
print(pm.show_accounts)


# ramy = PasswordManager()
# ramy.add_account('www.zahra.dz', 'zahrablyat@suka.dz', 'fuckzahra123')
# print(ramy.show_accounts)



