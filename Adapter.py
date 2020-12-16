import math


class RoundStick:
    def __init__(self, radius: int):
        self.radius = radius

    def get_radius(self):
        return self.radius


class SquareStick:
    def __init__(self, width: int):
        self.width = width

    def get_width(self):
        return self.width


class RoundHole:
    def __init__(self, radius: int):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, round_stick: RoundStick):
        return self.get_radius() >= round_stick.get_radius()


class SquareStickAdapter:
    def __init__(self, square_stick: SquareStick):
        self.square_stick = square_stick

    def get_radius(self):
        return self.square_stick.get_width() * math.sqrt(2) / 2


hole = RoundHole(5)
round_stick = RoundStick(5)
print(hole.fits(round_stick))

small_stick = SquareStick(5)
large_stick = SquareStick(10)
small_adapter = SquareStickAdapter(small_stick)
large_adapter = SquareStickAdapter(large_stick)

print(hole.fits(small_adapter))
print(hole.fits(large_adapter))