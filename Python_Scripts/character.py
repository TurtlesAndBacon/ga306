#Character Dictionary
character01 = {}

# Program introduces itself
print('Hello, I\'m NONDESCRIPT GAME!', '\n'
        'Let\'s get started with your first character.', '\n'
        'What is your character\'s name?''\n')

char_name = input()

character01['Name'] = char_name

print('\n''Ok,', char_name, '. What type of character are you?''\n')

char_type = input()

character01['Class'] = char_type

print('\n''Ah, a \"mighty\"', char_type + '. How many hit points do you have?''\n')

hit_points = input()

character01['HP'] = hit_points

print('\n''Sure, fine. How many magic points do you have?''\n')

magic_points = input()

character01['MP'] = magic_points

print('\n'
      'That\'ll work, I suppose.', '\n'
      'Here are your chosen stats:''\n')

print(character01)
print('\n'
      'Is this correct?''\n')

answer = input()

if answer=='Yes':
    print('\n'+'Sweet.')


else:
    while True:
        print('What would you like to change?')
        change_request = input()
        if change_request=='Name':
            print('Then enter a new one.''\n')
            char_name = input()
            character01['Name'] = char_name
            print('Here are your chosen stats:''\n')
            print(character01)
            print('\n'
                  'Is this correct?''\n')

            answer = input()

            if answer=='Yes':
                print('\n'+'Sweet.')
            else:
                break
        elif change_request=='Class':
            print('Then enter a new one.''\n')
            char_type = input()
            character01['Class'] = char_type
            print('Here are your chosen stats:''\n')
            print(character01)
            print('\n'
                  'Is this correct?''\n')

            answer = input()

            if answer=='Yes':
                print('\n'+'Sweet.')
            else:
                break
        elif change_request=='HP':
            print('Then enter a different number.''\n')
            hit_points = input()
            character01['HP'] = hit_points
            print('\n''Here are your chosen stats:''\n')
            print(character01)
            print('\n'
                  'Is this correct?''\n')

            answer = input()

            if answer=='Yes':
                print('\n'+'Sweet.')
            else:
                break
        elif change_request=='MP':
            print('Then enter a different number.''\n')
            magic_points = input()
            character01['MP'] = magic_points
            print('Here are your chosen stats:''\n')
            print(character01)
            print('\n'
                  'Is this correct?''\n')

            answer = input()

            if answer=='Yes':
                print('\n'+'Sweet.')
            else:
                break
