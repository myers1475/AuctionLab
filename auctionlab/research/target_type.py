from enum import Enum


class TargetType(str, Enum):
    SWING_HIGH = "Swing High"
    SWING_LOW = "Swing Low"

    PREVIOUS_DAY_HIGH = "Previous Day High"
    PREVIOUS_DAY_LOW = "Previous Day Low"

    PREVIOUS_WEEK_HIGH = "Previous Week High"
    PREVIOUS_WEEK_LOW = "Previous Week Low"

    ASIA_HIGH = "Asia High"
    ASIA_LOW = "Asia Low"

    NEW_YORK_HIGH = "New York High"
    NEW_YORK_LOW = "New York Low"

    FVG = "FVG"
    IFVG = "iFVG"