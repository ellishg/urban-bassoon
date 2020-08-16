# urban-bassoon
A database of recipes.

[![Build Status](https://travis-ci.org/ellishg/urban-bassoon.svg?branch=main)](https://travis-ci.org/ellishg/urban-bassoon)

## Add Recipe
To add a recipe, create a new `.yaml` file in the `recipes/` directory and add the recipe name to `recipe-list.yaml`.

## Verify Recipes
You will need to install `yamllint` at [https://github.com/adrienverge/yamllint](https://github.com/adrienverge/yamllint) to verify the recipes.

```bash
yamllint recipe-list.yaml
yamllint recipes/
```