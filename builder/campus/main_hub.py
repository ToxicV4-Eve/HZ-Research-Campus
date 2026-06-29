from builder.geometry import rectangle, wall
from builder.palette import WHITE_CONCRETE
from litemapy import Region


def build_main_hub():
    
    # Overall build area (large enough for future expansion)
    region = Region(0, 0, 0, 41, 6, 41)

    white = WHITE_CONCRETE

    # -------------------------
    # Main Hub floor
    # -------------------------
    rectangle(region, 5, 0, 5, 31, 31, white)

    print("Building north wall...")

    wall(region, 10, 1, 10, 10, 5, "north", white)


    # -------------------------
    # Exterior walls (5 blocks tall)
    # -------------------------
    wall(region, 5, 1, 5, 31, 5, "north", white)
    wall(region, 5, 1, 35, 31, 5, "north", white)

    wall(region, 5, 1, 5, 31, 5, "east", white)
    wall(region, 35, 1, 5, 31, 5, "east", white)

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