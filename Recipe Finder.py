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

    def run(self):
        """Run the recipe finder tool."""
        while True:
            user_input = input("Enter the ingredients you have (comma-separated): ")
            # Split the input string into a list and strip whitespace
            ingredients = [ingredient.strip() for ingredient in user_input.split(",")]




            # Find available recipes
            available_recipes = self.find_recipes(ingredients)




            if available_recipes:
                print("You can make the following recipes:")
                for recipe in available_recipes:
                    print(f"- {recipe}")
            else:
                print("No recipes found with the given ingredients.")




            # Check if the user wants to search again
            repeat = input("Do you want to search for more recipes? (yes/no): ").strip().lower()
            if repeat != 'yes':
                print("Exiting the recipe finder. Goodbye!")
                break




if __name__ == "__main__":
    # Create an instance of RecipeFinder and run it
    recipe_finder = RecipeFinder()
    recipe_finder.run()