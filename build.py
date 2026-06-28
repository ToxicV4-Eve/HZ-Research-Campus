from litemapy import Region, BlockState
from builder.exporter import export_region

print("Generating first litematic...")

region = Region(0, 0, 0, 9, 1, 9)

white = BlockState("minecraft:white_concrete")

for x in range(9):
    for z in range(9):
        region.setblock(x, 0, z, white)

export_region(
    region,
    "output/first_platform.litematic",
    "First Platform"
)

print("Done!")