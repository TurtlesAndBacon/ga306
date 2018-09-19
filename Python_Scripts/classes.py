class AddressBookEntry():
    pass

me = AddressBookEntry()
you = AddressBookEntry()
me.name = 'Jake'
me.phone = '208-870-7006'
you.name = 'Justin'
you.phone = '503-555-1234'
print(me.name, me.phone)
print(you.name, you.phone)

def __init__(self, name, phone):
    self.name = name
    self.phone = phone
