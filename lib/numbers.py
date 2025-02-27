class Number:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return self.value % 2 == 0

    def is_positive(self):
        return self.value > 0


class Numbers:
    def __init__(self, values):
        self.values = [Number(value) for value in values]

    def sum(self):
        return sum(number.value for number in self.values)

    def average(self):
        if not self.values:
            raise ValueError("A lista de números não pode estar vazia.")
        return self.sum() / len(self.values)