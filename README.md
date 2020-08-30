# urban-bassoon
A database of food recipes used in [https://github.com/ellishg/laughing-potato](https://github.com/ellishg/laughing-potato).

[![Build Status](https://travis-ci.org/ellishg/urban-bassoon.svg?branch=main)](https://travis-ci.org/ellishg/urban-bassoon)

## Recipes
To add a recipe, simply create a new `.yaml` file in the `recipes/` directory with the following scheme.

```yaml
title: The Recipe Title

description: A brief description of the recipe.

# A list of ingredients. The unit is optional, but should be something like grams, cups, tablespoons, etc.
ingredients:
  - name: flour
    amount: 3
    unit: cups

  - name: eggs
    amount: 2

directions:
  - A list of instructions.
  - They describe the steps of the recipe.

# An optional list of tags to help search for this recipe.
tags:
  - dinner
  - cheese

# An optional list of image paths.
images:
  - images/sourdough-bread.jpg
```

## Ingredients
To enable metric/imperial unit conversions for an ingredient, add to the `unit-conversions.yaml` file. For example, the following describes that `1` cup of flour is `136` grams.

```yaml
flour:
  cups: 1
  grams: 136
```

## Verify Files
You will need to install `yamllint` at [https://github.com/adrienverge/yamllint](https://github.com/adrienverge/yamllint) to lint the recipes.

```bash
yamllint .
```

## Images
All images should formatted as a `.jpg` with no `EXIF`, `XMP`, or `IPTC` metadata, and be saved to the `images` directory.
