from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass
from typing import Any


# User-facing classes
@dataclass
class Filter:
    column: str
    equals: Any | None = None
    between: tuple[Any, Any] | None = None
    values: list[Any] | None = None
    greater_than: Any | None = None
    less_than: Any | None = None


# Internal classes
@dataclass
class _Dimension:
    column: str
    type: str
    values: list[str] | None = None
    original_column: str | None = None
    transform: str | None = None


@dataclass
class _Measure:
    column: str
    type: str
    agg: str


@dataclass(frozen=True)
class Metric:
    id: str
    title: str
    description: str
    x: str
    y: list[str] | str
    chart_type: str
    owner: str | None = None
    prepared_table: str | None = None
    base_table: str | None = None
    query: str | None = None
    agg: str | None = None
    x_label: str | None = None
    y_label: str | None = None
    legend_label: str | None = None
    trace_titles: list[str] | None = None
    date_col: str | None = None
    dimensions: list[_Dimension] | None = None
    measures: list[_Measure] | None = None
    defaults: dict[str, Any] | None = None
    days_back: int = 400  # How many days back to compute the metric

    def __post_init__(self):
        if (
            self.query is None
            and self.prepared_table is None
            and self.base_table is None
        ):
            raise ValueError(
                "Either query or base_table or prepared_table must be provided"
            )

    @classmethod
    def from_dict(cls, data: dict) -> "Metric":
        data = data.copy()
        dimensions = [_Dimension(**dim) for dim in data.pop("dimensions", [])]
        measures = [_Measure(**measure) for measure in data.pop("measures", [])]
        return cls(**data, dimensions=dimensions, measures=measures)

    def get_measure(self, measure: str) -> _Measure:
        if self.measures is None:
            raise ValueError("Measures not set")

        for _measure in self.measures:
            if _measure.column.lower() == measure.lower():
                return _measure
        raise ValueError(f"Measure {measure} not found")

    def get_hash(self) -> str:
        return hashlib.sha256(str(asdict(self)).encode()).hexdigest()

    def to_dict(self) -> dict:
        return asdict(self)
