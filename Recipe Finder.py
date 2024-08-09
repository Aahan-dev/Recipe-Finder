class RecipeFinder:
    def __init__(self):
        """Initialize the Recipe Finder with a predefined set of recipes."""
        self.recipes = {
            "Pasta": ["pasta", "tomato sauce", "cheese"],
            "Salad": ["lettuce", "tomato", "cucumber", "olive oil"],
            "Omelette": ["eggs", "cheese", "pepper", "onion"],
            "Smoothie": ["banana", "yogurt", "milk", "honey"],
            "Stir Fry": ["chicken", "vegetables", "soy sauce", "rice"]
        }

    def find_recipes(self, ingredients):
        """
        Find recipes that can be made with the given ingredients.

        Args:
            ingredients (list): A list of ingredients the user has.

        Returns:
            list: A list of recipe names that can be made with the available ingredients.
        """
        available_recipes = []
        for recipe, recipe_ingredients in self.recipes.items():
            # Check if all ingredients for the recipe are in the user's ingredients
            if all(ingredient in ingredients for ingredient in recipe_ingredients):
                available_recipes.append(recipe)
        return available_recipes

    