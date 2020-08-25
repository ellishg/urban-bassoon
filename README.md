# urban-bassoon
A database of food recipes.

[![Build Status](https://travis-ci.org/ellishg/urban-bassoon.svg?branch=main)](https://travis-ci.org/ellishg/urban-bassoon)

## Add Recipe
To add a recipe, create a new `.yaml` file in the `recipes/` directory and rebuild the `recipe-list.yaml` file using `build.py`.

```bash
python build.py
```

## Verify Recipes
You will need to install `yamllint` at [https://github.com/adrienverge/yamllint](https://github.com/adrienverge/yamllint) to lint the recipes.

```bash
yamllint .
```

## Images
All images should formatted as a `.jpg` with no `EXIF`, `XMP`, or `IPTC` metadata, and be saved to the `images` directory.
