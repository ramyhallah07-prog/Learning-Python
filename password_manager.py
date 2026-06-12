import string
from random import choices
class PasswordManager:
    def password_generator(lenth, lower = 0, upper = 0, nums = 0, spetial_char = 0):
        char = string.ascii_letters
        char_low = string.ascii_lowercase
        char_up = string.ascii_uppercase
        num = string.digits
        spetials = string.punctuation
        _password = []
        if lower:
            _password.extend(choices(char_low, k= lower))
        if upper:
            _password.extend(choices(char_up, k= upper))
        if nums:
            _password.extend(choices(num, k= nums))
        if spetial_char:
            _password.extend(choices(spetials, k= spetial_char))
        if (not upper and not lower and not nums and not spetial_char) or lenth < 8:
            _password.extend(choices(char, k= lenth))
            print('WARNING : weak password')
        password = choices(_password, k = lenth)
        if len(password) < lenth:
            password.extend(choices(char+num+spetials, k = (lenth - len(password))))
        for i in password:
            print(i, end = '')
        return password
        
    lenth, lower, upper, nums, spetial_char = int(input('lenth of the password: ')), int(input("lowercase number: ")), int(input("uppercase number: ")), int(input("digits number: ")), int(input("spetial characters number: "))
    password_generator(lenth, lower, upper, nums, spetial_char)