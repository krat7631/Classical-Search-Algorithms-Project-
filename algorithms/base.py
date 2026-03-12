"""Shared constraint options for search algorithms."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchConstraints:
    # None = no limit (unconstrained for that dimension)
    max_depth: Optional[int] = None
    max_expansions: Optional[int] = None
    time_budget_seconds: Optional[float] = None
