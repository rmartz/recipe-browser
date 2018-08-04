import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Observable, BehaviorSubject } from 'rxjs';

import { Recipe, RecipeJson } from '../models/recipe.model';
import { Ingredients } from './ingredients.service';

@Injectable()
export class Recipes {

  private _recipes = new BehaviorSubject<Recipe[]>([]);

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
  }

  public list(): Observable<Recipe[]> {
    return this._recipes.asObservable();
  }
}
