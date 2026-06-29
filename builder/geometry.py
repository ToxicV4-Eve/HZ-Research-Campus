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

def wall(
        region: Region,
        x: int,
        y: int,
        z: int,
        length: int,
        height: int,
        direction: str,
        block: BlockState,
    ):
        """Build a vertical wall.

        direction:
            "north" -> +X
            "south" -> +X
            "east"  -> +Z
            "west"  -> +Z
        """

        if direction.lower() in ("north", "south"):
            for dy in range(height):
                rectangle(
                    region,
                    x,
                    y + dy,
                    z,
                    length,
                    1,
                    block,
                )

        elif direction.lower() in ("east", "west"):
            for dy in range(height):
                rectangle(
                    region,
                    x,
                    y + dy,
                    z,
                    1,
                    length,
                    block,
                )

        else:
            raise ValueError(f"Unknown wall direction: {direction}")