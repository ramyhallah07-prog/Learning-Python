import string
from random import choices
class PasswordManager:
    def __init__(self):
        pass
    
    def password_generator(self, lenth, lower = 0, upper = 0, nums = 0, spetial_char = 0):
        self.char = string.ascii_letters
        self.char_low = string.ascii_lowercase
        self.char_up = string.ascii_uppercase
        self.num = string.digits
        self.spetials = string.punctuation
        _password = []
        if lower:
            _password.extend(choices(self.char_low, k= lower))
        if upper:
            _password.extend(choices(self.char_up, k= upper))
        if nums:
            _password.extend(choices(self.num, k= nums))
        if spetial_char:
            _password.extend(choices(self.spetials, k= spetial_char))
        if (not upper or upper ==0 and not lower and not nums and not spetial_char) or lenth < 8:
            _password.extend(choices(self.char, k= lenth))
            print('WARNING : weak password')
        password = choices(_password, k = lenth)
        if len(password) < lenth:
            password.extend(choices(self.char+self.num+self.spetials, k = (lenth - len(password))))
        for i in password:
            print(i, end = '')
        return password

pm = PasswordManager()
lenth, lower, upper, nums, spetial_char = int(input('lenth of the password: ')), int(input("lowercase number: ")), int(input("uppercase number: ")), int(input("digits number: ")), int(input("spetial characters number: "))
pm.password_generator(lenth, lower, upper, nums, spetial_char)