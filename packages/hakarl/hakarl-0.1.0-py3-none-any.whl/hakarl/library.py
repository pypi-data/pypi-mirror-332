from pathlib import Path

from hakarl.models import Recipe
from hakarl.parsing import Parser, ParsingError
from hakarl.rendering import Renderer
from hakarl.slugify import slugify


class Library:
    def __init__(self, library_path: Path) -> None:
        self._library_dir = library_path

        if not self._library_dir.exists():
            self._library_dir.mkdir(parents=True)

        self._recipes: dict[str, Recipe] = {}
        self._renderer = Renderer()
        self._load_recipes()

    def _load_recipes(self) -> None:
        parser = Parser()

        for recipe_file in self._library_dir.glob("*.rcp"):
            slug = recipe_file.stem
            content = recipe_file.read_text(encoding="utf-8")

            try:
                self._recipes[slug] = parser.parse_recipe(content)
            except ParsingError as e:
                print(f"Skipping {recipe_file}: Failed to parse ({e})")

    def recipe_exists(self, slug: str) -> bool:
        return slug in self._recipes

    def list_recipes(self) -> list[tuple[str, Recipe]]:
        return list(self._recipes.items())

    def get_recipe(self, slug: str) -> Recipe:
        return self._recipes[slug]

    def create_recipe(self, recipe: Recipe) -> str:
        title = recipe.title if recipe.title else "Untitled"
        slug = slugify(title)
        counter = 1

        while slug in self._recipes or (self._library_dir / f"{slug}.rcp").exists():
            slug = f"{slug}-{counter}"
            counter += 1

        content = self._renderer.render_recipe(recipe)
        self._recipes[slug] = recipe
        recipe_path = self._library_dir / f"{slug}.rcp"
        recipe_path.write_text(content, encoding="utf-8")

        return slug

    def update_recipe(self, slug: str, recipe: Recipe) -> None:
        if slug in self._recipes and self._recipes[slug] == recipe:
            return

        recipe_text = self._renderer.render_recipe(recipe)
        self._recipes[slug] = recipe
        recipe_path = self._library_dir / f"{slug}.rcp"
        recipe_path.write_text(recipe_text, encoding="utf-8")

    def delete_recipe(self, slug: str) -> None:
        if slug not in self._recipes:
            raise ValueError(f"Recipe '{slug}' not found")

        recipe_path = self._library_dir / f"{slug}.rcp"
        if recipe_path.exists():
            recipe_path.unlink()

        del self._recipes[slug]
