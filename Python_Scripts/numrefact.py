def get_num():
    num = int(input())
    return num

def get_tens(num):
    tens = num // 10
    return tens

def get_ones(num):
    ones = num % 10
    return ones

def get_tenWrd(tens):
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
    else:
        tenWrd = tens
    return tenWrd

def get_oneWrd(ones):
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
    else:
        oneWrd = ''
    return oneWrd

def get_output(tens, ones, tenWrd, oneWrd):
    if tens == 0:
        output = oneWrd
    elif tens == 1:
        if ones == 1:
            output = 'Eleven'
        elif ones == 2:
            output = 'Twelve'
        elif ones == 3:
            output = 'Thirteen'
        elif ones == 5:
            output = 'Fifteen'
        else:
            output = oneWrd + 'teen'
    else:
        output = tenWrd + ' ' + oneWrd
    print(output)

def main():
    print('Enter a number between 1 and 99.')
    num = get_num()
    tens = get_tens(num)
    ones = get_ones(num)
    tenWrd = get_tenWrd(tens)
    oneWrd = get_oneWrd(ones)
    get_output(tens, ones, tenWrd, oneWrd)

main()
