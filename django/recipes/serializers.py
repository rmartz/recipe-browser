from rest_framework import serializers

from recipes.models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'label', 'ingredients')


class IngredientSerializer(serializers.ModelSerializer):
    recipe_count = serializers.SerializerMethodField()

    def get_recipe_count(self, obj):
        return Recipe.objects.filter(ingredients=obj).count()

    class Meta:
        model = Ingredient
        fields = ('id', 'label', 'recipe_count', 'parent')
