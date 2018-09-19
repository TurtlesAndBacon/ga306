import random
randomNum = random.randint(0,8)
print('What is your name?')
name = input()

fortunes = [
    ', you have been cursed with male-pattern baldness.',
    ', you have been cursed to always think there is one more stair.',
    ', you have been cursed to always step in water after putting on fresh socks.',
    ', you have been cursed to always get the squeaky shopping cart.',
    ', you have been cursed to always sit at wobbly tables.',
    ', you have been cursed to always sit in the front row at the movies.',
    ', you have been cursed to always be behind a slow driver.',
    ', you have been cursed to always lose a book just before finishing it.',
    ', you have been cursed to only have access to dial-up internet.',
]
print(name + fortunes[randomNum])
