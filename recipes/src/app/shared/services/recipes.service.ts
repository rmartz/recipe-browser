import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Observable, BehaviorSubject, combineLatest } from 'rxjs';

import { Ingredient } from '../models/ingredient.model';
import { Recipe, RecipeJson } from '../models/recipe.model';
import { Ingredients } from './ingredients.service';

@Injectable()
export class Recipes {

  private _recipes = new BehaviorSubject<Recipe[]>([]);
  private _filtered: Observable<Recipe[]>;

  constructor(protected http: HttpClient,
              protected ingredients: Ingredients) {
    const url = '/assets/recipes.json';
    this.http.get<RecipeJson[]>(url).pipe(
      map(result => {
        return result.map(record => {
          const ingredients_list = record.ingredients.map(name => ingredients.get(name));
          return new Recipe(record.label, ingredients_list);
        });
      })
    ).subscribe(result => {
      this._recipes.next(result);
    });

    this._filtered = combineLatest<Recipe[], Ingredient[]>(
      this.all(), ingredients.blacklist()
    ).pipe(
      map(([recipes, blacklist]) => {
        return recipes.filter(recipe => {
          return !recipe.ingredients.some(ingredient => {
            return blacklist.includes(ingredient);
          });
        });
      })
    );
  }

  public all(): Observable<Recipe[]> {
    return this._recipes.asObservable();
  }

  public filtered(): Observable<Recipe[]> {
    return this._filtered;
  }
}
