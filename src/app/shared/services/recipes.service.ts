import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, switchMap } from 'rxjs/operators';
import { Observable, BehaviorSubject, fromEvent, of, concat } from 'rxjs';

import { Recipe, RecipeJson } from '../models/recipe.model';
import { Ingredients } from './ingredients.service';
import { shuffle } from '../utils/shuffle';

@Injectable()
export class Recipes {

  private _recipes = new BehaviorSubject<Recipe[]>([]);
  private _filtered: Observable<Recipe[]>;
  private _random: Observable<Recipe[]>;

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

    this._filtered = this.all().pipe(
        switchMap<Recipe[], Recipe[]>(recipes => {
          // Whenever a blacklistChange event is triggered, re-filter all recipes
          return concat(
            // Concat an empty observable so we can build filtered recipes prior to any events
            of(this),
            fromEvent(document, 'blacklistChange')
          ).pipe(
            map<any, Recipe[]>(() => {
              return recipes.filter(recipe => {
                return !recipe.ingredients.some(ingredient => ingredient.blacklisted);
              });
            })
          );
        })
      );

      this._random = this.filtered().pipe(
        switchMap<Recipe[], Recipe[]>(list => {
          return concat(
            of(this),
            fromEvent(document, 'shuffleRecipes')
          ).pipe(
            map<any, Recipe[]>(() => {
              return shuffle(list);
            })
          );
        })
      );
    }

  public all(): Observable<Recipe[]> {
    return this._recipes.asObservable();
  }

  public filtered(): Observable<Recipe[]> {
    return this._filtered;
  }

  public random(): Observable<Recipe[]> {
    return this._random;
  }
}
