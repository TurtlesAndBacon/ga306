print('Enter a number between 1 and 99.')

num = int(input())

tens = num // 10
ones = num % 10

if tens == 9:
    tenWrd = 'Ninety'
elif tens == 8:
    tenWrd = 'Eighty'
elif tens == 7:
    tenWrd = 'Seventy'
elif tens == 6:
    tenWrd = 'Sixty'
elif tens == 5:
    tenWrd = 'Fifty'
elif tens == 4:
    tenWrd = 'Forty'
elif tens == 3:
    tenWrd = 'Thirty'
elif tens == 2:
    tenWrd = 'Twenty'
elif tens == 1:
    tenWrd = 'Ten'

if ones == 9:
    oneWrd = 'Nine'
elif ones == 8:
    oneWrd = 'Eight'
elif ones == 7:
    oneWrd = 'Seven'
elif ones == 6:
    oneWrd = 'Six'
elif ones == 5:
    oneWrd = 'Five'
elif ones == 4:
    oneWrd = 'Four'
elif ones == 3:
    oneWrd = 'Three'
elif ones == 2:
    oneWrd = 'Two'
elif ones == 1:
    oneWrd = 'One'

if tens == 0:
    print(oneWrd)
elif ones == 0:
    print(tenWrd)
elif tens == 1:
    if ones == 0:
        print('Ten')
    if ones == 1:
        print('Eleven')
    if ones == 2:
        print('Twelve')
    if ones == 3:
        print('Thirteen')
    if ones == 4:
        print('Fourteen')
    if ones == 5:
        print('Fifteen')
    if ones == 6:
        print('Sixteen')
    if ones == 7:
        print('Seventeen')
    if ones == 8:
        print('Eighteen')
    if ones == 9:
        print('Nineteen')
else:
    print(tenWrd, oneWrd)
