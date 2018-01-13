from django.test import TestCase
from recipes.models import Ingredient


class IngredientManagerTestCase(TestCase):
    def test_include_ancestors_one_ingredient(self):
        ingredient = Ingredient.objects.create(label="Test")

        result = Ingredient.objects.include_ancestors([ingredient.id])

        self.assertQuerysetEqual(result, [repr(ingredient)])

    def test_include_ancestors_includes_ancestors(self):
        ancestor = Ingredient.objects.create(label="Parent")
        descendant = Ingredient.objects.create(label="Child", parent=ancestor)

        result = Ingredient.objects.include_ancestors([descendant.id])

        self.assertQuerysetEqual(result, [repr(ancestor), repr(descendant)],
                                 ordered=False)

    def test_include_ancestors_detects_loops(self):
        ancestor = Ingredient.objects.create(label="Ancestor")
        middle = Ingredient.objects.create(label="Middle", parent=ancestor)
        descendant = Ingredient.objects.create(label="Child", parent=middle)

        # Create a loop from ancester back to descendant
        ancestor.parent = descendant
        ancestor.save()

        # This should terminate
        Ingredient.objects.include_ancestors([descendant.id])
