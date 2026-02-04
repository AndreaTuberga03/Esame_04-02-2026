from dataclasses import dataclass

@dataclass
class Authorship:
    object_id: int
    role: str
    artist_id: int

    def __hash__(self):
        return self.object_id

    def __str__(self):
        return self.role

    def __repr__(self):
        return self.role