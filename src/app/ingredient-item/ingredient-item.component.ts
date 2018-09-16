import { Component, Input } from '@angular/core';
import { Ingredient, Rating } from '../shared/models/ingredient.model';

@Component({
  selector: 'app-ingredient-item',
  templateUrl: './ingredient-item.component.html'
})
export class IngredientItemComponent {
  public ratings = Rating;
  @Input() ingredient: Ingredient;

  constructor() { }
}
