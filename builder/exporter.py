from litemapy import Region, Schematic, BlockState


def export_region(region, filename, name="Atlas Export"):
    schematic = Schematic(
        name=name,
        lm_version=4,
        lm_subversion=0
    )

    schematic.regions["main"] = region

    print("Blocks in region:", region.count_blocks())

    schematic.save(filename)

    print(f"Saved {filename}")