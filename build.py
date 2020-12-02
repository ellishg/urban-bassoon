#!/usr/bin/env python3

import sys
from pathlib import Path
import json, yaml


class Ingredient(dict):
    def __init__(self, data):
        dict.__init__(
            self,
            **{
                key: value
                for key, value in data.items()
                if key in ["name", "amount", "unit"]
            },
        )
        assert self.is_valid(), f"{data} does not conform to Ingredient"

    def is_valid(self):
        return all(
            [
                isinstance(self["name"], str),
                isinstance(self["amount"], int) or isinstance(self["amount"], float),
                isinstance(self["unit"], str) if "unit" in self else True,
            ]
        )


class Recipe(dict):
    def __init__(self, data, filename):
        # TODO: Assert filename has no spaces and is url-safe.
        self.filename = filename
        data.setdefault("tags", [])
        data.setdefault("images", [])
        dict.__init__(
            self,
            ingredients=[Ingredient(ingredient) for ingredient in data["ingredients"]],
            **{
                key: value
                for key, value in data.items()
                if key
                in ["title", "description", "directions", "tags", "images", "authors"]
            },
        )
        assert self.is_valid(), f"{data} does not conform to Recipe"

    def is_valid(self):
        return all(
            [isinstance(self["title"], str), isinstance(self["description"], str),]
            + [isinstance(direction, str) for direction in self["directions"]]
            + ([isinstance(tag, str) for tag in self["tags"]] if "tags" in self else [])
            + (
                [isinstance(image, str) for image in self["images"]]
                if "images" in self
                else []
            )
            + (
                [isinstance(author, str) for author in self["authors"]]
                if "authors" in self
                else []
            )
        )

    def get_recipe_info(self):
        return {
            "title": self["title"],
            "filename": self.filename,
            "tags": self["tags"],
        }

    @staticmethod
    def load(path):
        with path.open() as file:
            return Recipe(yaml.safe_load(file), path.stem)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [output_path|--dry-run]")
        exit(1)

    project_root = Path(__file__).resolve().parent

    recipes = [
        Recipe.load(path) for path in sorted(project_root.joinpath("recipes").iterdir())
    ]

    recipe_list = [recipe.get_recipe_info() for recipe in recipes]

    with project_root.joinpath("unit-conversions.yaml").open() as file:
        unit_conversions = yaml.safe_load(file)

    if sys.argv[1] != "--dry-run":

        output_path = Path(sys.argv[1]).resolve()
        output_path.mkdir(exist_ok=True)

        with output_path.joinpath("recipe-list.json").open("w") as file:
            json.dump(recipe_list, file)

        with output_path.joinpath("unit-conversions.json").open("w") as file:
            json.dump(unit_conversions, file)

        for recipe in recipes:
            with output_path.joinpath(recipe.filename + ".json").open("w") as file:
                json.dump(recipe, file)
