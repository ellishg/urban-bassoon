#!/usr/bin/env python

import sys
from pathlib import Path
import json, yaml


class Ingredient:
    def __init__(self, ingredient):
        self.name = ingredient["name"]
        self.amount = ingredient["amount"]
        self.unit = ingredient["unit"] if "unit" in ingredient else None
        assert self.is_valid()

    def is_valid(self):
        return all(
            [
                isinstance(self.name, str),
                isinstance(self.amount, float) or isinstance(self.amount, int),
            ]
            + ([isinstance(self.unit, str)] if self.unit else [])
        )


class Recipe:
    def __init__(self, recipe, filename):
        self.filename = filename
        self.title = recipe["title"]
        self.description = recipe["description"]
        self.ingredients = [
            Ingredient(ingredient) for ingredient in recipe["ingredients"]
        ]
        self.directions = recipe["directions"]
        self.tags = recipe["tags"] if "tags" in recipe else []
        self.images = recipe["images"] if "images" in recipe else None
        assert self.is_valid()

    def is_valid(self):
        return all(
            [isinstance(self.title, str), isinstance(self.description, str),]
            + [isinstance(direction, str) for direction in self.directions]
            + ([isinstance(tag, str) for tag in self.tags] if self.tags else [])
            + ([isinstance(image, str) for image in self.images] if self.images else [])
        )

    def get_recipe_info(self):
        return {
            "title": self.title,
            "filename": self.filename,
            "tags": self.tags,
        }

    @staticmethod
    def load(path):
        with path.open() as file:
            return Recipe(yaml.safe_load(file), path.name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [output_path|--dry-run]")
        exit(1)

    project_root = Path(__file__).resolve().parent

    recipes = [
        Recipe.load(path) for path in sorted(project_root.joinpath("recipes").iterdir())
    ]

    recipe_list = [recipe.get_recipe_info() for recipe in recipes]

    if sys.argv[1] != "--dry-run":

        output_path = Path(sys.argv[1]).resolve()
        output_path.mkdir(exist_ok=True)

        with output_path.joinpath("recipe-list.json").open("w") as file:
            json.dump(recipe_list, file)
