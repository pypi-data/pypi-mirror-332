from hakarl.models import SingleAmount, RangeAmount, Ingredient, Recipe
from hakarl.util import pretty


class Renderer:
    def render_recipe(self, recipe: Recipe) -> str:
        parts: list[str] = []

        if recipe.meta:
            parts.append("---")
            for key, value in recipe.meta.items():
                parts.append(f"{key}: {value}")
            parts.append("---")
            parts.append("")

        parts.append(f"= {recipe.title}")
        parts.append("")

        if recipe.description:
            parts.append(f"> {recipe.description}")
            parts.append("")

        step_number = 1
        for section in recipe.sections:
            # Section title
            if section.title:
                parts.append(f"+ {section.title}")
                parts.append("")

            for step in section.steps:
                parts.append(f"# {step.paragraphs[0]}")
                parts.append("")
                if len(step.paragraphs) > 1:
                    for paragraph in step.paragraphs[1:]:
                        parts.append(paragraph)
                        parts.append("")

                step_number += 1

                if step.ingredients:
                    for ingredient in step.ingredients:
                        parts.append(self._render_ingredient(ingredient))
                    parts.append("")

        if parts[-1] == "":
            parts.pop()

        return "\n".join(parts)

    def _render_ingredient(self, ingredient: Ingredient) -> str:
        parts = ["* "]

        if not ingredient.amount:
            return f"* {ingredient.name}"

        parts.append(self._render_amount(ingredient.amount))
        parts.append(" ")

        if ingredient.alt_amount:
            parts.append(f"({self._render_amount(ingredient.alt_amount)}) ")

        parts.append(ingredient.name)

        if ingredient.notes:
            parts.append(f", {ingredient.notes}")

        return "".join(parts)

    def _render_amount(self, amount: SingleAmount | RangeAmount) -> str:
        if isinstance(amount, SingleAmount):
            return f"{amount.quantity} {amount.unit}"
        else:
            return f"{amount.quantity_min}-{amount.quantity_max} {amount.unit}"


class TypstRenderer:
    def render_recipe(self, recipe: Recipe) -> str:
        parts: list[str] = []

        parts.extend([
            "#set page(",
            "  paper: \"us-letter\"",
            ")",
            # "#set enum(indent: 0em)",
            # "#set list(indent: 1em)",
            ""
        ])

        parts.append(f"#align(center)[= {recipe.title}]")
        parts.append("")
        parts.append("#v(1cm)")
        parts.append("")

        step_number = 1
        for section in recipe.sections:
            if section.title:
                parts.append(f"== {section.title}\n")

            for step in section.steps:
                parts.append(f"{step_number}. {pretty("\n".join(step.paragraphs))}")
                step_number += 1

                if step.ingredients:
                    parts.append("")
                    for ingredient in step.ingredients:
                        parts.append(self._render_ingredient(ingredient))

                parts.append("")

        return "\n".join(parts).strip()

    def _render_ingredient(self, ingredient: Ingredient) -> str:
        parts = []

        if ingredient.amount:
            parts.append(self._render_amount(ingredient.amount))
            parts.append(" ")

        if ingredient.alt_amount:
            parts.append(f"({self._render_amount(ingredient.alt_amount)}) ")

        parts.append(f"*{ingredient.name}*")

        if ingredient.notes:
            parts.append(f", {ingredient.notes}")

        return f"   - {pretty("".join(parts))}"

    def _render_amount(self, amount: SingleAmount | RangeAmount) -> str:
        if isinstance(amount, SingleAmount):
            return f"{amount.quantity} {amount.unit}"
        return f"{amount.quantity_min}-{amount.quantity_max} {amount.unit}"


