from dataclasses import dataclass, field
from typing import List

@dataclass
class World:
    day: int = 1
    events: List[str] = field(default_factory=list)
