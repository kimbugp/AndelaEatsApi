import enum


class MealTypes(str, enum.Enum):
    main = "main"
    side = "side"
    protein = "protein"

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class Channels(str, enum.Enum):
    web = "web"
    slack = "slack"
    mobile = "mobile"

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class MealPeriods(str, enum.Enum):
    lunch = "lunch"
    breakfast = "breakfast"

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class OrderStatus(int, enum.Enum):
    booked = 0
    collected = 1
    cancelled = 2

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)
