password = input('Enter pass: ')

result = {}

if len(password) >= 8:
    result['length'] = (True)
else:
    result['length'] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result['digits'] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['upper-case'] = uppercase

print(result)

if all(result.values()):
    print("Strong pass")
else:
    print("Weak pass")