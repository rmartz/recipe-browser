from django.urls import reverse

from rest_framework.test import APITestCase

from recipes.models import Recipe, Ingredient


class RecipeManagerTestCase(APITestCase):
    def test_recipe_list_empty(self):
        url = reverse('recipes-list')
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_nonempty(self):
        recipe = Recipe.objects.create(label="Test recipe")

        url = reverse('recipes-list')
        response = self.client.get(url)

        self.assertEqual(response.json(), [{'id': recipe.id,
                                            'ingredients': [],
                                            'label': recipe.label}])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_with_ingredient(self):
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        url = '{}?ingredients={}'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(response.json(), [{'id': recipe.id,
                                            'ingredients': [ingredient.id],
                                            'label': recipe.label}])
        self.assertEqual(response.status_code, 200)

    def test_recipe_manager__missing_ingredient(self):
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        url = '{}?ingredients=-1'.format(reverse('recipes-list'))
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)
