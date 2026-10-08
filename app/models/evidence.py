from dataclasses import dataclass


@dataclass
class Evidence:
    source: str
    content: str
    score: float