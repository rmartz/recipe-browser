from rest_framework import serializers

from recipes.models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()

    def get_ingredients(self, obj):
        return [{
            'id': ri.ingredient.id,
            'label': ri.ingredient.label,
            'optional': ri.optional,
            'quantity': ri.quantity,
            'is_trivial': ri.ingredient.is_trivial
        } for ri in obj.recipeingredient_set.all()]

    class Meta:
        model = Recipe
        fields = ('id', 'label', 'ingredients')


class IngredientSerializer(serializers.ModelSerializer):
    weight = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'label', 'weight', 'parent', 'is_trivial')
