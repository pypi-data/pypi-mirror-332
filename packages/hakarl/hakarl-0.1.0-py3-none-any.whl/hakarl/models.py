from dataclasses import dataclass, field


@dataclass
class Amount:
    unit: str


@dataclass
class SingleAmount(Amount):
    quantity: str


@dataclass
class RangeAmount(Amount):
    quantity_min: str
    quantity_max: str


@dataclass
class Ingredient:
    name: str
    amount: SingleAmount | RangeAmount | None = None
    alt_amount: SingleAmount | RangeAmount | None = None
    notes: str | None = None


@dataclass
class Step:
    paragraphs: list[str]
    ingredients: list[Ingredient] | None


@dataclass
class Section:
    title: str | None
    steps: list[Step]


@dataclass
class Recipe:
    slug: str
    title: str
    description: str | None
    sections: list[Section]
    meta: dict[str, str] = field(default_factory=dict)
