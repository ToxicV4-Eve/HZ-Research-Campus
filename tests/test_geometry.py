from litemapy import Region
from builder.geometry import rectangle, hollow_rectangle
from builder.palette import WHITE_CONCRETE

region = Region(0, 0, 0, 20, 1, 20)

rectangle(region, 2, 0, 2, 5, 5, WHITE_CONCRETE)
hollow_rectangle(region, 10, 0, 2, 7, 7, WHITE_CONCRETE)

print("Blocks:", region.count_blocks())