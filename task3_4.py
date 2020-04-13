import re

pattern = '\d+'
regex = re.compile('[@_!#$&]') 

while True:
    print('Enter your password')
    pwd = input('>')
    pwdLength = len(pwd)
    if pwdLength < 8:
        print('Your password length must be up to 8 characters:')
        continue
        
    if re.findall(pattern, pwd) == []:
        print('Your password must contain one or more figures')
        continue
    
    if regex.search(pwd) == None:
        print('Your password must contain any of these characters $ # & _ ! @')
        continue

    print('Your password is ', pwd)
    break
print('Password valid')