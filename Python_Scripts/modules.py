class Player:
    def __init__(self, name, job, hp, mp, ap):
        self.name = name
        self.job = job
        self.hp = hp
        self.mp = mp
        self.ap = ap

    def update_hp(hp, update_value):
        hp = hp + update_value
        return hp
