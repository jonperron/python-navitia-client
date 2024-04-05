from dataclasses import dataclass

from .base_entity import BaseEntity


@dataclass
class Pathway(BaseEntity):
    is_entrance: bool
    is_exit: bool
    length: int
    traversal_time: int
