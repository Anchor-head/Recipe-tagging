# Recipe tagging system: what does it do?

The purpose of this project is to build a website that allows you to search recipes using a fine-grained multi-tag system that would allow you to filter recipes by multiple criteria simultaneously (e.g. "high protein", "vegan" AND "less than X grams of sugar").

Surprisingly, such a service does not yet exist as far as I know.

## Current progress

So far, I have only made a script (extract.py) that scrapes all recipes from Allrecipes.com and stores them in a json file along with some of their details (cooking time, prep time, yield, etc.).

## Next steps

1. Extract ingredient information from recipes to add to database
2. Extract nutritional information from ingredient information for nutrient-related tagging
3. Develop a search-by-tag system
4. Expand recipe selection by scraping more websites
5. Integrate an AI agent to produce meal plan recommendations according to user specifications