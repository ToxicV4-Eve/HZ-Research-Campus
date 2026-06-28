from litemapy import BlockState, Region


def rectangle(
    region: Region,
    x: int,
    y: int,
    z: int,
    width: int,
    length: int,
    block: BlockState,
):
    """Fill a solid rectangle."""
    for dx in range(width):
        for dz in range(length):
            region.setblock(x + dx, y, z + dz, block)


def hollow_rectangle(
    region: Region,
    x: int,
    y: int,
    z: int,
    width: int,
    length: int,
    block: BlockState,
):
    """Draw only the border of a rectangle."""

    # Top edge
    rectangle(region, x, y, z, width, 1, block)

    # Bottom edge
    rectangle(region, x, y, z + length - 1, width, 1, block)

    # Left edge
    rectangle(region, x, y, z, 1, length, block)

    # Right edge
    rectangle(region, x + width - 1, y, z, 1, length, block)