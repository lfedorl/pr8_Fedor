# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random

chars = 'qwertyyuiopasdfghjklzxcvbnmQWERTYYUIOPASDFGHJKLZXCVBNM123456789'
number = input('количество паролей?'+ "\n")
length = input('длина пароля?'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
