import re
from dataclasses import dataclass

from hakarl.models import Section, Step, Ingredient, Recipe, SingleAmount, RangeAmount


MIXED_NUMBER = r"(?:\d+(?:\s+\d+/\d+)?|\d+/\d+)"
RANGE_AMOUNT = fr"(?:{MIXED_NUMBER})-(?:{MIXED_NUMBER})"
UNITS = r"(?:cups?|teaspoons?|tablespoons?|tsp|tbsp|ounces?|pounds?|quarts?|ml|milliliters?|grams?|cans?|each|cloves?|stalks?|bunch|bunches|sprigs?|bags?|pinch|sticks?)"

AMOUNT_REGEX = fr"""
    ^
    (?P<quantity>(?:{MIXED_NUMBER})|(?:{RANGE_AMOUNT}))\s+
    (?P<unit>{UNITS})\s+
    (?:\((?P<alt_quantity>(?:{MIXED_NUMBER})|(?:{RANGE_AMOUNT}))\s+(?P<alt_unit>{UNITS})\)\s+)?
    (?P<name>[^,]+?)
    (?:\s*,\s*(?P<notes>.+))?
    $
"""
AMOUNT_PATTERN = re.compile(AMOUNT_REGEX, re.VERBOSE)

class ParsingError(Exception):
    def __init__(self, message: str, line: int):
        self.message = message
        self.line = line


def _parse_amount(quantity: str, unit: str) -> SingleAmount | RangeAmount:
    if "-" in quantity:
        qmin, qmax = quantity.split("-", 1)
        return RangeAmount(quantity_min=qmin.strip(), quantity_max=qmax.strip(), unit=unit.strip())
    return SingleAmount(quantity=quantity.strip(), unit=unit.strip())


def parse_ingredient(ingredient: str, line_number: int) -> Ingredient:
    if not ingredient.strip():
        raise ParsingError("Empty ingredient", line_number)

    # For ingredients that do not start with a digit, treat them as name (with optional notes)
    if not ingredient[0].isdigit():
        if "," in ingredient:
            name, notes = ingredient.split(",", 1)
            return Ingredient(name=name.strip(), notes=notes.strip())
        return Ingredient(name=ingredient.strip())

    # Attempt to match an ingredient with a quantity and unit
    match = AMOUNT_PATTERN.match(ingredient)
    if match:
        amount = _parse_amount(match.group("quantity"), match.group("unit"))

        alt_amount = None
        if match.group("alt_quantity"):
            alt_amount = _parse_amount(match.group("alt_quantity"), match.group("alt_unit"))

        return Ingredient(
            name=match.group("name").strip(),
            amount=amount,
            alt_amount=alt_amount,
            notes=match.group("notes").strip() if match.group("notes") else None,
        )

    raise ParsingError("Invalid ingredient format", line_number)


@dataclass
class Block:
    type: str
    text: str
    line: int


class Parser:
    def __init__(self) -> None:
        self._blocks: list[Block] = []
        self._current_block: Block | None = None

    def _pop_block(self) -> Block:
        block = self._blocks.pop(0)
        self._current_block = self._blocks[0] if self._blocks else None
        return block

    def parse_recipe(self, text: str) -> Recipe:
        meta, text = self._parse_meta(text)

        self._blocks = self._parse_blocks(text, len(meta) + 3)
        self._current_block = self._blocks[0] if self._blocks else None

        if self._current_block is None:
            raise ParsingError("No content to parse", 0)

        if self._current_block.type != "title":
            raise ParsingError(
                f"Expected title, got {self._current_block.type}", self._current_block.line
            )

        if self._current_block.text == "" and len(self._blocks) > 1:
            raise ParsingError("Title cannot be empty", self._current_block.line)

        title = self._pop_block().text
        description = self._parse_description()
        sections = self._parse_sections()

        return Recipe(slug="", title=title, description=description, sections=sections, meta=meta)

    def _parse_meta(self, text: str) -> tuple[dict[str, str], str]:
        meta = {}
        if text.startswith("---"):
            lines = text.splitlines()
            lines = lines[1:]
            while lines[0] != "---":
                key, value = lines[0].split(": ", 1)
                meta[key] = value
                lines = lines[1:]
            text = "\n".join(lines[1:])
        return meta, text.strip()

    def _parse_description(self) -> str | None:
        if self._current_block is not None and self._current_block.type == "description":
            if self._current_block.text == "" and len(self._blocks) > 1:
                raise ParsingError("Description cannot be empty", self._current_block.line)
            return self._pop_block().text
        return None

    def _parse_sections(self) -> list[Section]:
        sections = []
        while self._current_block is not None:
            if self._current_block.type not in ("subtitle", "step"):
                raise ParsingError(
                    f"Expected subtitle or step, got {self._current_block.type}", self._current_block.line
                )
            section_title = None
            if self._current_block.type == "subtitle":
                section_title = self._pop_block().text
            steps = self._parse_steps()
            sections.append(Section(section_title, steps))
        return sections

    def _parse_steps(self) -> list[Step]:
        steps = []
        while self._current_block is not None and self._current_block.type != "subtitle":
            if self._current_block.type != "step":
                raise ParsingError(
                    f"Expected step, got {self._current_block.type}", self._current_block.line
                )
            step_block = self._pop_block()
            paragraphs = [step_block.text]

            while self._current_block is not None and self._current_block.type == "paragraph":
                paragraphs.append(self._pop_block().text)

            ingredients = []
            while self._current_block is not None and self._current_block.type == "ingredient":
                block = self._pop_block()
                ingredient = parse_ingredient(block.text, block.line)
                ingredients.append(ingredient)

            steps.append(Step(paragraphs, ingredients))
        return steps

    @staticmethod
    def _parse_blocks(text: str, line_offset: int) -> list[Block]:
        blocks = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if not stripped:
                continue

            if stripped.startswith("*"):
                blocks.append(Block("ingredient", stripped[1:].strip(), line_number + line_offset))
            elif stripped.startswith(">"):
                blocks.append(Block("description", stripped[1:].strip(), line_number + line_offset))
            elif stripped.startswith("+"):
                blocks.append(Block("subtitle", stripped[2:].strip(), line_number + line_offset))
            elif stripped.startswith("="):
                blocks.append(Block("title", stripped[1:].strip(), line_number + line_offset))
            elif stripped.startswith("#"):
                blocks.append(Block("step", stripped[1:].strip(), line_number + line_offset))
            else:
                blocks.append(Block("paragraph", stripped, line_number + line_offset))
        return blocks
