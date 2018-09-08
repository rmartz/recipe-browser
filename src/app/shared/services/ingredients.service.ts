import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject, of } from 'rxjs';
import { Ingredient } from '../models/ingredient.model';

@Injectable()
export class Ingredients {

  private _ingredients = new BehaviorSubject<Ingredient[]>([]);
  private _list: {[name: string]: Ingredient} = {};

  constructor() {  }

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
}
