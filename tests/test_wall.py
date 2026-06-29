from litemapy import Region

from builder.geometry import wall
from builder.palette import WHITE_CONCRETE

region = Region(0, 0, 0, 20, 10, 20)

wall(
    region,
    x=2,
    y=0,
    z=2,
    length=12,
    height=5,
    direction="north",
    block=WHITE_CONCRETE
)

print("Blocks:", region.count_blocks())