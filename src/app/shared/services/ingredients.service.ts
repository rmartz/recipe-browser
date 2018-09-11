import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject, of, fromEvent } from 'rxjs';
import { Ingredient } from '../models/ingredient.model';
import { switchMap, map, distinct } from 'rxjs/operators';

@Injectable()
export class Ingredients {

  private _ingredients = new BehaviorSubject<Ingredient[]>([]);
  private _list: {[name: string]: Ingredient} = {};
  private _has_favorited: Observable<boolean>;

  constructor() {
    this._has_favorited = this._ingredients.pipe(
      switchMap<Ingredient[], boolean>(ingredients => {
        return fromEvent(document, 'favoriteChange').pipe(
          map(() => {
            return ingredients.some(ingredient => ingredient.favorited);
          })
        );
      })
    );
  }

  public list(): Observable<Ingredient[]> {
    return this._ingredients.asObservable();
  }

  public get(name: string): Ingredient {
    if (!this._list[name]) {
      this._list[name] = new Ingredient(name);
      this._ingredients.next(Object.values(this._list));
    }
    return this._list[name];
  }

  public hasFavorited(): Observable<boolean> {
    return this._has_favorited;
  }
}
