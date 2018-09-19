class PlayerEntry:
    def __init__(self, Name, HP, MP, AP, DP):
        self.Name = Name
        self.HP= HP
        self.MP = MP
        self.AP = AP
        self.DP = DP

    def __repr__(self):
        return 'PlayerEntry({!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.Name,
            self.HP,
            self.MP,
            self.AP,
            self.DP
        )
        # return 'Player ' + self.Name

    def update_health(self, damage):
        self.HP -= damage
        # return self.HP

Player01 = PlayerEntry('Varis', 50, '50', '25', '25')

print(Player01)

damage = 10

Player01.update_health(damage)

print(Player01)

print(var1)
