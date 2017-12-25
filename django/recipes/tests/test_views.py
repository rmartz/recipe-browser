from django.urls import reverse

from rest_framework.test import APITestCase

from recipes.models import Recipe, Ingredient


class RecipeApiTestCase(APITestCase):
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

    def test_recipe_list__limit_to__with_ingredient(self):
        """Check that limit_to includes recipes with ingredients."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        url = '{}?limit_to={}'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(response.json(), [{'id': recipe.id,
                                            'ingredients': [ingredient.id],
                                            'label': recipe.label}])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__missing_ingredient(self):
        """Check that limit_to excludes recipes with missing ingredinets."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        url = '{}?limit_to=-1'.format(reverse('recipes-list'))
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__no_ingredients(self):
        """Check that recipes with no ingredients match limit_to filter."""
        recipe = Recipe.objects.create(label="Test recipe")

        url = '{}?limit_to=-1'.format(
            reverse('recipes-list'))
        response = self.client.get(url)

        self.assertEqual(response.json(), [{'id': recipe.id,
                                            'ingredients': [],
                                            'label': recipe.label}])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__with_multi(self):
        """Assert that limit_to properly handles ingredient list."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        url = '{}?limit_to={},-1'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(response.json(), [{'id': recipe.id,
                                            'ingredients': [ingredient.id],
                                            'label': recipe.label}])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__has_ingredient__missing(self):
        """Assert that has_ingredient excludes recipes without ingredient."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        Recipe.objects.create(label="Test recipe")

        url = '{}?has_ingredient={}'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__has_ingredient__present(self):
        """Assert that has_ingredient returns recipes with ingredient."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        recipe.ingredients.add(ingredient)

        url = '{}?has_ingredient={}'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(response.json(), [{'id': recipe.id,
                                            'ingredients': [ingredient.id],
                                            'label': recipe.label}])
        self.assertEqual(response.status_code, 200)
