def get_name():
    name = input()
    return name

def get_class():
    chr_class = input()
    return chr_class

def get_mgc():
    mgc = input()
    return mgc

def get_atk():
    atk = abs(int(mgc)-100)
    return atk

def main():
    print('What is your character\'s name?')
    get_name()
    print('What class is your character?')
    get_class()
    print('You have 100 points total. How many would you like to dedicate to magic?\
            The remainder will be your attack points.')
    get_points()
    print('Ok', get_name, 'you are a', get_class, 'with', \
    str(mgc), 'magic points and', str(atk), 'attack points!')

main()
