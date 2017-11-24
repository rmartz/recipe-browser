# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from recipes.models import Recipe, Ingredient
from recipes.serializers import RecipeSerializer, IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        queryset = Recipe.objects.all()
        try:
            ingredients = self.request.query_params['ingredients']
            queryset = Recipe.objects.for_ingredients(ingredients)
        except KeyError:
            pass

        return queryset


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
