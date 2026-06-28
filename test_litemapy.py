from litemapy import Region, Schematic, BlockState
import inspect

print("REGION INIT")
print(inspect.signature(Region))

print()

print("SCHEMATIC INIT")
print(inspect.signature(Schematic))

print()

print("SETBLOCK")
print(inspect.signature(Region.setblock))

print()

print("SAVE")
print(inspect.signature(Schematic.save))

print()

print("BLOCKSTATE")
print(inspect.signature(BlockState))