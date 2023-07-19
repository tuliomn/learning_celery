from dataclasses import dataclass

@dataclass
class Pokemon:
    id: int
    name: str
    sprite: str
    base_experience: int
    order: int