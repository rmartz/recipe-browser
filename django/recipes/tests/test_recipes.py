from django.test import TestCase
from recipes.models import Recipe, Ingredient


class RecipeManagerTestCase(TestCase):
    def test_recipe_manager__no_ingredients(self):
        recipe = Recipe.objects.create(label="Test recipe")

        result = Recipe.objects.for_ingredients([])

        self.assertSequenceEqual(result, [recipe])

    def test_recipe_manager__has_ingredient(self):
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        result = Recipe.objects.for_ingredients([ingredient])

        self.assertSequenceEqual(result, [recipe])

    def test_recipe_manager__missing_ingredient(self):
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        result = Recipe.objects.for_ingredients([])

        self.assertSequenceEqual(result, [])
