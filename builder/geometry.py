from .structure import Structure


def draw_rectangle(structure: Structure,
                   x: int,
                   y: int,
                   z: int,
                   width: int,
                   length: int,
                   block):

    for dx in range(width):
        for dz in range(length):
            structure.set_block(
                x + dx,
                y,
                z + dz,
                block
            )


def draw_hollow_rectangle(structure: Structure,
                          x: int,
                          y: int,
                          z: int,
                          width: int,
                          length: int,
                          block):

    for dx in range(width):
        structure.set_block(x + dx, y, z, block)
        structure.set_block(x + dx, y, z + length - 1, block)

    for dz in range(length):
        structure.set_block(x, y, z + dz, block)
        structure.set_block(x + width - 1, y, z + dz, block)