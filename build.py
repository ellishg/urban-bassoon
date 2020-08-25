#!/usr/bin/env python

import yaml
import os


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
    def __init__(self, recipe):
        self.title = recipe["title"]
        self.description = recipe["description"]
        self.ingredients = [
            Ingredient(ingredient) for ingredient in recipe["ingredients"]
        ]
        self.directions = recipe["directions"]
        self.tags = recipe["tags"] if "tags" in recipe else None
        self.images = recipe["images"] if "images" in recipe else None
        assert self.is_valid()

    def is_valid(self):
        return all(
            [isinstance(self.title, str), isinstance(self.description, str),]
            + [isinstance(direction, str) for direction in self.directions]
            + ([isinstance(tag, str) for tag in self.tags] if self.tags else [])
            + ([isinstance(image, str) for image in self.images] if self.images else [])
        )


def get_recipe_info(recipe_filename):
    with open(os.path.join("recipes", recipe_filename)) as file:
        recipe = Recipe(yaml.safe_load(file))
    return {
        "title": recipe.title,
        "filename": recipe_filename,
        **({"tags": recipe.tags} if recipe.tags else {}),
    }


recipe_list = [get_recipe_info(filename) for filename in sorted(os.listdir("recipes"))]

with open("recipe-list.yaml", "w") as file:
    file.write(yaml.safe_dump(recipe_list))
