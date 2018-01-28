key = 2
total = ': '
x = 0
testlist = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890']
message = 'alfred'
length = len(message)
count = ''
print (message)
identify = (index for index,y in enumerate(testlist) if y == message[x])
print(count)
while x <= length:
    for index in identify:
        if message[x] != testlist[0:62]:
            total = total + message[x]
            print (message[x])
            break
        if index == 61:
            total = total + testlist[0]
            print (testlist[0])
            break
        if index == 62:
            total = total + testlist[1]
            print (testlist[1])
            break
        else:
            total = total + testlist[index + key]
            print (testlist[index + key])
            break
    x = x + 1
    print (total)
    
else:
    print (total)
