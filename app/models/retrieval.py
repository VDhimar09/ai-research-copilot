from dataclasses import dataclass


@dataclass
class RetrievalResult:
    source: str
    content: str
    score: float
    matched_words: list[str]