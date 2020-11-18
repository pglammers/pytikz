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


# # default fill color for this package
# DEFAULT_FILL_COLOR = "yellow"
