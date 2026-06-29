from builder.exporter_mcedit import MCEditExporter

exporter = MCEditExporter()

exporter.export_empty(
    "output/empty.schematic",
    width=5,
    height=5,
    length=5,
)