class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self._strength = 1
        self._agility = 1
        self._intellect = 1
        self._unit_level = 1
        self.class_unit = ""
        self.extra_characteristic = ""

    @property
    def strength(self):
        return self._strength

    @property
    def agility(self):
        return self._agility

    @property
    def _intelligence(self):
        return self._intellect

    def __repr__(self):
        if self.class_unit == "Mage":
            return f"Class: {self.class_unit}, Name: {self.name}, Clan: {self.clan}, " \
                   f"Health: {self.health}, Intellect: {self._intelligence}," \
                   f"Personal skills level: {self._unit_level}, Extra characteristic: {self.extra_characteristic}"
        if self.class_unit == "Archer":
            return f"Class: {self.class_unit}, Name: {self.name}, Clan: {self.clan}, " \
                   f"Health: {self.health}, Agility: {self._agility},Personal skills level: {self._unit_level}," \
                   f"Extra characteristic: {self.extra_characteristic}"
        if self.class_unit == "Knight":
            return f"Class: {self.class_unit}, Name: {self.name}, Clan: {self.clan}, " \
                   f"Health: {self.health}, Strength: {self._strength},Personal skills level: {self._unit_level}," \
                   f"Extra characteristic: {self.extra_characteristic}"

    def unit_health(self):
        self.health += 10
        if self.health >= 100:
            self.health = 100
        if self.health == 0:
            "Game over"

    def increase_unit_level(self):
        if self.clan == "Mage":
            self._intellect += 1
            if self._intellect >= 10:
                self._intellect = 10
        if self.class_unit == "Archer":
            self._agility += 1
            if self._agility >= 10:
                self._agility = 10
        if self.class_unit == "knight":
            self._strength += 1
            if self._strength >= 10:
                self._strength = 10


class Mage(Unit):
    def __init__(self, name, clan, extra_characteristic):
        super().__init__(name, clan)
        self.name = name
        self.extra_characteristic = extra_characteristic
        self.class_unit = "Mage"

    @property
    def new_level(self):
        self._intellect = self._unit_level
        return self._intelligence


class Archer(Unit):
    def __init__(self, name, clan, extra_characteristic):
        super().__init__(name, clan)
        self.name = name
        self.extra_characteristic = extra_characteristic
        self.class_unit = "Archer"

    @property
    def new_level(self):
        self._agility = self._unit_level
        return self._agility


class Knight(Unit):
    def __init__(self, name, clan, extra_characteristic):
        super().__init__(name, clan)
        self.name = name
        self.extra_characteristic = extra_characteristic
        self.class_unit = "Knight"

    @property
    def new_level(self):
        self._agility = self._unit_level
        return self._strength


Mage_unit = Mage("Dark Mage", "Our dark world", "Fire&Water - 50%, Air - 50%")
Mage_unit.increase_unit_level()
Archer_unit = Archer("BestArcher", "UKR_CLAN", "Bow - 50%, Crossbow - 50%")
Archer_unit.increase_unit_level()
Knight_unit = Knight("Warm Heart", "Peace", "Sword, Ax, Lance")
Knight_unit.increase_unit_level()
Knight_unit.unit_health()
print(Mage_unit)
print(Archer_unit)
print(Knight_unit)
