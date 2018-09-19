import random

print('What is your character\'s name?')
name = input()
print('What class is your character?')
chr_class = input()
print('You have 100 points total. How many would you like to dedicate to magic?\
        The remainder will be your attack points.')
print('Magic: ')
mgc = input()
atk = abs(int(mgc)-100)
print('Ok ' + name + ', you are a ' + chr_class + ' with ' \
+ str(mgc) + ' magic points and ' + str(atk) + ' attack points!')

#while (int(mgc) > 0) == True:
#    print('you have', str(mgc), 'mp')
#    int(mgc) -= random.randint(1,10)

def cast_spell():
        while (mgc > 0) == True:
            int(mgc) -= random.randint(1,10)
            print('You cast your spell and have', str(mgc), 'mp remaining.')

print('Try casting a spell! Type: Cast spell')
print('You currently have', str(mgc) + 'mp.', 'and', str(atk) + 'hp.')
