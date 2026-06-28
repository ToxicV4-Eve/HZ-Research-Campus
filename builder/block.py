from dataclasses import dataclass

@dataclass(frozen=True)
class Block:
    name: str