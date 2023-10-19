import random
import string
lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

length = int(input('Enter the length of your password: '))
medium=input('Select the medium\nEasy,Normal or Hard:').lower()
if medium =='easy':
    password=lower_case+upper_case
elif medium=='normal':
    password=lower_case+upper_case+digits
elif medium=='hard':
    password=lower_case+upper_case+digits+symbols
else:
    print('Please first select the medium between Easy,Normal or Hard')
    exit


if length<1:
    print('Length should se greater than 1')
else:
    generated_password=' '.join(random.choices(password,k=length)) 
    print(f'The Generated Password is {generated_password}')
