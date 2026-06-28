from litemapy import Schematic

schem = Schematic.load("output/first_platform.litematic")

print("Regions:", schem.regions.keys())

for name, region in schem.regions.items():
    print("Region:", name)
    print("Blocks:", region.count_blocks())