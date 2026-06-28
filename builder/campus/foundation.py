from litemapy import Region, BlockState


def build_foundation():
    region = Region(0, 0, 0, 64, 1, 64)

    concrete = BlockState("minecraft:white_concrete")

    for x in range(64):
        for z in range(64):
            region[x, 0, z] = concrete

    return region