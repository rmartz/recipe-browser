from rest_framework import serializers

from recipes.models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()

    def get_ingredients(self, obj):
        return [{
            'id': ri.ingredient.id,
            'label': ri.ingredient.label,
            'optional': ri.optional,
            'quantity': ri.quantity
        } for ri in obj.recipeingredient_set.all()]

    class Meta:
        model = Recipe
        fields = ('id', 'label', 'ingredients')


class IngredientSerializer(serializers.ModelSerializer):
    recipe_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'label', 'recipe_count', 'parent')
