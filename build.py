from builder.structure import Structure
from builder.palette import WHITE_CONCRETE
from builder.geometry import draw_hollow_rectangle

structure = Structure()

print("Generating room...\n")

draw_hollow_rectangle(
    structure,
    0,
    0,
    0,
    9,
    9,
    WHITE_CONCRETE
)

for z in range(9):

    line = ""

    for x in range(9):

        if structure.get_block(x, 0, z):
            line += "#"
        else:
            line += "."

    print(line)

print()
print(f"{len(structure.blocks)} blocks placed.")