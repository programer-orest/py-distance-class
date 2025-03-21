from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self):
        return f'Distance: {self.km} kilometers.'

    def __repr__(self):
        return f'Distance(km={self.km})'

    def __add__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

        return Distance(self.km + other)

    def __iadd__(self, other: Distance | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self

        self.km += other
        return self

    def __mul__(self, other: Distance | int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float | int) -> Distance:
        if isinstance(other, int) and self.km % other == 0:
            return Distance(self.km // other)

        return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km

        return self.km < other

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km

        return self.km == other

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km

        return self.km > other

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km

        return self.km <= other

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km

        return self.km >= other
