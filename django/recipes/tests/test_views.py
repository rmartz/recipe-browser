from __future__ import unicode_literals

from django.urls import reverse

from rest_framework.test import APITestCase

from recipes.models import Recipe, Ingredient, RecipeIngredient


class RecipeApiTestCase(APITestCase):
    def test_recipe_list_empty(self):
        url = reverse('recipes-list')
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_nonempty(self):
        recipe = Recipe.objects.create(label="Test recipe")
        ingredient = Ingredient.objects.create(label="Test ingredient")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)

        url = reverse('recipes-list')
        response = self.client.get(url)

        self.assertEqual(response.json(), [
            {'id': recipe.id,
             'label': recipe.label,
             'ingredients': [
                {'id': ingredient.id,
                 'label': ingredient.label,
                 'is_trivial': ingredient.is_trivial,
                 'optional': False,
                 'quantity': ''}]
             }])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__with_ingredient(self):
        """limit_to includes recipes with ingredients."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)

        url = '{}?limit_to={}'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], recipe.id)
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__missing_ingredient(self):
        """limit_to excludes recipes with missing required ingredients."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)

        url = '{}?limit_to=-1'.format(reverse('recipes-list'))
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__missing_optional_ingredient(self):
        """limit_to does not exclude optional ingredients."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=ingredient,
                                        optional=True)

        url = '{}?limit_to=-1'.format(
            reverse('recipes-list'))
        response = self.client.get(url)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], recipe.id)
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__mix_optional_required_ingredient(self):
        """limit_to matches recipes with unmatched optional ingredients."""
        recipe = Recipe.objects.create(label="Test recipe")
        optional = Ingredient.objects.create(label="Optional ingredient")
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=optional,
                                        optional=True)
        required = Ingredient.objects.create(label="Required ingredient")
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=required,
                                        optional=False)

        url = '{}?limit_to={}'.format(
            reverse('recipes-list'),
            required.id)
        response = self.client.get(url)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], recipe.id)
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__no_ingredients(self):
        """recipes with no ingredients match limit_to filter."""
        recipe = Recipe.objects.create(label="Test recipe")

        url = '{}?limit_to='.format(
            reverse('recipes-list'))
        response = self.client.get(url)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], recipe.id)
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__limit_to__with_multi(self):
        """limit_to properly handles ingredient list."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)

        url = '{}?limit_to={},-1'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], recipe.id)
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__has_ingredient__missing(self):
        """has_ingredient excludes recipes without ingredient."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        Recipe.objects.create(label="Test recipe")

        url = '{}?has_ingredient={}'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_recipe_list__has_ingredient__present(self):
        """has_ingredient returns recipes with ingredient."""
        ingredient = Ingredient.objects.create(label="Test ingredient")
        recipe = Recipe.objects.create(label="Test recipe")
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)

        url = '{}?has_ingredient={}'.format(
            reverse('recipes-list'),
            ingredient.id)
        response = self.client.get(url)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], recipe.id)
        self.assertEqual(response.status_code, 200)


class IngredientApiTestCase(APITestCase):
    def test_ingredient_list_empty(self):
        url = reverse('ingredients-list')
        response = self.client.get(url)

        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_ingredient_list_nonempty(self):
        ingredient = Ingredient.objects.create(label="Test ingredient")

        url = reverse('ingredients-list')
        response = self.client.get(url)

        self.assertEqual(response.json(), [
            {'id': ingredient.id,
             'label': ingredient.label,
             'parent': ingredient.parent,
             'is_trivial': ingredient.is_trivial,
             'weight': 0
             }])
        self.assertEqual(response.status_code, 200)

    def test_suggest_with_excludes_ingredients(self):
        """Ingredients are not suggested for themselves."""
        ingredient = Ingredient.objects.create(label='Test ingredient')
        recipe = Recipe.objects.create(label='Test recipe')
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient)

        url = '{}?suggest_with={}'.format(
            reverse('ingredients-list'),
            ingredient.id)
        response = self.client.get(url)

        # We should have received zero ingredients back
        self.assertEqual(len(response.json()), 0)
        self.assertEqual(response.status_code, 200)

    def test_suggest_with_shared_ingredients(self):
        """Shared ingredients are suggested."""
        starting_ingredient = Ingredient.objects.create(label='Input')
        shared_ingredient = Ingredient.objects.create(label='Shared')
        recipe = Recipe.objects.create(label='Test recipe')
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=starting_ingredient)
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=shared_ingredient)

        url = '{}?suggest_with={}'.format(
            reverse('ingredients-list'),
            starting_ingredient.id)
        response = self.client.get(url)

        # We should have one suggested ingredient
        self.assertEqual(len(response.json()), 1)
        result_ingredient = response.json()[0]
        # It should be the shared ingredient
        self.assertEqual(result_ingredient['id'], shared_ingredient.id)
        # It should have a weight of 1, from the shared recipe
        self.assertEqual(result_ingredient['weight'], 1)
        self.assertEqual(response.status_code, 200)

    def test_suggest_with_weighted_by_shared_ingredients(self):
        """Suggested ingredients are weighted by number of connections."""
        starting_ingredient1 = Ingredient.objects.create(label='Input1')
        starting_ingredient2 = Ingredient.objects.create(label='Input2')
        shared_ingredient = Ingredient.objects.create(label='Shared')
        recipe = Recipe.objects.create(label='Test recipe')
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=starting_ingredient1)
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=starting_ingredient2)
        RecipeIngredient.objects.create(recipe=recipe,
                                        ingredient=shared_ingredient)

        url = '{}?suggest_with={},{}'.format(
            reverse('ingredients-list'),
            starting_ingredient1.id, starting_ingredient2.id)
        response = self.client.get(url)

        # We should have one suggested ingredient
        self.assertEqual(len(response.json()), 1)
        result_ingredient = response.json()[0]
        # It should be the shared ingredient
        self.assertEqual(result_ingredient['id'], shared_ingredient.id)
        # It should have a weight of 1, from the shared recipe
        self.assertEqual(result_ingredient['weight'], 2)
        self.assertEqual(response.status_code, 200)

    def test_suggest_with_weighted_by_shared_recipes(self):
        """Suggested ingredients are weighted by number of matching recipes."""
        starting_ingredient = Ingredient.objects.create(label='Input1')
        shared_ingredient = Ingredient.objects.create(label='Shared')
        recipe1 = Recipe.objects.create(label='Test recipe 1')
        RecipeIngredient.objects.create(recipe=recipe1,
                                        ingredient=starting_ingredient)
        RecipeIngredient.objects.create(recipe=recipe1,
                                        ingredient=shared_ingredient)
        recipe2 = Recipe.objects.create(label='Test recipe 2')
        RecipeIngredient.objects.create(recipe=recipe2,
                                        ingredient=starting_ingredient)
        RecipeIngredient.objects.create(recipe=recipe2,
                                        ingredient=shared_ingredient)

        url = '{}?suggest_with={}'.format(
            reverse('ingredients-list'),
            starting_ingredient.id)
        response = self.client.get(url)

        # We should have one suggested ingredient
        self.assertEqual(len(response.json()), 1)
        result_ingredient = response.json()[0]
        # It should be the shared ingredient
        self.assertEqual(result_ingredient['id'], shared_ingredient.id)
        # It should have a weight of 1, from the shared recipe
        self.assertEqual(result_ingredient['weight'], 2)
        self.assertEqual(response.status_code, 200)
