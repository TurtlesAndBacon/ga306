import random
randomNum = random.randint(0,8)
print('What is your name?')
name = input()

def get_fortune(name):
    if randomNum == 1:
        print(name + ', you have been cursed with male-pattern baldness.')
    if randomNum == 2:
        print(name + ', you have been cursed to always think there is one more stair.')
    if randomNum == 3:
        print(name + ', you have been cursed to always step in water after putting on fresh socks.')
    if randomNum == 4:
        print(name + ', you have been cursed to always get the squeaky shopping cart.')
    if randomNum == 5:
        print(name + ', you have been cursed to always sit at wobbly tables.')
    if randomNum == 6:
        print(name + ', you have been cursed to always sit in the front row at the movies.')
    if randomNum == 7:
        print(name + ', you have been cursed to always be behind a slow driver.')
    if randomNum == 8:
        print(name + ', you have been cursed to always lose a book just before finishing it.')
    if randomNum == 9:
        print(name + ', you have been cursed to only have access to dial-up internet.')

get_fortune(name)
