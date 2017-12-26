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
        if 'limit_to' in self.request.query_params:
            ingredients = self.request.query_params['limit_to'].split(',')
            queryset = Recipe.objects.for_ingredients(filter(None, ingredients))

        if 'has_ingredient' in self.request.query_params:
            ingredient = self.request.query_params['has_ingredient']
            queryset = queryset.filter(ingredients=ingredient)

        return queryset


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
