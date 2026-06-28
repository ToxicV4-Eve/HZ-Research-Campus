from litemapy import Region, BlockState


def build_main_hub():
    # Overall build area (large enough for future expansion)
    region = Region(0, 0, 0, 41, 1, 41)

    white = BlockState("minecraft:white_concrete")

    # -----------------------
    # Main Hub (31x31)
    # -----------------------

    for x in range(5, 36):
        for z in range(5, 36):
            region[x, 0, z] = white

    # -----------------------
    # North Corridor
    # -----------------------

    for x in range(18, 23):
        for z in range(0, 5):
            region[x, 0, z] = white

    # -----------------------
    # South Corridor
    # -----------------------

    for x in range(18, 23):
        for z in range(36, 41):
            region[x, 0, z] = white

    # -----------------------
    # West Corridor
    # -----------------------

    for x in range(0, 5):
        for z in range(18, 23):
            region[x, 0, z] = white

    # -----------------------
    # East Corridor
    # -----------------------

    for x in range(36, 41):
        for z in range(18, 23):
            region[x, 0, z] = white

    return region