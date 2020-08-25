#!/usr/bin/env python

import yaml
import os


class Ingredient:
    def __init__(self, ingredient):
        self.name = ingredient["name"]
        self.amount = ingredient["amount"]
        self.unit = ingredient["unit"] if "unit" in ingredient else None


class Recipe:
    def __init__(self, recipe):
        self.title = recipe["title"]
        self.description = recipe["description"]
        self.ingredients = list(map(Ingredient, recipe["ingredients"]))
        self.directions = recipe["directions"]
        self.tags = recipe["tags"] if "tags" in recipe else None


def get_recipe_info(recipe_filename):
    with open(os.path.join("recipes", recipe_filename)) as file:
        recipe = Recipe(yaml.safe_load(file))
    return {
        "title": recipe.title,
        "filename": recipe_filename,
        **({"tags": recipe.tags} if recipe.tags else {}),
    }


recipe_list = list(map(get_recipe_info, sorted(os.listdir("recipes"))))

with open("recipe-list.yaml", "w") as file:
    file.write(yaml.safe_dump(recipe_list))
