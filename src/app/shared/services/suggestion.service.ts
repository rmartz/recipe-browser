import { Injectable } from '@angular/core';
import { map, switchMap } from 'rxjs/operators';
import { Observable, fromEvent, of, concat } from 'rxjs';

import { Recipe, RecipeWeight } from '../models/recipe.model';
import { Ingredients } from './ingredients.service';
import { Recipes } from './recipes.service';
import { Ingredient, IngredientWeight } from '../models/ingredient.model';

@Injectable()
export class Suggestions {
  private _suggestedRecipes: Observable<RecipeWeight[]>;
  private _suggestedIngredients: Observable<IngredientWeight[]>;

  constructor(protected ingredients: Ingredients,
              protected recipes: Recipes) {

    this._suggestedRecipes = recipes.filtered().pipe(
      switchMap<Recipe[], RecipeWeight[]>(list => {
        // Whenever a blacklistChange event is triggered, re-filter all recipes
        return concat(
          // Concat an empty observable so we can build filtered recipes prior to any events
          of(this),
          fromEvent(document, 'favoriteChange')
        ).pipe(
          map<any, RecipeWeight[]>(() => {
            return list.map(recipe => {
              const weight = (1.0 * recipe.ingredients.filter(ingredient => ingredient.favorited).length
                              / Math.sqrt(recipe.ingredients.length));
              return new RecipeWeight(recipe, weight);
            }).sort((a, b) => b.weight - a.weight);
          })
        );
      })
    );

    this._suggestedIngredients = this.ingredients.list().pipe(
        switchMap<Ingredient[], IngredientWeight[]>(ingredient_list => {
          return this._suggestedRecipes.pipe(
            map<RecipeWeight[], IngredientWeight[]>(recipe_list => {
              return ingredient_list.map(ingredient => {
                // Find all the RecipeWeight objects for recipes that include this ingredient
                const ingredient_recipes = recipe_list.filter(recipe_weight => recipe_weight.recipe.ingredients.includes(ingredient));
                // Sum their weight (Add one for this ingredient)
                const weight = ingredient_recipes.reduce((sum, recipe) => sum + recipe.weight, 0);
                const occurrences = ingredient_recipes.length;
                const additions = ingredient_recipes.filter(recipe => recipe.weight === 0).length;
                return new IngredientWeight(ingredient, weight, occurrences, additions);
              });
            })
          );
        })
      );
  }

  public suggestedRecipes(): Observable<RecipeWeight[]> {
    return this._suggestedRecipes;
  }

  public suggestedIngredients(): Observable<IngredientWeight[]> {
    return this._suggestedIngredients;
  }
}
