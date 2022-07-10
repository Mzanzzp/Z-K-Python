class Pracownik:
    def __init__(self, name, rate_per_hour):
        self.name = name
        self.rate_per_hour = rate_per_hour

    def register_time(self, hour):
        self.hour = hour

    def pay_salary(self):
        if self.hour < 8:
            to_pay = self.rate_per_hour * self.hour
        else:
            to_pay = self.rate_per_hour * 8 + (self.hour - 8) * (self.rate_per_hour + 100)
        self.hour = 0
        return to_pay


class Bonus:
    def __init__(self, value):
        self.value = value


class ValueBonus(Bonus):
    order = 2

    def calculate(self, to_pay: int):
        return to_pay + self.value


class PercentBonus(Bonus):
    order = 1

    def calculate(self, to_pay: int):
        return to_pay + (to_pay * self.value / 100)


class PremiumEmployee(Pracownik):
    def __init__(self, name, rate_per_hour):
        super().__init__(name, rate_per_hour)
        self.bonuses = {}

    def pay_salary(self):
        to_pay = super().pay_salary()

        for bonus in sorted(self.bonuses.values(), key=lambda x: x.order):
            to_pay = bonus.calculate(to_pay)

        return to_pay

    def give_bonus(self, bonus: Bonus):
        if bonus.__class__ in self.bonuses:
            self.bonuses[bonus.__class__] += bonus
        else:
            self.bonuses[bonus.__class__] = bonus



