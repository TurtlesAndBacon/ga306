print('Enter your phone number. All digits please.')
phnum = input()
phlength = len(phnum)

def ten_digit(phnum):
    phlist = list(phnum)
    phlist.insert(0, '(')
    phlist.insert(4, ')')
    phlist.insert(5, ' ')
    phlist.insert(9, '-')
    print(*phlist, sep='')

def ten_digit_2(phnum):
    phlist = list(phnum)
    phlist.insert(3, '-')
    phlist.insert(7, '-')
    print(*phlist, sep='')

def ten_digit_3(phnum):
    phlist = list(phnum)
    phlist[3:3]= ['-']
    phlist[7:7]= ['-']
    print(*phlist, sep='')

def sev_digit(phnum):
    phlist = list(phnum)
    phlist.insert(3, '-')
    print(*phlist, sep='')

def main():
    if phlength == 10:
        ten_digit_3(phnum)
        ten_digit_2(phnum)
        ten_digit(phnum)

    elif phlength == 7:
        sev_digit(phnum)

main()
