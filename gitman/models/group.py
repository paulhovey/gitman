from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Group:
    """A group with sources."""

    name: str
    members: Optional[List[str]] = field(default_factory=list)

    def __post_init__(self):
        if self.members is None:
            self.members = []

    def __repr__(self):
        return "<group {}>".format(self)

    def __str__(self):
        pattern = "['{n}']"
        return pattern.format(n=self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __lt__(self, other):
        return self.name < other.name
