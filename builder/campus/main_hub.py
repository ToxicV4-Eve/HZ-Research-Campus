from builder.geometry import rectangle, hollow_rectangle
from builder.palette import WHITE_CONCRETE
from litemapy import Region


def build_main_hub():
    # Overall build area (large enough for future expansion)
    region = Region(0, 0, 0, 41, 2, 41)

    white = WHITE_CONCRETE

    # -------------------------
    # Main Hub floor
    # -------------------------
    rectangle(region, 5, 0, 5, 31, 31, white)

    # -------------------------
    # Exterior walls
    # -------------------------
    hollow_rectangle(region, 5, 1, 5, 31, 31, white)

    # -------------------------
    # North entrance
    # -------------------------
    rectangle(region, 18, 0, 0, 5, 5, white)

    # -------------------------
    # South entrance
    # -------------------------
    rectangle(region, 18, 0, 36, 5, 5, white)

    # -------------------------
    # West entrance
    # -------------------------
    rectangle(region, 0, 0, 18, 5, 5, white)

    # -------------------------
    # East entrance
    # -------------------------
    rectangle(region, 36, 0, 18, 5, 5, white)

    return region