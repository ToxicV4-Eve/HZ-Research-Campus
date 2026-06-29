"""
MCEdit (.schematic) exporter.

Target:
    Minecraft 1.12.2
    WorldEdit 6.x
"""

from pathlib import Path

from nbtlib import (
    File,
    ByteArray,
    Compound,
    Int,
    List,
    Short,
    String,
)


class MCEditExporter:
    """
    Exports Atlas regions to the classic
    WorldEdit / MCEdit .schematic format.
    """

    def __init__(self):
        pass

    def export_empty(
        self,
        filename: str,
        width: int,
        height: int,
        length: int,
    ):
        size = width * height * length

        schematic = File(
            {
                "Width": Short(width),
                "Height": Short(height),
                "Length": Short(length),

                "Materials": String("Alpha"),

                "Blocks": ByteArray([0] * size),
                "Data": ByteArray([0] * size),

                "Entities": List[Compound]([]),
                "TileEntities": List[Compound]([]),

                "WEOffsetX": Int(0),
                "WEOffsetY": Int(0),
                "WEOffsetZ": Int(0),

                "WEOriginX": Int(0),
                "WEOriginY": Int(0),
                "WEOriginZ": Int(0),
            },
            root_name="Schematic",
        )

        schematic.save(Path(filename), gzipped=True)

        print(f"Saved {filename}")