from builder.campus.main_hub import build_main_hub
from builder.exporter import export_region

print("Generating Main Hub...")

region = build_main_hub()

export_region(
    region,
    "output/main_hub.litematic",
    "Main Hub"
)

print("Done!")