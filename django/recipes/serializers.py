from rest_framework import serializers

from recipes.models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'label', 'ingredients')


class IngredientSerializer(serializers.ModelSerializer):
    recipe_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'label', 'recipe_count', 'parent')
