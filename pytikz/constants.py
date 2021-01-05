from enum import Enum


class LineWidth(Enum):
    ULTRA_THIN = "ultra thin"
    VERY_THIN = "very thin"
    THIN = "thin"
    SEMITHICK = "semithick"
    THICK = "thick"
    VERY_THICK = "very thick"
    ULTRA_THICK = "ultra thick"


class LineJoin(Enum):
    MITER = "miter"
    BEVEL = "bevel"
    ROUND = "round"


class AnchorPosition(Enum):
    CENTER = "center"
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    NORTH_EAST = "north east"
    NORTH_WEST = "north west"
    SOUTH_EAST = "south east"
    SOUTH_WEST = "south west"


# # default fill color for this package
# DEFAULT_FILL_COLOR = "yellow"
